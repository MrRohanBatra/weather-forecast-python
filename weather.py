#!/usr/bin/python3
import requests
import os
from datetime import *
import platform
#All modules imported
if (os.name=="nt"):    
    import py_setenv as pyset #importing py_setenv module for permanently saving the environment variable
    if ("API_Weatherapi.com" in os.environ):
        API=os.getenv("API_weatherapi.com") #got API key from system only
    else:
        API=input("Enter your API key: ")
        pyset.set_variable("API_Weatherapi.com",API,os.getenv("USERNAME"))   # to set environment variable
else:
    API=input("Enter your API key: ")
print("autorefresh mode is set to on")
city=input("Enter city name in the format (city,country)\nAns:")
os.system("cls")
if (city.lower()=="delhi"):
    city="delhi,india"
def autorefresh(city,api,t):
    while True:
        if (int((datetime.now().time().strftime("%S")))- int(t) > 5): #timer for 15 seconds
            if (os.name=="nt"):
                os.system("cls")
                print("Refreshed......\n")
                weather_forcast(city,api)
            elif (platform.system().lower() =="linux"):
                os.system("clear")
                print("Refreshed......\n")
                weather_forcast(city,api)
            else:
                os.system("clear")
                print("Refreshed......\n")
                weather_forcast(city,api)
        else:
            continue
def weather_forcast(city,Api,s=0):
    baseurl="http://api.weatherapi.com/v1/current.json"
    p={'key':Api,'q':city,'aqi':"yes"}
    fetch_data=requests.get(baseurl,params=p)
    if (fetch_data.status_code ==200): #if data is fetched successfully
        data=fetch_data.json()
        temp_c=data["current"]["temp_c"] #temperature in celcious
        temp_f=data["current"]["temp_f"] #tempereture in farenhiet
        time=datetime.now().time().strftime("%H:%M") #time using datetime module and formatted string using stftime
        location=data["location"]["name"]+","+data["location"]["country"] 
        print(f"\nThe weather for the day is..................\n->Location:{location}\n->Temperature:{temp_c}°C || {temp_f}°F\n->Date:{datetime.now().date()} {time}\n\n")
    else: #if data is not fetched successfully
        print("\n->Unable to fetch data\n->Might be a issue with your city name or the API key.\n->Please check")
        weather_forcast(input("\nEnter city name in the format (city,country)\nAns:"),Api)
    autorefresh(city,Api,datetime.now().time().strftime("%S"))
weather_forcast(city,API)
