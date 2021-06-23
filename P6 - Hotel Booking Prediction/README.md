## Hotel Booking Prediction

### Project Summary

![image](https://user-images.githubusercontent.com/54513557/123023604-4839b600-d39d-11eb-871f-46ab8e847d42.png)

Due to recent events in the world, the hotel industry has taken a major setback on its business. Hotel room booking and subsequent cancellations are causing Hotel owners the constant headache of losing business.  
This project looks at a dataset comprised of data pertaining to Hotel booking and their attributes. Through this study we will try to look at what factors would be available to the Hotel owners which they could use and predict the outcome of a booking. Utilizing the insights gained by this analysis the Hotel owners could better plan their business and see how they can profit in this tough times. Using the features from each hotel booking, my model will predict whether the hotel booking will be cancelled or not.  

### Dataset details

1) **Input Data** - [Kaggle Dataset](https://www.kaggle.com/jessemostipak/hotel-booking-demand)
2) The data is originally from the article [Hotel Booking Demand Datasets](https://www.sciencedirect.com/science/article/pii/S2352340918315191), written by Nuno Antonio, Ana Almeida, and Luis Nunes for Data in Brief, Volume 22, February 2019.
3) Dataset contains around 119390 records of Hotel Bookings


### Technology Used:

1) Python 3
2) Jupyter Notebook


### Exploratory Data Analysis

1. Hotel distribution based on booking status

![image](https://user-images.githubusercontent.com/54513557/123024090-255bd180-d39e-11eb-9683-070ef03648d6.png)

2. Number of reservations per year

![image](https://user-images.githubusercontent.com/54513557/123024158-39073800-d39e-11eb-92c6-b7a755a728f9.png)

3. Average number of hotel guests per month

![image](https://user-images.githubusercontent.com/54513557/123024191-48868100-d39e-11eb-892c-941a4019abbd.png)

4. Pearson Correlation Heatmap

![image](https://user-images.githubusercontent.com/54513557/123024262-648a2280-d39e-11eb-848e-a6cd8c2e1fd8.png)

5. Spearman Correlaton Heatmap

![image](https://user-images.githubusercontent.com/54513557/123024285-6ce25d80-d39e-11eb-9bc9-9c9ce9c71df0.png)


### Modeling

- Target variable – “is_canceled” which determines if a hotel booking has been canceled or not. 
- Since the values are of PCA transformation, we normalized the data as it could impact the performance of the model.
- SelectKBest technique used to identify most relevant features.
- Below is the aggregate measure of performance across the 4 classification models.

![image](https://user-images.githubusercontent.com/54513557/123024452-af0b9f00-d39e-11eb-87dd-c5dcbb3ec76c.png)

1) Random Forest Classification Model

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/123024664-06aa0a80-d39f-11eb-8fc4-dd1206394124.png)

2) Logistic Regression Classicication Model

Below is the Confusion Matrix:

![image](https://user-images.githubusercontent.com/54513557/123024726-22adac00-d39f-11eb-9be1-3d72dcb62b0b.png)


### Conclusion

* lead_time is one of the most importance feature. This means that the sooner the reservation is made compared to arrival time, the more likely it will be cancelled.
- Comparing the Random Forest model and Logistic Regression model I think Random Forest model is much better with this dataset than Logistic Regression mode.
- In the confusion matrix the random forest predicts the values for both classes more accurately than the logistic regression confusion matrix.
- The LogisticRegression model predicted the 1,594 Not Canceled bookings as Canceled bookings and 5,093 canceled bookings as Not Canceled.
- The RandomForestClassifier model predicted the 1,012 Not Canceled bookings as Canceled bookings and 2,354 canceled bookings as Not Canceled.
- In the precision recall and F1 score the Random forest model scored better on all three metrics for both classes. In the ROC AUC curve the random forest preforms much better.
- Overall, the Random Forest model out preforms the logistic regression model on every point.
