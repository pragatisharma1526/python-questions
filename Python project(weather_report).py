import requests

API_key = '952072f37336c945cee7f7890f89ace3'
city_name = input("Enter city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
print(weather_data)

if weather_data.json()['cod']=='404':
    print("Enter correct city name")

else:
    weather=weather_data.json()['weather'][0]['main']
    print(weather)
    temp=weather_data.json()['main']['temp']
    print(temp)
    humidity=weather_data.json()['main']['humidity']
    print(humidity)