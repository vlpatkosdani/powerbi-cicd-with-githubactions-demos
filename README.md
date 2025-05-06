## Intermediate Scenario 1 – Automate BPA with a C# Script

📍 This branch matches Part 2 of the blog series:  
[Automating BPA with C# in Tabular Editor + GitHub Actions](https://fabricatedinsights.substack.com/p/automating-bpa-with-c-in-tabular)

This branch extends previous scenarios by:

- Using a C# macro script to execute BPA in Tabular Editor  
- Consolidating all BPA issues into a single CSV output for easier analysis  
- Leveraging a fully custom BPA ruleset stored locally  
- Avoiding repeated runs for each Severity 3 issue  
- Demonstrating local testing and silent failure handling strategies

📝 Key files in this branch:

- [`Custom_TA_Macro_for_BPA.csx`](./Custom_TA_Macro_for_BPA.csx) – the custom script  
- [`BPA_Rules.json`](./BPA_Rules.json) – your editable ruleset  
- [`.github/workflows/Run_BPA_via_Custom_Macro.yml`](./.github/workflows/Run_BPA_via_Custom_Macro.yml) – updated to use the `-S` flag to run the script

🔗 Full Overview & Future Scenarios

👉 See the full list of scenarios and CI/CD goals in the  
[main branch README](https://github.com/vlpatkosdani/powerbi-cicd-with-githubactions-demos#-scenario-overview)
