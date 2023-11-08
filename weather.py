import requests
import os
import py_setenv as pyset

from datetime import *
if (os.name=="nt"):
    if ("API_Weatherapi.com" in os.environ):
        API=os.getenv("API_weatherapi.com")
    else:
        API=input("Enter your API key: ")
        pyset.set_variable("API_Weatherapi.com",API,os.getenv("USERNAME"))   # to set environment variable
else:
    API=input("Enter your API key: ")
l_city=[
    ("Mumbai", "India"),
    ("Delhi", "India"),
    ("Kolkata", "India"),
    ("Chennai", "India"),
    ("Bangalore", "India"),
    ("Hyderabad", "India"),
    ("Ahmedabad", "India"),
    ("Pune", "India"),
]      
def autorefresh(city,api,t):
    while True:
        if (int((datetime.now().time().strftime("%S")))- int(t) > 30):
            if (os.name=="nt"):
                os.system("cls")
                print("Refreshed......\n")
                weather_forcast(city,api)
            elif (os.name =="linux"):
                print("Refreshed......\n")
                weather_forcast(city,api)
            else:
                print("Refreshed......\n")
                weather_forcast(city,api)
        else:
            continue
def weather_forcast(city,Api,s=0):
    baseurl="http://api.weatherapi.com/v1/current.json"
    p={'key':Api,'q':city,'aqi':"yes"}
    fetch_data=requests.get(baseurl,params=p)
    if (fetch_data.status_code ==200):
        data=fetch_data.json()
        temp_c=data["current"]["temp_c"]
        temp_f=data["current"]["temp_f"]
        time=datetime.now().time().strftime("%H:%M")
        location=data["location"]["name"]+","+data["location"]["country"]
        print(f"\nThe weather for the day is..................\n->Location:{location}\n->Temperature:{temp_c}°C || {temp_f}°F\n->Date:{datetime.now().date()} {time}\n\n")
    else:
        print("\n->Unable to fetch data\n->Might be a issue with your city name or the API key.\n->Please check")
        weather_forcast(input("\nEnter city name in the format (city,country)\nAns:"),Api)
    if(s==0):
        autorefresh(city,Api,datetime.now().time().strftime("%S"))
def mainmenu():
    global API
    print("Welcome to the weather app.........................          ")
    print("\nTo display the weather")
    while True:
        print("Choose any one from the following options\n1->city of your choice\n2->Cities from favourate list\n3->exit")
        i=int(input("Enter your Choice"))
        if(i==1):
            print("autorefresh mode is set to on")
            city=input("Enter city name in the format (city,country)\nAns:")
            os.system("cls")
            if (city.lower()=="delhi"):
                city="delhi,india"
            weather_forcast(city,API,s=0)
        elif(i==2):
            global l_city
            l=l_city
            for i in l:
                city=i[0]+","+i[1]
                print(city)
                weather_forcast(city,API,s=1)
                print("\n")
        elif(i==3):
            break
    exit()   
mainmenu()