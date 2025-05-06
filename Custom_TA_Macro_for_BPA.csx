using TabularEditor.BestPracticeAnalyzer;

var model = new TabularModelHandler("Contoso 10k.SemanticModel/definition/database.tmdl").Model;
var bpa = new Analyzer();
bpa.SetModel(model);

Console.WriteLine("BPA Job started");

// Specify the base path and the file name separately
var customRuleCollection = BestPracticeCollection.GetCollectionFromFile(
    ".",
    "BPA_Rules.json"
);

// Instead of directly setting ExternalRuleCollections, use the method in the Analyzer class
bpa.LoadExternalRuleCollections();
bpa.ExternalRuleCollections.Add(customRuleCollection);

var sb = new System.Text.StringBuilder();
string newline = Environment.NewLine;
sb.Append("RuleCategory" + '\t' + "RuleID" + '\t' + "RuleName" + '\t' + "RuleDescription" +  '\t' + "ObjectName" + '\t' + "ObjectType" + '\t' + "RuleSeverity" + '\t' + "HasFixExpression" + newline);

// Analyze using ONLY the custom rules by passing false to all default rule inclusion flags
var results = bpa.Analyze(
    bpa.GetEffectiveRules(
        includeLocalMachineRules: false, 
        includeLocalUserRules: false, 
        includeModelRules: false, 
        includeExternalRules: true
    )
).ToList();

foreach (var a in results)
{
    sb.Append(a.Rule.Category + '\t' + a.Rule.ID + '\t' + a.RuleName + '\t' + a.Rule.Description + '\t' + a.ObjectName + '\t' + a.ObjectType + '\t' + a.Rule.Severity + '\t' + a.CanFix + newline);
}

// Print output to console (for GitHub Actions logs)
Console.WriteLine(sb.ToString());

string outputPath =  "BPA_Results.csv";


// Then save as outputFile
using (var writer = new System.IO.StreamWriter(outputPath, false))
{
    writer.Write(sb.ToString());
}

Console.WriteLine("Results exported to: " + outputPath);