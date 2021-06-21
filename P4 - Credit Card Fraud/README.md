## Credit Card Fraud Prediction

### Project Summary
  
![image](https://user-images.githubusercontent.com/54513557/122613779-09c59380-d04b-11eb-9590-af8fb5073170.png)
  

Credit card fraud was ranked number one type of identity theft fraud. Each year financial institutions lose a significant amount of money as a result of credit card fraud. Due to increase in fraud rates, researchers have started using different machine learning methods to detect and analyze frauds in online transactions. In year 2018, a total of $24.26 Billion was lost due to payment card fraud across the globe and United States being the most fraud prone country.  
This project intends to create a model for credit card fraud detection using past credit card transactions with the knowledge of the ones that turned out to be a fraud. 


### Dataset Details

1) **Input Data** - [Kaggle Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
2) Dataset contains 2 days of Credit card transactions from Sept ’13 by European cardholders.
3) Out of 284,807 transactions, 492 are fraud.
4) Most of the fraudulent transactions are of small amounts. 


### Exploratory Data Analysis

1) Fraud vs Non-Fraud

![image](https://user-images.githubusercontent.com/54513557/122691359-d7579a00-d1f4-11eb-8643-80fd51bbadc5.png)

2) Distribution of fraudulent transactions amounts

![image](https://user-images.githubusercontent.com/54513557/122691392-0bcb5600-d1f5-11eb-95e0-8b466a0d7a06.png)

3) Distribution of transaction time

![image](https://user-images.githubusercontent.com/54513557/122691414-2271ad00-d1f5-11eb-944e-43aaba797c36.png)

4) Pearson Correlation Heatmap

![image](https://user-images.githubusercontent.com/54513557/122691441-4fbe5b00-d1f5-11eb-9752-7e201db56baa.png)


### Modeling

- Target variable – “Class” which determines if a transaction is fraudulent or not.
- Our dataset is highly imbalanced as most of the transactions are non-fraudulent. 
- We are implementing oversampling technique called SMOTE to handle our imbalanced dataset.
- SelectKBest technique used to identify most relevant features.
- Below is the aggregate measure of performance across the 4 classification models.

![image](https://user-images.githubusercontent.com/54513557/122691509-c3606800-d1f5-11eb-95e4-16c574c64a12.png)

1) Random Forest Model Classification

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/122691543-f4d93380-d1f5-11eb-86f9-dccf23f70967.png)


2) Logistic Regression Model Classification

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/122691557-0a4e5d80-d1f6-11eb-8b67-d4a0bdda0cda.png)


### Conclusion

1) Transaction time does not have any influence on prediction of fraudulent transaction.
2) SMOTE oversampling technique helped overcome the Imbalanced datasets challenge. 
3) Best suited classification model for our dataset would be Random forest model. 
4) 98.528% of the time, Random Forest model will correctly predict if the transaction was fraudulent or not.
5) 98.032% of the time, Logistic Regression model will correctly predict if the transaction was fraudulent or not.


[Link to code in GitHub](https://github.com/vinaynagaraj88/vinaynagaraj88.github.io/tree/main/P4%20-%20Credit%20Card%20Fraud)
