## EDA of FIFA-2019

### Project Summary

![image](https://user-images.githubusercontent.com/54513557/123075065-8060e900-d3dd-11eb-9754-7a8a929a8fcd.png)

FIFA football World Cup is one of the most watched sports event in the world with more than half of the world’s population being its viewers. It is the biggest sporting event on the planet. It is an international association football competition contested by the senior men's national teams of the members of the Fédération Internationale de Football Association (FIFA), the sport's global governing body. This event is played every 4 years.  
People around the world are crazy about this event that there would be discussions about who is the best player and each person defending their players, teams. People are awake all night to catch the matches live, then analyze every game, watch highlights, read articles, YouTube videos. It is a religion in some places. The economic crisis of Spain was forgotten, albeit for a few days, when they won the World Cup in 2010. Such is the craze.  


### Dataset Details

1) **Input Data** - [Kaggle Dataset](https://www.kaggle.com/blurredmachine/fifa-2019-world-cup-dataset)
2) Dataset contains 18,206 records of the details of the players who played in the FIFA World Cup and their final value at which they were sold to the club.


### Important Variables

1) **Age**: This column has the age of each player in years
2) **Height**: This column has the height of each player in feet
3) **Weight**: This column has the weight of each player in pounds
4) **Preferred foot**: Player’s preferred foot, Right or Left.
5) **Defending**: This is a new column which is mean of Marking, Standing Tackle and Sliding Tackle. 
6) **Shooting**: This is a new column which is the mean of Finishing, Volleys, Free Kick Accuracy, Shot power, Long shots, Penalties.


### Technology Used:

1) Python 3
2) Jupyter Notebook


### Exploratory Data Analysis

1) Youngest and Oldest Player

![image](https://user-images.githubusercontent.com/54513557/123077517-ba32ef00-d3df-11eb-97f7-cc4ed357836a.png)

2) Lightest and Heaviest Player

![image](https://user-images.githubusercontent.com/54513557/123077589-cae36500-d3df-11eb-94ca-36e8e0b43373.png)

3) Tallest and Shortest Player

![image](https://user-images.githubusercontent.com/54513557/123077628-d6369080-d3df-11eb-8933-75ff38858191.png)

4) Football Positions

![image](https://user-images.githubusercontent.com/54513557/123077667-e0588f00-d3df-11eb-8528-9ad4a7302dfb.png)

5) Preferred Foot of Players

![image](https://user-images.githubusercontent.com/54513557/123077709-ea7a8d80-d3df-11eb-8edf-15999a3dab48.png)

6) Better Defenders

![image](https://user-images.githubusercontent.com/54513557/123077763-f49c8c00-d3df-11eb-805f-ed2e9891e60a.png)

7) Better Shooters

![image](https://user-images.githubusercontent.com/54513557/123077790-fcf4c700-d3df-11eb-8f92-10cefc1ae968.png)


### Conclusion

1) Oldest player is 45 years old and Youngest player is 16 years old
2) Lightest player is 110lbs and Heaviest player is 243 lbs.
3) Tallest player is 6’9 and shortest player is 5’1.
4) There are 2,212 strikers in out list of players
5) We have 4,211 Left foot players and 13,995 Right foot players.
6) From the CDF plot shown above, the shape of the distribution clearly indicates that Left foot players are better in Defending than the Right foot players.
7) From the CDF plot shown above, the shape of the distribution clearly indicates that Left foot players are better in Shooting than the Right foot players.
8) As per our model, a player would be around 28.45 years to master the skill of Defending and Shooting.
