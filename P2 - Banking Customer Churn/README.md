## Banking Customer Churn

### Project Summary

![image](https://user-images.githubusercontent.com/54513557/126904905-6584eb5b-8e5a-4e1c-ba12-9a80bc707113.png)

Customers are the most important part of your business regardless of the industry. There would be no sales without customers and they are a critical factor when developing your marketing messaging and strategy. Customer Churn is the rate at which customers stop doing business with an entity. This is one of the most acknowledged problems in the banking sector and Banks are constantly looking at data/suggestions which could help them improve their customer service and retain their existing customers and also bring in new customers.  
Through this project, I intend to focus on the behavior of bank customers who are more likely to leave the bank. I want to find out some striking behaviors of customers through Exploratory Data Analysis and later on use some of the predictive analytics techniques to determine the customers who are most likely to churn.  

### Dataset details

1. **Input Data** - [Kaggle](https://www.kaggle.com/shrutimechlearn/churn-modelling)
2. The dataset contains 10,000 records with 13 attributes and one target variable.
3. Demographically the information is about customers from Spain, France, and Germany.
4. 55% of customers are Male, and 45% are Female, with an average age of 38.9 years. 
5. ‘Age’ is a majorly contributing factor to Customer Churn. 

### Technology Used

1. Python 3
2. Jupyter Notebook

### Exploratory Data Analysis

1. Exited '0' (Active Customer) vs '1' (Exited Customer)

![image](https://user-images.githubusercontent.com/54513557/126905039-dd6ecf09-5be1-4168-81ed-6f049d3e1891.png)

2. Gender wise Customer Churn - Female Customers tend to exit more

![image](https://user-images.githubusercontent.com/54513557/126905068-f47403c1-5a16-4535-8186-c543b8687f26.png)

3. Geography wise Customer Churn - Germany Customers tend to exit more

![image](https://user-images.githubusercontent.com/54513557/126905081-4059c860-3197-436d-b9f7-58255f2c631a.png)

4. Customer Churn based on Activity - Inactive customers tend to exit the bank more.

![image](https://user-images.githubusercontent.com/54513557/126905109-895d6a76-40a3-4aa0-aece-379bdad61869.png)

5. Credit Card Customer Churn - Customers with no credit card tend to exit the bank more.

![image](https://user-images.githubusercontent.com/54513557/126905147-e876afe9-2bc6-468c-a400-dfdf955e0606.png)

6. Product wise Customer Churn - The ratio of exited cases with 3 or more products definitely higher than under 2 products.

![image](https://user-images.githubusercontent.com/54513557/126905167-e9109190-4d53-4773-90a1-2af8e840b687.png)

7. Age wise Customer Churn - People with Ages between 30 to 40 has the highest probability of staying and Ages between 45 to 55 has the highest probability of leaving.

![image](https://user-images.githubusercontent.com/54513557/126905196-09a09d29-b064-4daf-82c8-9ad5d5d2ecb4.png)


### Modeling

- Target variable – “Exited” which determines if a customer exited the bank or not. 
- SelectKBest technique used to identify most relevant features and below is a plot on their importance.

![image](https://user-images.githubusercontent.com/54513557/126905251-665eac24-fba9-4ea3-bf2f-ebc04aef81a7.png)

- Below is the aggregate measure of performance across the popular classification models.

![image](https://user-images.githubusercontent.com/54513557/126905278-496a744b-d9f1-4549-a2a8-23d229290ecd.png)

1) Random Forest Model Classification

Below is the Confusion Matrix after HyperParameter Tuning:

![image](https://user-images.githubusercontent.com/54513557/126905286-9fb7fce2-0a94-45d7-9561-ead73c0e4c6d.png)

2) SVC Classification

Below is the Confusion Matrix after HyperParameter Tuning:

![image](https://user-images.githubusercontent.com/54513557/126905301-03927b99-3994-4566-9fb8-4053eda94673.png)

3) GaussianNB Classification

Below is the Confusion Matrix after HyperParameter Tuning:

![image](https://user-images.githubusercontent.com/54513557/126905322-890dda54-e5bb-48ac-b067-3fef1b0c0e30.png)


### Conclusion

1) Banks need to see how they can engage the older generation more with their bank.
2) It is important to make sure banks keep the customers actively engaged with the bank.
3) Bank need to improve their service to Female customers and also customers in Germany.
4) Provide interesting perks to customers who open a credit card with their bank.
5) Random Forest Classification model is best suited for this prediction.

[Link to code in GitHub](https://github.com/vinaynagaraj88/DataScience_Portfolio/tree/main/P2%20-%20Banking%20Customer%20Churn)
