import tkinter as tk
import requests

API_KEY = '1d03c9951c66c5c94eb203daa75daf40'  
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return data

def display_weather(weather_data):
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']

    result_label.config(text=f'Temperature: {temperature}°C\n'
                             f'Humidity: {humidity}%\n'
                             f'Wind Speed: {wind_speed} m/s\n'
                             f'Description: {description}')

def get_weather_button_click():
    city = city_entry.get()
    if city:
        weather_data = get_weather(city)
        display_weather(weather_data)
    else:
        result_label.config(text='Please enter a city name')

# Create the main window
root = tk.Tk()
root.title('Weather Forecast App')

# Create and place widgets
city_label = tk.Label(root, text='Enter city name:')
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text='Get Weather', command=get_weather_button_click)
get_weather_button.pack(pady=5)

result_label = tk.Label(root, text='', justify='left')
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
