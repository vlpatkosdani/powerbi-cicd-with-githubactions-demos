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
| ✅ | Basic Scenario 1 – Default BPA Ruleset | [`basic-scenario-1-default-bpa-rules`]([https://github.com/your-org/your-repo/tree/basic-scenario-1-default-bpa-rules](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/basic-scenario-1-default-bpa-ruleset)) | Run BPA using the default ruleset by referencing its URL from Tabular Editor’s GitHub repo |
| ✅ | Basic Scenario 2 – Custom BPA Ruleset | [`basic-scenario-2-custom-bpa-rules`]([https://github.com/your-org/your-repo/tree/basic-scenario-2-custom-bpa-rules](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos/tree/basic-scenario-2-custom-bpa-ruleset)) | Use a local JSON file with a custom BPA rule |
| ⏳ | Intermediate Scenario 1 – BPA with result analysis | _coming soon_ | Parse and handle BPA output programmatically |
| ⏳ | Advanced Scenario 1 – Full CI/CD Workflow | _coming soon_ | Combine validations, PR checks, formatting, and more |

---

## 📄 Related Blog Posts

### 📝 Background & Thought Process

| Article | Description |
|---------|-------------|
| ✅ [From Version Chaos to CI/CD – Power BI Version Control with GitHub](https://fabricatedinsights.substack.com/p/from-version-chaos-to-cicd-power?r=2pu5jb) | Why versioning matters and what CI/CD means in a Power BI context |
| ✅ [Building Your Power BI CI/CD Pipeline – Part 1](https://fabricatedinsights.substack.com/p/building-your-power-bi-cicd-pipeline?r=2pu5jb) | Why you should use BPA to improve the quality and consistency of your model |
| ✅ [Building Your Power BI CI/CD Pipeline – Part 2](https://fabricatedinsights.substack.com/p/building-your-power-bi-cicd-pipeline-660?r=2pu5jb) | Thoughts on: electing the right BPA rules for your project and adjusting severity levels—deciding how strictly best practices should be enforced |

---

### ⚙️ Technical Tutorials (This Repo)

| Article | Branch |
|---------|--------|
| ✅ [Part 1 – Run BPA with default ruleset](#) | `basic-scenario-1-default-bpa-rules` |
| ✅ [Part 2 – Use a custom BPA rule](#) | `basic-scenario-2-custom-bpa-rules` |
| ⏳ Part 3 – Analyze and interpret BPA output | _coming soon_ |
| ⏳ Part 4 – Pull request validation with GitHub Actions | _coming soon_ |
| ⏳ Part 5 – Full Power BI CI/CD pipeline | _coming soon_ |

---

## 🏁 Getting Started

To test any scenario locally:

1. Clone the repository:

2. Switch to the scenario you want to follow:

3. Open in VS Code and review the `.pbip` project and GitHub Actions YAML file

4. Push a change or run the workflow manually on GitHub

---

## 🧰 Features in This Series

✅ Already covered:
- Running **Tabular Editor’s BPA** with default & custom rulesets  
- Using GitHub Actions to fail workflows based on BPA severity  
- Adding rule-breaking DAX examples for testing  

🔜 Coming soon:
- Parsing BPA output for better reporting
- Using **Power BI Inspector** for visual best practice checks
- **Auto-formatting DAX** 
- Validating changes in **pull requests**

---

## 🙌 Feedback

Have questions, suggestions, or ideas for new scenarios?  
Feel free to [open an issue](https://github.com/your-org/powerbi-cicd-with-githubactions-demos/issues) or reach out on LinkedIn.

---

📌 Maintained by: [Daniel Patkos](https://www.linkedin.com/in/danielgaborpatkos/)  
🛠️ Powered by: Power BI, GitHub Actions, Tabular Editor
