import requests
from datetime import *
API="cb6b65b6dc8c47cb9bf124135230111"
city=input("Enter city name in the format (city,name)\nAns:")
def weather_forcast(city,Api):
    baseurl="http://api.weatherapi.com/v1/current.json"
    p={'key':Api,'q':city}
    fetch_data=requests.get(baseurl,params=p)
    if (fetch_data.status_code ==200):
        data=fetch_data.json()
        temp_c=data["current"]["temp_c"]
        temp_f=data["current"]["temp_f"]
        time=datetime.now().time().strftime("%H:%M")
        loaction=data["location"]["name"]+","+data["location"]["country"]
        print(f"\nThe weather for the day is..................\nLocation:{loaction}\nTemperature:{temp_c}°C || {temp_f}°F\nDate:{datetime.now().date()} {time}")
weather_forcast(city,API)