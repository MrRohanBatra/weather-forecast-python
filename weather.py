import requests
import os
import py_setenv as pyset
from datetime import * 
if "API_Weatherapi.com" in os.environ:
    API=os.getenv("API_weatherapi.com")
else:
    API=input("Enter your API key: ")
    pyset.set_variable("API_Weatherapi.com",API,os.getenv("USERNAME"))   # to set environment variable
city=input("Enter city name in the format (city,name)\nAns:")
def weather_forcast(city,Api):
    baseurl="http://api.weatherapi.com/v1/current.json"
    p={'key':Api,'q':city,'aqi':"yes"}
    fetch_data=requests.get(baseurl,params=p)
    if (fetch_data.status_code ==200):
        data=fetch_data.json()
        temp_c=data["current"]["temp_c"]
        temp_f=data["current"]["temp_f"]
        time=datetime.now().time().strftime("%H:%M")
        aqi=round(float(str(data["current"]["air_quality"]["co"])[1:]))
        location=data["location"]["name"]+","+data["location"]["country"]
        if (aqi in range(0,50)):
            aqi_condition="Good"
        elif(aqi in range(50,100)):
            aqi_condition="Satisfactory"
        elif(aqi in range(100,200)):
            aqi_condition="Moderately Polluted"
        elif(aqi in range(200,300)):
            aqi_condition="Poor"
        elif(aqi in range(300,400)):
            aqi_condition="Very Poor"
        else:
            aqi_condition="Serve"
        print(f"\nThe weather for the day is..................\n->Location:{location}\n->Temperature:{temp_c}°C || {temp_f}°F\n->AQI:{aqi} {aqi_condition}\n->Date:{datetime.now().date()} {time}\n\n")
    else:
        print("\n->Unable to fetch data\n->Might be a issue with your city name or the API key.\n->Please check")
        weather_forcast(input("\nEnter city name in the format (city,name)\nAns:"),Api)
        weather_forcast(city,API)
