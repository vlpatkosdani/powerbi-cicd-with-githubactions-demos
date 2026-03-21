# Automated BPA Analysis with PR Comments

A Python-based solution for analyzing Best Practice Analyzer (BPA) results and posting structured, actionable feedback directly on GitHub pull requests.

## What This Does

This solution takes BPA results from Tabular Editor, analyzes them, categorizes violations by severity, and posts a comprehensive comment on your pull request. Instead of developers hunting through GitHub Actions logs and downloading CSV artifacts, they get immediate feedback right where they're working.

**Key features:**
- Automatic severity-based categorization (Must Correct, Correct ASAP, Nice to Have)
- Structured PR comments with collapsible sections
- Links to rule descriptions for educational context
- Automatic PR labeling (`bpa-failed`, `bpa-warning`, `bpa-passed`)
- Handles GitHub's 65,000 character limit with smart fallback strategies

## Prerequisites

- Power BI project saved as PBIP format
- GitHub repository with GitHub Actions enabled
- Tabular Editor 2.x (downloaded automatically by the workflow)
- Python 3.x (available in GitHub Actions runners)

## Files in This Solution
```
.
├── .github/
│   └── workflows/
│       └── Run_BPA_and_analyse_result.yml          # GitHub Actions workflow
├── scripts/
│   ├── bpa_result_analysis.py        # Analyzes and categorizes BPA results
│   ├── pr_comment.py                 # Posts formatted comment to PR
│   ├── BPA_Rules.json                # Custom BPA rules with CustomSeverity
│   ├── bpa_rules.md                  # Rule descriptions for PR links
│   └── run_bpa.csx                   # C# macro for running BPA
└── README.md                          # This file
```

## How It Works

### 1. BPA Execution (C# Macro)

The `run_bpa.csx` macro runs Tabular Editor with your custom BPA rules and exports violations to a CSV file. This approach consolidates all findings in a single run instead of failing on the first Severity 3 issue.

### 2. Analysis & Categorization (Python)

`bpa_result_analysis.py` reads the BPA output CSV and enriches it with custom severities from `BPA_Rules.json`. The script:

- Merges BPA results with your custom rule definitions
- Splits violations into three CSV files by severity
- Sets a GitHub Actions environment variable (`SEVERITY_3_FOUND`) to control workflow failure

**Severity levels:**
- **Severity 3 (Must Correct):** Critical issues that block deployment
- **Severity 2 (Correct ASAP):** Important but non-blocking issues
- **Severity 1 (Nice to Have):** Suggestions for improvement

### 3. PR Comment Generation (Python)

`pr_comment.py` builds and posts a structured comment with:

**Comment structure:**
1. **Deployment status header** - Clear yes/no answer at the top
2. **Summary table** - Issue counts by severity level
3. **Rule summaries** - Violation counts per rule
4. **Detailed violations** - Collapsible sections with:
   - Rule name and description link
   - List of affected objects (measures, columns, tables)

**Smart features:**
- Severity 3 sections expanded by default, others collapsed
- Handles large comments with progressive truncation (always keeps Severity 3 visible)
- Removes old BPA labels and adds current status label
- Links to workflow artifacts for full CSV downloads

## Setup Instructions

### 1. Add Custom BPA Rules

Create `scripts/BPA_Rules.json` with your rules. **Critical:** Add these fields to each rule:
```json
{
  "ID": 1,
  "Name": "Avoid division (use DIVIDE function instead)",
  "Category": "DAX Expressions",
  "Description": "Use DIVIDE() instead of / operator...",
  "Severity": 2,
  "CustomSeverity": 3,
  "Anchor": "avoid-division",
  "Scope": "Measure, CalculatedColumn",
  "Expression": "Tokenize().Any(Type = DIV and ...)",
  "CompatibilityLevel": 1200
}
```

**Key fields:**
- `ID`: Unique identifier for merging with BPA results
- `CustomSeverity`: Your organization's severity (1-3) - this determines workflow behavior
- `Anchor`: URL-safe slug for linking to rule descriptions

### 2. Create Rule Descriptions

Create `scripts/bpa_rules.md` with detailed explanations for each rule:
```markdown
## Avoid division (use DIVIDE function instead) {#avoid-division}

**Why this matters:**
The `/` operator throws an error on division by zero. The `DIVIDE()` function 
handles this gracefully by returning BLANK() or a custom value.

**How to fix:**
Replace `[Measure1] / [Measure2]` with `DIVIDE([Measure1], [Measure2])`

**Learn more:**
- [DIVIDE function reference](https://dax.guide/divide/)
```

### 3. Add Python Scripts

Copy `bpa_result_analysis.py` and `pr_comment.py` to your `scripts/` folder.

**Key environment variables used:**
- `GITHUB_TOKEN`: Automatically provided by GitHub Actions
- `REPO`: Repository name (e.g., `owner/repo-name`)
- `RUN_ID`: Current workflow run ID
- `PR_NUMBER`: Pull request number

## Customization

### Adjust Severity Thresholds

Edit the `CustomSeverity` field in `BPA_Rules.json` to match your organization's priorities. Only Severity 3 issues will fail the workflow.

### Modify Comment Structure

Edit `pr_comment.py` to adjust:
- Comment sections and ordering
- Collapsible section behavior
- Character limit fallback strategy
- Label names

### Add More Rules

Extend `BPA_Rules.json` with additional rules from:
- [Official BPA rules repository](https://github.com/microsoft/Analysis-Services/tree/master/BestPracticeRules)
- Custom rules specific to your organization

## Troubleshooting

**Comment not posting:**
- Check that `GITHUB_TOKEN` has write permissions for pull requests
- Verify PR number is correctly passed to the script

**Character limit exceeded:**
- The script has built-in fallbacks, but for very large models consider:
  - Reducing the number of rules checked
  - Running BPA only on changed files
  - Splitting checks across multiple workflows

**Workflow always passing despite violations:**
- Check that `CustomSeverity` field exists in your BPA rules
- Verify the environment variable is being set correctly in `bpa_result_analysis.py`

**Rule links broken:**
- Ensure `Anchor` field in JSON matches the heading ID in `bpa_rules.md`
- Use URL-safe characters in anchors (lowercase, hyphens only)

## Example Output

See a live example of the PR comment in action: [Test PR](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/pull/1)

The comment includes:
- ✅ or ❌ deployment status
- 📊 Summary table with issue counts
- 🚨 Expanded Severity 3 issues
- ⚡ Collapsible Severity 2 issues
- 💡 Collapsible Severity 1 suggestions
- 🔗 Links to rule descriptions
- 🏷️ Automatic PR labels

## License

MIT License - feel free to adapt this for your own projects.

## Contributing

Found an issue or have a suggestion? Open an issue or PR in the main repository.

---

**Author:** Dániel Patkós  
**Blog:** [Fabricated Insights](https://substack.com/@fabricatedinsights)  
**LinkedIn:** [Daniel Gabor Patkos](https://www.linkedin.com/in/danielgaborpatkos/)