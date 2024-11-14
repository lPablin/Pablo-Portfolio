# 📊 Investment Asset Management System for Banco Mangander

This project involves designing an Entity-Relationship Diagram (ERD) for Banco Mangander, an investment firm managing diverse financial assets across multiple clients. The system must store detailed information for each client and their holdings, which include stocks, bonds, and bank deposits. Each asset type has unique attributes and must support transactions, market valuation history, and risk categorization (e.g., high-risk, short-term). The ERD will capture these requirements, including entity relationships, cardinalities, and inheritance for asset subtypes where appropriate.

![imagen](Northwind_E-R_Diagram.PNG)

In the SQL project, it was decided to create the following tables and apply views for the rest of the data. This way, permanent data such as transaction records are stored in a table, while a view is used to dynamically update and reflect the variable values derived from these transactions.
