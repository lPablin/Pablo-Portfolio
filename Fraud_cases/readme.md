# 🛡️💳 Fraud Detection Project

This project drew significant attention from specialists in artificial intelligence in the field(PhD cum laude and university professors), receiving positive reactions and insightful feedback on LinkedIn. The goal was to detect fraudulent transactions within a dataset containing detailed information on each transaction, including:

- Timestamp
-Sender and receiver information
- Transaction amount
- Sender's and receiver's previous and subsequent balances
- Type of transaction
- Target variable indicating whether the transaction was fraudulent

 ## Project Motivation

While using a neural network might be the initial approach for this problem, understanding the underlying theory is essential for achieving reliable results. A neural network is, in essence, a complex collection of linear regressions with activation functions. For this project, we selected logistic regression to achieve a simple, effective model with low overfitting risk—something that can be an issue with decision trees.

## Prediction Methodology

Since the goal was to identify fraudulent transactions, we applied the logistic function to calculate the probability of fraud. This led to a streamlined model that, while basic, provided substantial accuracy without overfitting.

My project focused on studying class balancing to optimize the logistic regression model. Depending on the presence of fraud cases (the minority class) in the training set, specificity and sensitivity metrics varied. The ultimate goal was to maximize fraud detection while avoiding unnecessary transaction holds that could impact financial operations.

## Key Insights from the Project
1. Class Balancing and Weight Adjustment:
Balancing classes and adjusting class weights inversely to their frequency proved most effective. When uniform weights were applied, it was preferable to increase the minority class proportion. Other techniques, such as using k-nearest neighbors to generate artificial fraud cases or excluding significant portions of the majority class, were also explored.

2. Feature Correlation and Importance:
The correlation matrix revealed that time of day (step_day) was the most highly correlated feature. However, fraud detection focused more on the transaction amount and sender's balance, which were highly collinear only in fraud cases. Initial and final balances showed collinearity in non-fraudulent cases alone.
![Texto del enlace](fraud_matrix.jfif)

4. Classifying Fraud Types:
Fraud cases occurred in transfers and cash-out transactions. Limiting the dataset to these types improved model sensitivity from 78% to 94%.

## Results
During nighttime hours, approximately 1% of transactions were fraudulent. In this specific case, where classes were more balanced, sensitivity reached 93% and specificity reached 95%.

The logistic regression model struggled to handle categorical variables normalized with standard scaler, as binary classes' maximum standard deviation value was only 0.5, whereas other variables had higher values. By splitting categories into separate cases, sensitivity increased to 98%, with specificity remaining constant. Decision tree models, however, natively handle categorical and numerical variables and may therefore achieve better values without custom data preparation.

Using label encoding was considered to allow logistic regression to process categorical and numerical data together. However, caution is needed in assigning label values accurately for model effectiveness.

## Comparison with Other Research
In some publications like [this one](https://www.ijert.org/research/an-evaluation-of-machine-learning-methods-to-predict-fraud-in-mobile-money-transactions-IJERTV11IS010191.pdf), authors used the same dataset but obtained fraud detection rates between 64-80% with complex models such as neural networks. They did not explore simpler methods like logistic regression with the logit function. By comparison, our logistic regression model achieved a sensitivity of 93%. This demonstrates the importance of effective data preparation and model selection in achieving optimal results.

## Conclusion
This project highlights how different modeling and data preparation techniques can yield vastly different results, even when using the same dataset and algorithms. Data Science requires an understanding of both the model and the specific context, making it a field rich with potential solutions.


