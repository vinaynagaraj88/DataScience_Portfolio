## Stroke Prediction

### Project Summary

![Stroke Prediction](https://user-images.githubusercontent.com/54513557/128503763-1e527568-af4c-4887-8689-f3cca8a01bad.jpeg)

According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. A stroke happens when blood stops flowing to any part of your brain, damaging brain cells.  
Recent advances in stroke care have reduced case fatality and improved functional outcomes after stroke. Detecting Stroke at an early stage and providing medication for that is very crucial to a patient's health condition. If stroke can be predicted at an early stage there is 4% lower risk of in-hospital death, 4% better odds of walking independently after leaving the hospital and also 3% better odds of being sent home instead of to an institution.  
As part as of this project, we are trying to identify the factors that lead to stroke in patients and build a classifier model that would help hospitals in predicting if a patient is likely to suffer from stroke or not.
 

### Dataset details

1. **Input Data** - [Kaggle](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)
2. The dataset contains 5,110 records with 11 attributes and one target variable.
3. bmi” column had 201 missing rows which was filled using the Forward Fill technique.
4. ‘Age’ is a majorly contributing factor to Customer Churn. 

### Technology Used

1. Python 3
2. Jupyter Notebook

### Exploratory Data Analysis

1. No-Stroke '0' vs Stroke '1'

![image](https://user-images.githubusercontent.com/54513557/128504471-595d15ac-f41e-47ed-bd68-4b41ba91d5c3.png)

2. Stroke Distribution by Age

![image](https://user-images.githubusercontent.com/54513557/128504524-597a4e58-42e8-43d0-9af5-ee7151032c7f.png)

3. Effects of Smoking on Stroke

![image](https://user-images.githubusercontent.com/54513557/128504570-4770f9a3-00a7-4712-bfec-56455c145e9c.png)

4. Effect of Heart disease on Stroke

![image](https://user-images.githubusercontent.com/54513557/128504616-5eba4ef9-4477-429f-98dc-b662e1c56110.png)

5. Effect of work type on Stroke

![image](https://user-images.githubusercontent.com/54513557/128504695-261391cc-7037-4760-b797-2024589d5002.png)

6. Effect of marriage on Stroke

![image](https://user-images.githubusercontent.com/54513557/128504743-92753735-fcf5-4475-ae1a-fdc377546990.png)

7. Effect of Gender on Stroke

![image](https://user-images.githubusercontent.com/54513557/128504797-85649be1-c1cc-42d0-a880-fb043c3c3fb9.png)

8. Effect of Residence Type on Stroke

![image](https://user-images.githubusercontent.com/54513557/128504867-279e0bbc-b7f0-494a-a264-1eedf46bba9f.png)


### Modeling

- Target variable – “Stroke” which determines if a patient suffered from Stroke or not.  
- Our dataset is highly imbalanced as most of the records contained data of patients who had no-stroke. 
- We are implementing oversampling technique called SMOTE to handle our imbalanced dataset.
- SelectKBest technique used to identify most relevant features and below is a plot on their importance.

![image](https://user-images.githubusercontent.com/54513557/128504940-479e83d3-dc5c-4e3a-9d60-d991cc1a4de8.png)


1) Random Forest Model Classification - Results:

![image](https://user-images.githubusercontent.com/54513557/128505129-a95ceee9-2b9a-4404-b046-521afc5e01e8.png)

2) kNN - Results:

![image](https://user-images.githubusercontent.com/54513557/128505201-0b0121e0-1600-48c0-b91b-b9d909629214.png)

3) Decision Tree Classification - Results:

![image](https://user-images.githubusercontent.com/54513557/128505250-77ea6951-e669-4189-990e-0c195007221e.png)


### Conclusion

1) Age is an important factor in Stroke patients.
2) Smoking is injurious to health and can increase the chances of Stroke.
3) SMOTE Technique can used to overcome imbalanced data. 
4) Random Forest Model better suited.

[Link to code in GitHub](https://github.com/vinaynagaraj88/DataScience_Portfolio/tree/main/P3%20-%20Stroke%20Prediction)
