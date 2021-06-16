# course: DSC510
# assignment: 12.1
# date: 05/26/20
# name: Vinay Nagaraj
# description: Write a weather program which returns the weather details for the zip code or city name entered by the user.

import requests
import datetime

# function to call OpenWeathermap to get weather forecast based on city name
def get_weather_city(user_inp):
    apiKey = '3a40cabc8005cf7e8a1aafb0a239acbd'
    webSite = 'http://api.openweathermap.org/data/2.5/weather?lat=0&lon=1&units=imperial&appid='
    get_weather = requests.get(webSite + apiKey)
    try:
        get_weather.raise_for_status()
        if get_weather.status_code == 200:              # 200 is a successful return code
            passValue = 'http://api.openweathermap.org/data/2.5/weather?' + "appid=" + apiKey + "&q=" + user_inp
            try:
                response = requests.get(passValue)
                response.raise_for_status()
                disp_Weather = response.json()
                pretty_print(disp_Weather, user_inp)
            except requests.exceptions.HTTPError:
                print('Invalid City entered, please try again!')
        else:
            print('Connection was not successful, please try again!')
    except requests.exceptions.HTTPError as e:
        print('Connection was not successful, please try again!')
        return "Error: " + str(e)

# function to call OpenWeathermap to get weather forecast based on Zip code
def get_weather_zip(user_inp):
    apiKey = '3a40cabc8005cf7e8a1aafb0a239acbd'
    webSite = 'http://api.openweathermap.org/data/2.5/weather?lat=0&lon=1&units=imperial&appid='
    get_weather = requests.get(webSite + apiKey)
    try:
        get_weather.raise_for_status()
        if get_weather.status_code == 200:              # 200 is a successful return code
            passValue = 'http://api.openweathermap.org/data/2.5/weather?' + "appid=" + apiKey + "&zip=" + user_inp
            try:
                response = requests.get(passValue)
                response.raise_for_status()
                disp_Weather = response.json()
                pretty_print(disp_Weather, user_inp)
            except requests.exceptions.HTTPError:
                print('Invalid Zip code entered, please try again!')
        else:
            print('Connection was not successful, please try again!')
    except requests.exceptions.HTTPError as e:
        print('Connection was not successful, please try again!')
        return "Error: " + str(e)

# function to display the weather information in readable format
def pretty_print(disp_Weather, user_inp):
    main_weather = disp_Weather['main']
    city_name = disp_Weather['name']
    cur_weather = disp_Weather['weather']
    cur_temp = main_weather['temp']
    min_temp = main_weather['temp_min']
    max_temp = main_weather['temp_max']
    humidity = main_weather['humidity']
    print('\nCurrent Weather conditions for', user_inp)
    if user_inp.isdigit():
        print('City Name    :', city_name)
# Display Temperature in Fahrenheit
    temp_fahn = int(float((9 * (cur_temp - 273.15))/5 + 32))
    max_fahn = int(float((9 * (max_temp - 273.15))/5 + 32))
    min_fahn = int(float((9 * (min_temp - 273.15))/5 + 32))
    print('Current Temp :', str(temp_fahn) +'\u00b0F')
    print('High Temp    :', str(max_fahn) + '\u00b0F')
    print('Low Temp     :', str(min_fahn) + '\u00b0F')
    sun_time = disp_Weather['sys']
    sun_rise = sun_time['sunrise']
    sun_set = sun_time['sunset']
# Display time in standard format
    disp_sunrise = datetime.datetime.fromtimestamp(int(sun_rise)).strftime('%I:%M %p')
    disp_sunset = datetime.datetime.fromtimestamp(int(sun_set)).strftime('%I:%M %p')
    print('Sunrise      :', disp_sunrise)
    print('Sunset       :', disp_sunset)
    for item in cur_weather:
        print('Cloud Cover  :', (item['description']))
    winds = disp_Weather['wind']
    wind_speed = winds['speed']
# Convert wind speed from meters per second to miles per hour and display
    conv_windS = wind_speed * 2.237
    round_windS = round(conv_windS, 1)
    print('Wind Speed   :', str(round_windS), 'mph')
    print('Humidity     :', str(humidity) + '%' + '\n')

# main section to receive input from user and make the necessary call
def main():
    print('Hello, Welcome to Bellevue University Weather App')
    while True:
        print('Would you like to lookup weather data by US city or zip code?')
        user_choice = input('Enter 1 for US City, 2 for US Zip Code or 3 to Quit: ')
        if user_choice == '1':
            user_inp = input('Please enter the US city name: ')
            get_weather_city(user_inp)
        elif user_choice == '2':
            user_inp = input('Please enter the US Zip Code: ')
            get_weather_zip(user_inp)
        elif user_choice == '3':
            print('Thank you for using the Bellevue Weather App')
            break
        else:
            print('Invalid value entered, please try again')

if __name__ == "__main__":
    main()
