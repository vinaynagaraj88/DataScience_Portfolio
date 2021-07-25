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

- Target variable – “Attrition” which determines if the Employee quit the company or not. 
- SelectKBest technique used to identify the top 15 most relevant features.
- Below are the features plotted based on their relevence. 

![image](https://user-images.githubusercontent.com/54513557/126905618-c954b2d4-fa93-4d57-a8c2-ca0a03e04d3d.png)

- Below is the aggregate measure of performance across the 4 classification models.

![image](https://user-images.githubusercontent.com/54513557/124594204-26244700-de25-11eb-83f2-b1102b5a5d59.png)

1) Random Forest Model Classification

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/124594286-3c320780-de25-11eb-9226-2a15498afe8a.png)

2) Logistic Regression Model Classification

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/124594322-494ef680-de25-11eb-8082-f9bd11b911c4.png)


### Conclusion

1) As proven by Graph Analysis and SelectKBest, ‘OverTime’ plays a major factor in employee attrition.
2) Using Random Forest Model our model will correctly predict if the employee would leave the company or not 78.3% of the time.
3) Logistic Regression Model our model will correctly predict if the employee would leave the company or not 75% of the time.
4) Random forest model has fewer false positives than logistic regression making it a better model.
5) Ingesting more data to our machine learning model will help us get better results from what we have achieved here in our research.


[Link to code in GitHub](https://github.com/vinaynagaraj88/DataScience_Portfolio/tree/main/P1%20-%20Employee%20Attrition)
