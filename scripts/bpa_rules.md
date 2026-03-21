<details open>
<summary>### 🔥 Severity 3 (Must Correct)</summary>


#### <a name="avoid-division-use-divide-function-instead"></a>Avoid division (use DIVIDE function instead) (Severity 3)

Calculated Columns, Measures or Calculated Tables should not use the division symbol in their expressions (/) unless the denominator is a constant value. Instead, it is advised to always use the DIVIDE(<numerator>,<denominator>) function.

&nbsp;

---


#### <a name="dax-expressions-avoid-using-the-iferror-function"></a>[DAX Expressions] Avoid using the IFERROR function (Severity 3)

Avoid using the IFERROR function as it may cause performance degradation. If you are concerned about a divide-by-zero error, use the DIVIDE function as it naturally resolves such errors as blank (or you can customize what should be shown in case of such an error). Reference: https://www.elegantbi.com/post/top10bestpractices

&nbsp;

---

#### <a name="dax-expressions-avoid-using-the-iserror-function"></a>[DAX Expressions] Avoid using the ISERROR function (Severity 3)

Similarly to IFERROR, the usage of ISERROR can also have a negative impact on the performance.

&nbsp;

---

#### <a name="dax-expressions-column-references-should-be-fully-qualified"></a>[DAX Expressions] Column references should be fully qualified (Severity 3)

Using fully qualified column references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a column in DAX, first specify the table name, then specify the column name in square brackets. Reference: https://www.elegantbi.com/post/top10bestpractices

&nbsp;

---

#### <a name="dax-expressions-filter-column-values-with-proper-syntax"></a>[DAX Expressions] Filter column values with proper syntax (Severity 3)

Instead of using this pattern FILTER('Table','Table'[Column]="Value") for the filter parameters of a CALCULATE or CALCULATETABLE function, use one of the options below. As far as whether to use the KEEPFILTERS function, see the second reference link below. Option 1: KEEPFILTERS('Table'[Column]="Value") Option 2: 'Table'[Column]="Value" Reference: https://docs.microsoft.com/power-bi/guidance/dax-avoid-avoid-filter-as-filter-argument Reference: https://www.sqlbi.com/articles/using-keepfilters-in-dax/

&nbsp;

---

#### <a name="dax-expressions-measure-references-should-be-unqualified"></a>[DAX Expressions] Measure references should be unqualified (Severity 3)

Using unqualified measure references makes it easier to distinguish between column and measure references, and also helps avoid certain errors. When referencing a measure using DAX, do not specify the table name. Use only the measure name in square brackets. Reference: https://www.elegantbi.com/post/top10bestpractices

&nbsp;

---

#### <a name="dax-expressions-measures-should-not-be-direct-references-of-other-measures"></a>[DAX Expressions] Measures should not be direct references of other measures (Severity 3)

This rule identifies measures which are simply a reference to another measure. As an example, consider a model with two measures: [MeasureA] and [MeasureB]. This rule would be triggered for MeasureB if MeasureB's DAX was MeasureB:=[MeasureA]. Such duplicative measures should be removed.

&nbsp;

---

#### <a name="dax-expressions-no-two-measures-should-have-the-same-definition"></a>[DAX Expressions] No two measures should have the same definition (Severity 3)

Two measures with different names and defined by the same DAX expression should be avoided to reduce redundancy.

&nbsp;

---

#### <a name="error-prevention-avoid-invalid-characters-in-descriptions"></a>[Error Prevention] Avoid invalid characters in descriptions (Severity 3)

This rule identifies if a description for a given object in your model (i.e. table/column/measure) which contains an invalid character. Invalid characters will cause an error when deploying the model (and failure to deploy). This rule has a fix expression which converts the invalid character into a space, resolving the issue.

&nbsp;

---

#### <a name="error-prevention-avoid-invalid-characters-in-names"></a>[Error Prevention] Avoid invalid characters in names (Severity 3)

This rule identifies if a name for a given object in your model (i.e. table/column/measure) which contains an invalid character. Invalid characters will cause an error when deploying the model (and failure to deploy). This rule has a fix expression which converts the invalid character into a space, resolving the issue.

&nbsp;

---

#### <a name="error-prevention-avoid-the-userelationship-function-and-rls-against-the-same-table"></a>[Error Prevention] Avoid the USERELATIONSHIP function and RLS against the same table (Severity 3)

The USERELATIONSHIP function may not be used against a table which also leverages row-level security (RLS). This will generate an error when using the particular measure in a visual. This rule will highlight the table which is used in a measure's USERELATIONSHIP function as well as RLS. Reference: https://blog.crossjoin.co.uk/2013/05/10/userelationship-and-tabular-row-security/

&nbsp;

---

#### <a name="error-prevention-data-columns-must-have-a-source-column"></a>[Error Prevention] Data columns must have a source column (Severity 3)

Data columns must have a source column. A data column without a source column will cause an error when processing the model.

&nbsp;

---

#### <a name="error-prevention-expression-reliant-objects-must-have-an-expression"></a>[Error Prevention] Expression-reliant objects must have an expression (Severity 3)

Calculated columns, calculation items and measures must have an expression. Without an expression, these objects will not show any values.

&nbsp;

---

#### <a name="error-prevention-set-isavailableinmdx-to-true-on-necessary-columns"></a>[Error Prevention] Set IsAvailableInMdx to true on necessary columns (Severity 3)

In order to avoid errors, ensure that attribute hierarchies are enabled if a column is used for sorting another column, used in a hierarchy, used in variations, or is sorted by another column.

&nbsp;

---

#### <a name="formatting-month-as-a-string-must-be-sorted"></a>[Formatting] Month (as a string) must be sorted (Severity 3)

This rule highlights month columns which are strings and are not sorted. If left unsorted, they will sort alphabetically (i.e. April, August...). Make sure to sort such columns so that they sort properly (January, February, March...).

&nbsp;

---

#### <a name="formatting-objects-should-not-start-or-end-with-a-space"></a>[Formatting] Objects should not start or end with a space (Severity 3)

Objects should not start or end with a space

&nbsp;

---

#### <a name="maintenance-fix-referential-integrity-violations"></a>[Maintenance] Fix referential integrity violations (Severity 3)

This rule highlights relationships which have referential integrity violations. This indicates that there are values in the table on the 'from' side of the relationship which do not exist in the table on the 'to' side of the relationship. Referential integrity violations will also produce the 'blank' member value in slicers. It is recommended to fix these issues by ensuring that the 'to' table's primary key column has all the values in the 'from' table's foreign key column. Reference: https://blog.enterprisedna.co/vertipaq-analyzer-tutorial-relationships-referential-integrity/

&nbsp;

---

#### <a name="naming-conventions-object-names-must-not-contain-special-characters"></a>[Naming Conventions] Object names must not contain special characters (Severity 3)

Tabs, line breaks, etc.

&nbsp;

---

#### <a name="performance-check-if-bi-directional-and-many-to-many-relationships-are-valid"></a>[Performance] Check if bi-directional and many-to-many relationships are valid (Severity 3)

Bi-directional and many-to-many relationships may cause performance degradation or even have unintended consequences. Make sure to check these specific relationships to ensure they are working as designed and are actually necessary. Reference: https://www.sqlbi.com/articles/bidirectional-relationships-and-ambiguity-in-dax/

&nbsp;

---

#### <a name="performance-reduce-number-of-calculated-columns"></a>[Performance] Reduce number of calculated columns (Severity 3)

Calculated columns do not compress as well as data columns so they take up more memory. They also slow down processing times for both the table as well as process recalc. Offload calculated column logic to your data warehouse and turn these calculated columns into data columns. Reference: https://www.elegantbi.com/post/top10bestpractices

&nbsp;

---

#### <a name="performance-remove-auto-date-table"></a>[Performance] Remove auto-date table (Severity 3)

Avoid using auto-date tables. Make sure to turn off auto-date table in the settings in Power BI Desktop. This will save memory resources. Reference: https://www.youtube.com/watch?v=xu3uDEHtCrg

&nbsp;

---

#### <a name="performance-split-date-and-time"></a>[Performance] Split date and time (Severity 3)

This rule finds datetime columns that have values not at midnight. To maximize performance, the time element should be split from date element (or the time component should be rounded to midnight as this will reduce column cardinality). Reference: https://www.sqlbi.com/articles/separate-date-and-time-in-powerpivot-and-bism-tabular/


</details>

&nbsp;

---

<details open>
<summary>### ⚠️ Severity 2 (Correct ASAP)</summary>


#### <a name="avoid-single-attribute-dimensions-that-are-not-shared-by-multiple-facts"></a>Avoid single-attribute dimensions that are not shared by multiple facts (Severity 2)

In general, over-normalization should be avoided. If a dimension only holds a single attribute and the dimension is not shared by multiple facts, consider moving the attribute to the fact table.

&nbsp;

---

#### <a name="disable-attribute-hierachies-to-decrease-processing"></a>Disable attribute hierachies to decrease processing (Severity 2)

Disable Attribute hierarchies for hidden collumns. This will ensure faster processing.

&nbsp;

---

#### <a name="do-not-use-floating-point-data-types"></a>Do not use floating point data types (Severity 2)

Floating point datatypes can cause unexpected results when evaluating values close to 0. Use Currency / Fixed Decimal Number (decimal) instead.

&nbsp;

---

#### <a name="dax-expressions-avoid-using-1-xy-syntax"></a>[DAX Expressions] Avoid using '1-(x/y)' syntax (Severity 2)

Instead of using the '1-(x/y)' or '1+(x/y)' syntax to achieve a percentage calculation, use the basic DAX functions (as shown below). Using the improved syntax will generally improve the performance. The '1+/-...' syntax always returns a value whereas the solution without the '1+/-...' does not (as the value may be 'blank'). Therefore the '1+/-...' syntax may return more rows/columns which may result in a slower query speed. Let's clarify with an example: Avoid this: 1 - SUM ( 'Sales'[CostAmount] ) / SUM( 'Sales'[SalesAmount] ) Better: DIVIDE ( SUM ( 'Sales'[SalesAmount] ) - SUM ( 'Sales'[CostAmount] ), SUM ( 'Sales'[SalesAmount] ) ) Best: VAR x = SUM ( 'Sales'[SalesAmount] ) RETURN DIVIDE ( x - SUM ( 'Sales'[CostAmount] ), x )

&nbsp;

---

#### <a name="formatting-do-not-summarize-numeric-columns"></a>[Formatting] Do not summarize numeric columns (Severity 2)

Numeric columns (integer, decimal, double) should have their SummarizeBy property set to "None" to avoid accidental summation in Power BI (create measures instead).

&nbsp;

---

#### <a name="formatting-provide-format-string-for-measures"></a>[Formatting] Provide format string for measures (Severity 2)

Visible measures should have their format string property assigned

&nbsp;

---

#### <a name="maintenance-calculation-groups-with-no-calculation-items"></a>[Maintenance] Calculation groups with no calculation items (Severity 2)

Calculation groups have no function unless they have calculation items.

&nbsp;

---

#### <a name="performance-consider-a-star-schema-instead-of-a-snowflake-architecture"></a>[Performance] Consider a star-schema instead of a snowflake architecture (Severity 2)

Generally speaking, a star-schema is the optimal architecture for tabular models. That being the case, there are valid cases to use a snowflake approach. Please check your model and consider moving to a star-schema architecture. Reference: https://docs.microsoft.com/power-bi/guidance/star-schema

&nbsp;

---

#### <a name="performance-large-tables-should-be-partitioned"></a>[Performance] Large tables should be partitioned (Severity 2)

Large tables should be partitioned in order to optimize processing. In order for this rule to run properly, you must run the script shown here: https://www.elegantbi.com/post/vertipaqintabulareditor

&nbsp;

---

#### <a name="performance-model-should-have-a-date-table"></a>[Performance] Model should have a date table (Severity 2)

Generally speaking, models should generally have a date table. Models that do not have a date table generally are not taking advantage of features such as time intelligence or may not have a properly structured architecture.

&nbsp;

---

#### <a name="performance-reduce-usage-of-calculated-tables"></a>[Performance] Reduce usage of calculated tables (Severity 2)

Migrate calculated table logic to your data warehouse. Reliance on calculated tables will lead to technical debt and potential misalignments if you have multiple models on your platform.

&nbsp;

---

#### <a name="performance-reduce-usage-of-long-length-columns-with-high-cardinality"></a>[Performance] Reduce usage of long-length columns with high cardinality (Severity 2)

It is best to avoid lengthy text columns. This is especially true if the column has many unique values. These types of columns can cause longer processing times, bloated model sizes, as well as slower user queries. Long length is defined as more than 100 characters.

&nbsp;

---

#### <a name="performance-remove-redundant-columns-in-related-tables"></a>[Performance] Remove redundant columns in related tables (Severity 2)

Removing unnecessary columns reduces model size and speeds up data loading.

&nbsp;

---

#### <a name="performance-unpivot-pivoted-month-data"></a>[Performance] Unpivot pivoted (month) data (Severity 2)

Avoid using pivoted data in your tables. This rule checks specifically for pivoted data by month. Reference: https://www.elegantbi.com/post/top10bestpractices


</details>

&nbsp;

---

<details open>
<summary>### 💡 Severity 1 (Nice to Have)</summary>


#### <a name="add-objects-to-perspectives"></a>Add objects to perspectives (Severity 1)

Visible tables, columns, measures and hierarchies should be assigned to at least one perspective, if the Tabular Model uses perspectives. Otherwise, the objects will only be visible when connecting directly to the model.

&nbsp;

---

#### <a name="hide-foreign-key-columns"></a>Hide foreign key columns (Severity 1)

Columns used on the Many side of a relationship should be hidden, as the related (dimension) table is likely the best place to apply a filter context.

&nbsp;

---

#### <a name="organize-measures-in-display-folders"></a>Organize measures in display folders (Severity 1)

Tables with more than 10 visible measures should have them organized in display folders for improved usability

&nbsp;

---

#### <a name="provide-format-string-for-visible-numeric-columns"></a>Provide format string for visible numeric columns (Severity 1)

Visible numeric columns should have their Format String property assigned

&nbsp;

---

#### <a name="remove-unused-columns"></a>Remove unused columns (Severity 1)

Hidden columns, which do not have any dependencies, are not used in any relationships, not used in any hierarchies and not used as the SortByColumn for other columns, will likely not be used by clients and thus take up unnecessary space. Consider removing the columns from the model to save space and improve processing time, if you are certain that no external DAX or MDX queries make use of the columns.

&nbsp;

---

#### <a name="remove-unused-measures"></a>Remove unused measures (Severity 1)

Hidden measures, that are not referenced by any DAX expression, should be removed.

&nbsp;

---

#### <a name="revisit-todo-expressions"></a>Revisit TODO expressions (Severity 1)

Objects with an expression containing the word "TODO" (typically as a comment), should most likely be revisited.

&nbsp;

---

#### <a name="specify-application-name-in-connection-string"></a>Specify Application Name in connection string (Severity 1)

When connecting to a SQL Server data source, specify an Application Name in your connection string to let your DBA know where the connection is coming from. For example, you could specify "AnalysisServicesTabular <ServerName> <ModelName>" replacing <ServerName> with the name of your AS instance and <ModelName> with the name of your model.

&nbsp;

---

#### <a name="translate-display-folders"></a>Translate Display Folders (Severity 1)

Display Folder translations should be assigned for objects where the base DisplayFolder property has been assigned. Otherwise, users connecting to the model using a specific Culture will not see the Display Folder structure.

&nbsp;

---

#### <a name="translate-hierarchy-levels"></a>Translate Hierarchy Levels (Severity 1)

When the model contains one or more cultures, all levels on visible hirearchies should have their a translation applied to their name in all cultures.

&nbsp;

---

#### <a name="translate-object-descriptions"></a>Translate Object Descriptions (Severity 1)

When the model contains one or more cultures, all objects that have descriptions applied, should also have translated descriptions applied.

&nbsp;

---

#### <a name="translate-perspectives"></a>Translate Perspectives (Severity 1)

When the model contains one or more cultures, the model object and any perspectives in the model should have a translated name assigned in all cultures.

&nbsp;

---

#### <a name="translate-visible-object-names"></a>Translate Visible Object Names (Severity 1)

When the model contains one or more cultures, all visible objects should have a name translation provided in that culture.

&nbsp;

---

#### <a name="use-msoledbsql-provider"></a>Use MSOLEDBSQL provider (Severity 1)

Data source providers SQLOLEDB and SQLNCLI have been deprecated. Use MSOLEDBSQL instead. Set the "Provider" property to "System.Data.OleDb" and ensure that the connection string specified MSOLEDBSQL as "Provider". More information: https://docs.microsoft.com/en-us/sql/connect/oledb/oledb-driver-for-sql-server?view=sql-server-ver15

&nbsp;

---

#### <a name="dax-expressions-inactive-relationships-that-are-never-activated"></a>[DAX Expressions] Inactive relationships that are never activated (Severity 1)

Inactive relationships are activated using the USERELATIONSHIP function. If an inactive relationship is not referenced in any measure via this function, the relationship will not be used. It should be determined whether the relationship is not necessary or to activate the relationship via this method. Reference: https://docs.microsoft.com/power-bi/guidance/relationships-active-inactive Reference: https://dax.guide/userelationship/

&nbsp;

---

#### <a name="dax-expressions-use-the-treatas-function-instead-of-intersect-for-virtual-relationships"></a>[DAX Expressions] Use the TREATAS function instead of INTERSECT for virtual relationships (Severity 1)

The TREATAS function is more efficient and provides better performance than the INTERSECT function when used in virutal relationships. Reference: https://www.sqlbi.com/articles/propagate-filters-using-treatas-in-dax/

&nbsp;

---

#### <a name="error-prevention-avoid-structured-data-sources-with-provider-partitions"></a>[Error Prevention] Avoid structured data sources with provider partitions (Severity 1)

Power BI does not support provider (a.k.a. 'legacy') partitions which reference structured data sources. Partitions which reference structured data sources must use the M-language. Otherwise, 'provider' partitions must reference a 'provider' data source. This can be resolved by converting the structured data source into a provider data source (see 2nd reference link below). Reference: https://docs.microsoft.com/power-bi/admin/service-premium-connect-tools#data-source-declaration Reference: https://www.elegantbi.com/post/convertdatasources

&nbsp;

---

#### <a name="formatting-add-data-category-for-columns"></a>[Formatting] Add data category for columns (Severity 1)

Add Data Category property for appropriate columns. Reference: https://docs.microsoft.com/power-bi/transform-model/desktop-data-categorization

&nbsp;

---

#### <a name="formatting-format-flag-columns-as-yesno-value-strings"></a>[Formatting] Format flag columns as Yes/No value strings (Severity 1)

Flags must be properly formatted as Yes/No as this is easier to read than using 0/1 integer values.

&nbsp;

---

#### <a name="formatting-hide-fact-table-columns"></a>[Formatting] Hide fact table columns (Severity 1)

It is a best practice to hide fact table columns that are used for aggregation in measures.

&nbsp;

---

#### <a name="formatting-percentages-should-be-formatted-with-thousands-separators-and-1-decimal"></a>[Formatting] Percentages should be formatted with thousands separators and 1 decimal (Severity 1)

[Formatting] Percentages should be formatted with thousands separators and 1 decimal

&nbsp;

---

#### <a name="formatting-relationship-columns-should-be-of-integer-data-type"></a>[Formatting] Relationship columns should be of integer data type (Severity 1)

It is a best practice for relationship columns to be of integer data type. This applies not only to data warehousing but data modeling as well.

&nbsp;

---

#### <a name="formatting-whole-numbers-should-be-formatted-with-thousands-separators-and-no-decimals"></a>[Formatting] Whole numbers should be formatted with thousands separators and no decimals (Severity 1)

[Formatting] Whole numbers should be formatted with thousands separators and no decimals

&nbsp;

---

#### <a name="maintenance-ensure-tables-have-relationships"></a>[Maintenance] Ensure tables have relationships (Severity 1)

This rule highlights tables which are not connected to any other table in the model with a relationship.

&nbsp;

---

#### <a name="maintenance-perspectives-with-no-objects"></a>[Maintenance] Perspectives with no objects (Severity 1)

Perspectives that contain no objects (tables) are most likely not necessary. In this rule, it is only necessary to check tables as adding a column/measure/hierarchy to a perspective also adds the table to the perspective. Additionally, tables in general covers calculated tables and calculation groups as well.

&nbsp;

---

#### <a name="maintenance-remove-data-sources-not-referenced-by-any-partitions"></a>[Maintenance] Remove data sources not referenced by any partitions (Severity 1)

Data sources which are not referenced by any partitions may be removed.

&nbsp;

---

#### <a name="maintenance-remove-roles-with-no-members"></a>[Maintenance] Remove roles with no members (Severity 1)

May remove roles with no members.

&nbsp;

---

#### <a name="maintenance-remove-unnecessary-columns"></a>[Maintenance] Remove unnecessary columns (Severity 1)

Hidden columns that are not referenced by any DAX expressions, relationships, hierarchy levels or Sort By-properties should be removed.

&nbsp;

---

#### <a name="maintenance-remove-unnecessary-measures"></a>[Maintenance] Remove unnecessary measures (Severity 1)

Hidden measures that are not referenced by any DAX expressions should be removed for maintainability

&nbsp;

---

#### <a name="maintenance-visible-objects-with-no-description"></a>[Maintenance] Visible objects with no description (Severity 1)

Add descriptions to objects. These descriptions are shown on hover within the Field List in Power BI Desktop. Additionally, you can leverage these descriptions to create an automated data dictionary (see link below). Reference: https://www.elegantbi.com/post/datadictionary

&nbsp;

---

#### <a name="performance-check-if-dynamic-row-level-security-rls-is-necessary"></a>[Performance] Check if dynamic row level security (RLS) is necessary (Severity 1)

Usage of dynamic row level security (RLS) can add memory and performance overhead. Please research the pros/cons of using it. Reference: https://docs.microsoft.com/power-bi/admin/service-admin-rls

&nbsp;

---

#### <a name="performance-consider-using-aggregations-if-using-direct-query-in-power-bi"></a>[Performance] Consider using aggregations if using Direct Query in Power BI (Severity 1)

If using Direct Query in Power BI Premium, you may want to consider using aggregations in order to boost performance. Reference: https://docs.microsoft.com/power-bi/transform-model/desktop-aggregations

&nbsp;

---

#### <a name="performance-datecalendar-tables-should-be-marked-as-a-date-table"></a>[Performance] Date/calendar tables should be marked as a date table (Severity 1)

This rule looks for tables that contain the words 'date' or 'calendar' as they should likely be marked as a date table. Reference: https://docs.microsoft.com/power-bi/transform-model/desktop-date-tables

&nbsp;

---

#### <a name="performance-limit-row-level-security-rls-logic"></a>[Performance] Limit row level security (RLS) logic (Severity 1)

Try to simplify the DAX used for row level security. Usage of the functions within this rule can likely be offloaded to the upstream systems (data warehouse).

&nbsp;

---

#### <a name="performance-measures-using-time-intelligence-and-model-is-using-direct-query"></a>[Performance] Measures using time intelligence and model is using Direct Query (Severity 1)

At present, time intelligence functions are known to not perform as well when using Direct Query. If you are having performance issues, you may want to try alternative solutions such as adding columns in the fact table that show previous year or previous month data.

&nbsp;

---

#### <a name="performance-reduce-usage-of-calculated-columns-that-use-the-related-function"></a>[Performance] Reduce usage of calculated columns that use the RELATED function (Severity 1)

Calculated columns do not compress as well as data columns and may cause longer processing times. As such, calculated columns should be avoided if possible. One scenario where they may be easier to avoid is if they use the RELATED function. Reference: https://www.sqlbi.com/articles/storage-differences-between-calculated-columns-and-calculated-tables/

&nbsp;

---

#### <a name="performance-set-isavailableinmdx-to-false-on-non-attribute-columns"></a>[Performance] Set IsAvailableInMdx to false on non-attribute columns (Severity 1)

To speed up processing time and conserve memory after processing, attribute hierarchies should not be built for columns that are never used for slicing by MDX clients. In other words, all hidden columns that are not used as a Sort By Column or referenced in user hierarchies should have their IsAvailableInMdx property set to false. Reference: https://blog.crossjoin.co.uk/2018/07/02/isavailableinmdx-ssas-tabular/


</details>

