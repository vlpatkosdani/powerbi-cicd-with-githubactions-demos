# Power BI CI/CD with GitHub Actions – Demos & Scenarios

This repository is part of a blog series demonstrating how to implement **CI/CD practices in Power BI projects using GitHub Actions**.

The goal is to provide **step-by-step examples** that automate validation, formatting, and review tasks in `.pbip`-based Power BI projects.  
Each branch represents a different scenario with growing complexity and value — from basic BPA validation to full pipeline setups.

---

> 💡 The `main` branch always reflects the **latest available version** from the blog series.

---

## 🧭 Scenario Overview

| Status | Scenario | Branch | Description |
|--------|----------|--------|-------------|
| ✅ | Basic Scenario 1 – Default BPA Ruleset | [`basic-scenario-1-default-bpa-rules`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/basic-scenario-1-default-bpa-ruleset) | Run BPA using the default ruleset by referencing its URL from Tabular Editor's GitHub repo |
| ✅ | Basic Scenario 2 – Custom BPA Ruleset | [`basic-scenario-2-custom-bpa-rules`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/basic-scenario-2-custom-bpa-ruleset) | Use a local JSON file with a custom BPA rule |
| ✅ | Intermediate Scenario 1 – BPA via C# Macro with Consolidated Output | [`intermediate-scenario-1-bpa-macro-csharp`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/intermediate-scenario-1-bpa-macro-csharp) | Run BPA with a custom C# script to consolidate results into a CSV and support full custom rulesets |
| ✅ | Advanced Scenario 1 – Automated BPA Analysis with PR Comments | [`advanced-scenario-1-bpa-analysis-pr-comments`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/advanced-scenario-1-bpa-analysis-pr-comments) | Analyze BPA results with Python and post structured comments directly on pull requests |
| ✅ | Advanced Scenario 2 – Scaling with Central Repository | [`advanced-scenario-2-central-repo`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/advanced-scenario-2-central-repo) | Set up a central repository for reusable workflows and scripts that can be called from multiple project repositories |

---

## 📄 Related Blog Posts

### 📝 Background & Thought Process

| Article | Description |
|---------|-------------|
| ✅ [From Version Chaos to CI/CD – Power BI Version Control with GitHub](https://fabricatedinsights.substack.com/p/from-version-chaos-to-cicd-power?r=2pu5jb) | Why versioning matters and what CI/CD means in a Power BI context |
| ✅ [Building Your Power BI CI/CD Pipeline – Part 1](https://fabricatedinsights.substack.com/p/building-your-power-bi-cicd-pipeline?r=2pu5jb) | Why you should use BPA to improve the quality and consistency of your model |
| ✅ [Building Your Power BI CI/CD Pipeline – Part 2](https://fabricatedinsights.substack.com/p/building-your-power-bi-cicd-pipeline-660?r=2pu5jb) | Thoughts on: selecting the right BPA rules for your project and adjusting severity levels—deciding how strictly best practices should be enforced |

---

### ⚙️ Technical Tutorials (This Repo)

| Article | Branch |
|---------|--------|
| ✅ [Part 1 – Run BPA with default ruleset](https://fabricatedinsights.substack.com/i/160480588/step-a-create-your-first-github-actions-workflow) | [`basic-scenario-1-default-bpa-rules`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/basic-scenario-1-default-bpa-ruleset) |
| ✅ [Part 1 – Use a custom BPA rule](https://fabricatedinsights.substack.com/i/160480588/step-b-modify-your-first-github-actions-workflow) | [`basic-scenario-2-custom-bpa-rules`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/basic-scenario-2-custom-bpa-ruleset) |
| ✅ [Part 2 – Automating BPA with C# in Tabular Editor + GitHub Actions](https://fabricatedinsights.substack.com/p/automating-bpa-with-c-in-tabular) | [`intermediate-scenario-1-bpa-macro-csharp`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/intermediate-scenario-1-bpa-macro-csharp) |
| ✅ [Part 3 – Making BPA Results Actionable with Automated PR Comments](https://fabricatedinsights.substack.com/p/making-bpa-results-actionable-with) | [`advanced-scenario-1-bpa-analysis-pr-comments`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/advanced-scenario-1-bpa-analysis-pr-comments) |
| ✅ [Part 4 – Scaling Your CI/CD Pipeline Across Projects](link-to-part4) | [`advanced-scenario-2-central-repo`](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/advanced-scenario-2-central-repo-setup) |

---

## 🏁 Getting Started

To test any scenario locally:

1. Clone the repository:
```bash
git clone https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos.git
```

2. Switch to the scenario you want to follow:
```bash
git checkout basic-scenario-1-default-bpa-rules
```

3. Open in VS Code and review the `.pbip` project and GitHub Actions YAML file

4. Push a change or run the workflow manually on GitHub

---

## 🧰 Features in This Series

✅ Already covered:
- Running **Tabular Editor's BPA** with default & custom rulesets  
- Using GitHub Actions to fail workflows based on BPA severity  
- Adding rule-breaking DAX examples for testing
- Consolidating BPA results into a CSV using a custom C# macro
- **Analyzing BPA results with Python and posting structured PR comments**
- **Categorizing violations by severity (Must Correct, Correct ASAP, Nice to Have)**
- **Automatic PR labeling based on BPA status**
- **Setting up a central repository for reusable workflows**
- **Creating repository templates for standardized project setup**
- **Conditional workflow execution based on PR content**
- **Using CODEOWNERS for default approvers**


---

## 🙌 Feedback

Have questions, suggestions, or ideas for new scenarios?  
Feel free to [open an issue](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/issues) or reach out on [LinkedIn](https://www.linkedin.com/in/danielgaborpatkos/).

---

📌 Maintained by: [Daniel Patkos](https://www.linkedin.com/in/danielgaborpatkos/)  
🛠️ Powered by: Power BI, GitHub Actions, Tabular Editor