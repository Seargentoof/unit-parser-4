# unit-parser-4

This is the fourth version of the Unit Parser program programmed by Dawson Lin, designed to detect Retract-and-Reorder (RAR) errors in the 
Electronic Health Record by making comparisons between clinical units of measure. 

## Language
This project was written in Python 3. 

## How it works
Unit Parser 4's orders_are_equal method compares two orders at a time. It takes them in the string form "Measure Unit", where "Measure" is 
a numerical value and "Unit" is an expression of a unit (e.g. g, gram, grams). 

After parsing the two orders, the unit expressions are looked up in a previously created database (a Microsoft Excel spreadsheet). The 
spreadsheet consists of three columns: one with unit expressions (e.g. g, gram, grams), another with contexts (e.g. mass), and the last 
with values that are relative to a predetermined base unit (for example, g has a value of 1 while mg has a value of 1e-3). 

For each order, the unit context and the value of the order (measure * unit value) are determined. If the contexts AND the values match, 
the orders are determined to be equal. Otherwise, they are not. 

## How to use this program
Use the orders_are_equal method to make comparisons for equality between medical orders. 

The Excel database is meant to be user-friendly and easy to understand, edit, and expand. However, it needs to be as well-standardized as possible. To achieve this, please observe the following conventions:
1. One Context and Value allotted to each Expression.
2. Keep the letter case consistent within an Expression.
3. Refrain from adding unit Expressions that are equal in a case-insensitive context to prevent duplicate rows.
4. Group Expressions with the same Context together. 
5. All Contexts are to be written in lowercase.
6. If a unit Expression has an ambiguous Context, make the Context the singular form of the Expression (e.g. the Context of "unit" or "units" is "unit").
7. Unit Values of 1 denote that the corresponding Expression is a base unit. Maintain relativity to the base unit when assigning Values to
other Expressions. 
8. For metric units, use exponential notation (e.g, 1.00E+06 instead of 1000000) when denoting Values.
9. Try to make decimal number Values as precise as possible, as to minimize floating point error when comparing for equality.
10. Write notes in the dedicated "Notes" column only. 
