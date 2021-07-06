## Employee Attrition Prediction

### Project Summary

![image](https://user-images.githubusercontent.com/54513557/123791640-50b25500-d8a5-11eb-890f-6ce8b632cfaf.png)

Attrition can make a big dent in your organization’s bottom line as well as its culture. For an organization to perform successfully, it is important that the employer and the employee have a good relationship and understanding. When an employee decides to quit, there will be a lot of challenges for the employer. It will impact their productivity, revenue, experience and also time invested in training the employee.  
This project intends to identify the factors that lead to employee attrition and build a classifier model that would help an organization in predicting the employees that can leave the organization.  

### Dataset details

1. **Input Data** - [Kaggle](https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset)
2. The dataset used is a fictional data set created by IBM data scientists and available on Kaggle.
3. Out of 1,470 records, 237 are data related to Employees who left.
4. Working ‘OverTime’ is a majorly contributing factor to Employee Attrition.

### Technology Used

1. Python 3
2. Jupyter Notebook

### Exploratory Data Analysis

1. Attrition 'Yes' vs 'No'

![image](https://user-images.githubusercontent.com/54513557/123792139-e8b03e80-d8a5-11eb-9a1d-22b66e608656.png)

2. Working Over Time

![image](https://user-images.githubusercontent.com/54513557/123792448-3b89f600-d8a6-11eb-98b5-9af846e1cc25.png)

Employees working overtime are more likely to leave.  


3. Distance from Home

![image](https://user-images.githubusercontent.com/54513557/123792201-fc5ba500-d8a5-11eb-871b-d751d3e43ccf.png)

Employees traveling more than 10 miles are more likely to leave.  


4. Monthly Income

![image](https://user-images.githubusercontent.com/54513557/123792326-1c8b6400-d8a6-11eb-983d-524535fb1a1d.png)

Employees with monthly income of less than 5,000 are more likely to leave.  



### Modeling

- Target variable – “Class” which determines if a transaction is fraudulent or not.
- Our dataset is highly imbalanced as most of the transactions are non-fraudulent. 
- We are implementing oversampling technique called SMOTE to handle our imbalanced dataset.
- SelectKBest technique used to identify most relevant features.
- Top 15 features selected using SelectKBest technique.

![image](https://user-images.githubusercontent.com/54513557/124594459-6d123c80-de25-11eb-9bda-a1288bed6746.png)

- Below is the aggregate measure of performance across the 4 classification models.

![image](https://user-images.githubusercontent.com/54513557/124594204-26244700-de25-11eb-83f2-b1102b5a5d59.png)

1) Random Forest Model Classification

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/124594286-3c320780-de25-11eb-9226-2a15498afe8a.png)

2) Logistic Regression Model Classification

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/124594322-494ef680-de25-11eb-8082-f9bd11b911c4.png)


### Conclusion

1) Transaction time does not have any influence on prediction of fraudulent transaction.
2) SMOTE oversampling technique helped overcome the Imbalanced datasets challenge. 
3) Best suited classification model for our dataset would be Random forest model. 
4) 98.528% of the time, Random Forest model will correctly predict if the transaction was fraudulent or not.
5) 98.032% of the time, Logistic Regression model will correctly predict if the transaction was fraudulent or not.


[Link to code in GitHub](https://github.com/vinaynagaraj88/DataScience_Portfolio/tree/main/P1%20-%20Employee%20Attrition)
