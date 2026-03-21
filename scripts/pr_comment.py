
import pandas as pd
import requests
import os
import json
import re

# --- Configuration ---
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO = os.getenv('REPO')
RUN_ID = os.getenv('GITHUB_RUN_ID')
PR_NUMBER = os.getenv('PR_NUMBER')

# --- Load CSVs ---
must_correct = pd.read_csv('must_correct.csv')
correct_asap = pd.read_csv('correct_asap.csv')
nice_to_have = pd.read_csv('nice_to_have.csv')

# --- Load Rules with anchors ---
with open("main_branch_scripts/scripts/BPA_Rules.json") as f:
    RULES = {r['Name']: r for r in json.load(f)}

# --- Helpers ---
def get_anchor(rule_name):
    anchor = RULES.get(rule_name, {}).get("Anchor", "")
    if not anchor:
        anchor = re.sub(r'[^a-zA-Z0-9]+', '-', rule_name.strip()).lower()
    return anchor


def format_violations(df, expanded=True):
    if df.empty:
        return ""

    output = []
    grouped = df.groupby('RuleName')
    for rule, group in grouped:
        objects = group[['ObjectName', 'ObjectType']].dropna().drop_duplicates().values.tolist()
        anchor = get_anchor(rule)
        rule_link = f"https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/blob/main/scripts//bpa_rules.md#{anchor}"

        output.append(
            f"<details{' open' if expanded else ''}>\n"
            f"<summary><h4>🔎 {rule} – "
            f"<a href='{rule_link}' target='_blank'>Rule Description 🔗</a></h4></summary>\n"
        )

        formatted_objects = [f"**{obj}** ({typ})" for obj, typ in objects]
        if len(formatted_objects) > 10:
            columns = [formatted_objects[i::3] for i in range(3)]
            max_len = max(len(col) for col in columns)
            output.append("\n| List of Issues | List of Issues | List of Issues |")
            output.append("|:---------------|:---------------|:---------------|")
            for i in range(max_len):
                row = [columns[col][i] if i < len(columns[col]) else "" for col in range(3)]
                output.append("| " + " | ".join(row) + " |")
        else:
            output.extend([f"- {item}" for item in formatted_objects])

        output.append("</details>\n\n\n")
    return "\n".join(output)


def build_rule_summary(df):
    if df.empty:
        return ""
    rule_counts = df['RuleName'].value_counts().reset_index()
    rule_counts.columns = ['RuleName', 'Violations']
    rule_counts = rule_counts.sort_values('Violations', ascending=False)
    table = "| RuleName | Violations |\n|:---------|-----------:|\n"
    table += "\n".join([f"| {row['RuleName']} | {row['Violations']} |" for _, row in rule_counts.iterrows()])
    return table

def generate_message(include_sev3=True, include_sev2=True, include_sev1=True, summary_only_sev1=False, summary_only_sev2=False):
    message = result_message + artifact_section + summary_table
    if include_sev3:
        message += f"\n\n## 🚨 Must Correct (Severity 3)\n\n{build_rule_summary(must_correct)}\n\n{format_violations(must_correct)}"
    if include_sev2:
        message += "\n\n## ⚡ Correct ASAP (Severity 2)\n\n"
        message += build_rule_summary(correct_asap)
        if not summary_only_sev2:
            message += f"\n\n{format_violations(correct_asap)}"
        else:
            message += "\n\nToo many issues to display. Please check the artifacts for full results.\n"
    if include_sev1:
        message += "\n\n## 💡 Nice to Have (Severity 1)\n\n"
        message += build_rule_summary(nice_to_have)
        if not summary_only_sev1:
            message += f"\n\n<details><summary><strong>Click to check details</strong></summary>\n\n{format_violations(nice_to_have)}\n</details>"
        else:
            message += "\n\nToo many issues to display. Please check the artifacts for full results.\n"
    return message

# --- Result Status ---
if must_correct.empty:
    if correct_asap.empty:
        result_message = (
            "# ✅ Model can be deployed. No Severity 3 (critical) or Severity 2 issues found.\n\n"
            "### 💡 You can still improve model quality by addressing Severity 1 issues (if any)."
        )
    else:
        result_message = (
            "# ✅ Model can be deployed. No Severity 3 (critical) issues found.\n\n"
            "### ⚡ You should still fix Severity 2 issues ASAP to improve model quality!"
        )
else:
    result_message = "# ❌ Model cannot be deployed until Severity 3 issues are fixed."

artifact_link = f"https://github.com/{REPO}/actions/runs/{RUN_ID}"
artifact_section = f"\n\n📂 **BPA Result & Result analysis (CSV downloads):** [View .zip files Here]({artifact_link})\n"

summary_table = f"""### 📊 Summary

| Severity Level | Number of Issues |
|:---------------|-----------------:|
| 🚨 Must Correct | {len(must_correct)} |
| ⚡ Correct ASAP | {len(correct_asap)} |
| 💡 Nice to Have | {len(nice_to_have)} |
"""

# --- Generate the PR body with fallback truncation ---
comment_body = generate_message()
if len(comment_body) > 65000:
    comment_body = generate_message(include_sev3=True, include_sev2=True, include_sev1=True, summary_only_sev1=True)
if len(comment_body) > 65000:
    comment_body = generate_message(include_sev3=True, include_sev2=True, summary_only_sev2=True, include_sev1=False)
if len(comment_body) > 65000:
    comment_body = generate_message(include_sev3=True, include_sev2=False, include_sev1=False)
if len(comment_body) > 65000:
    comment_body = generate_message(include_sev3=False, include_sev2=False, include_sev1=True)

# --- Post PR Comment ---
url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/comments"
payload = {"body": comment_body}
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
response = requests.post(url, headers=headers, data=json.dumps(payload))
if response.status_code != 201:
    print(f"Failed to comment on PR: {response.status_code} - {response.text}")
else:
    print("Successfully added comment to PR.")

# --- Label PR ---
if not must_correct.empty:
    new_label = "bpa-failed"
elif not correct_asap.empty:
    new_label = "bpa-warning"
else:
    new_label = "bpa-passed"

labels_url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/labels"
labels_response = requests.get(labels_url, headers=headers)

if labels_response.status_code == 200:
    existing_labels = [label['name'] for label in labels_response.json()]
    old_bpa_labels = [label for label in existing_labels if label.startswith("bpa-")]

    for label in old_bpa_labels:
        delete_url = f"https://api.github.com/repos/{REPO}/issues/{PR_NUMBER}/labels/{label}"
        delete_response = requests.delete(delete_url, headers=headers)
        if delete_response.status_code == 200:
            print(f"Removed old label: {label}")
        else:
            print(f"Failed to remove label: {label} | {delete_response.text}")
else:
    print(f"Failed to fetch existing labels: {labels_response.text}")

add_payload = {"labels": [new_label]}
add_response = requests.post(labels_url, headers=headers, data=json.dumps(add_payload))
if add_response.status_code in (200, 201):
    print(f"Successfully applied label: {new_label}")
else:
    print(f"Failed to apply label: {add_response.status_code} - {add_response.text}")
