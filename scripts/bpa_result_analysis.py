import pandas as pd
import json
import os

# ---- Step 1: Load BPA CSV result
csv_path = "BPA_Results.csv"  # <- your BPA output csv file
csv_df = pd.read_csv(csv_path, sep="\t")

# ---- Step 2: Load the JSON file (Rules with SuggestedSeverity)
json_path = "main_branch_scripts/scripts/BPA_Rules.json"  # <- your JSON file
with open(json_path, 'r', encoding='utf-8') as f:
    rules_data = json.load(f)

rules_df = pd.DataFrame(rules_data)

# ---- Step 3: Fix column names for merging
# csv_df has RuleID (e.g., 1, 2, 3), json has ID (integer)
# Ensure RuleID column is integer
csv_df["RuleID"] = csv_df["RuleID"].astype(int)

# ---- Step 4: Left Join CSV (runtime issues) with JSON (static rule properties)
merged_df = csv_df.merge(rules_df[['ID', 'CustomSeverity']], how='left', left_on='RuleID', right_on='ID')

merged_df = merged_df.rename(columns={'CustomSeverity': 'VL_Severity', 'RuleDescription': 'Description'})


columns_to_keep = ['RuleCategory', 'RuleID', 'RuleName', 'ObjectName', 'ObjectType', 'VL_Severity', 'Description']


# ---- Step 5: Create Summary Tables
must_correct = merged_df[merged_df['VL_Severity'] == 3]
correct_asap = merged_df[merged_df['VL_Severity'] == 2]
nice_to_have = merged_df[merged_df['VL_Severity'] == 1]

# ---- Step 6: Output
print("\n=== MUST CORRECT ===")
print(must_correct[columns_to_keep])

print("\n=== CORRECT ASAP ===")
print(correct_asap[columns_to_keep])

print("\n=== NICE TO HAVE ===")
print(nice_to_have[columns_to_keep])

# ---- Step 7: Optionally export to CSV
must_correct[columns_to_keep].to_csv("must_correct.csv", index=False)
correct_asap[columns_to_keep].to_csv("correct_asap.csv", index=False)
nice_to_have[columns_to_keep].to_csv("nice_to_have.csv", index=False)


# ---- Step 8: Mark result using GitHub Actions environment variable
if not must_correct.empty:
    with open(os.environ['GITHUB_ENV'], "a") as env_file:
        env_file.write(f"SEVERITY_3_FOUND=true\n")
    print("Must Correct (Severity 3) issues detected. Model should not be deployed.")  # <-- no emoji
else:
    with open(os.environ['GITHUB_ENV'], "a") as env_file:
        env_file.write(f"SEVERITY_3_FOUND=false\n")
    print("No critical Severity 3 issues found.")  # <-- no emoji