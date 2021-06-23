## Weather Application

### Project Summary

![image](https://user-images.githubusercontent.com/54513557/123019306-ddd14780-d395-11eb-98ff-d7962f49b855.png)

Weather is the day-to-day state of the atmosphere, and its short-term variation in minutes to weeks. People generally think of weather as the combination of temperature, humidity, precipitation, cloudiness, visibility, and wind. Weather application enable users to get instant alerts regarding weather conditions. Weather applications are the simplest method to know about the updates of the upcoming weather.  

This project is a Weather API application program which returns the weather details for the zip code or city name entered by the user. Secure API key is used to invoke the secure http web service call to openweather.  
The application returns some key results such as Maximum temperature, minimum temperature, Humidity, Sunrise & Sunset times. 


### Input Details
1) Data is derived from webservice API depending on input parameters provided by the end user.
2) Python 3
3) Python Packages needed - requests - datetime
4) Registration with open weather API to be able to submit API request.
5) PyCharm


### Approach

1) Create an account with openWeather website to get the API key that can be used for API calls.
2) Create code to accept either zip code or city name from user and then use the open weather API to retrieve the weather data for that city or zip.
3) Parse the JSON API response received from open weather service and print it back to user in an easily readable format.
