import requests
import platform
import os
from datetime import *
from tkinter import *
from tkinter import messagebox

if (os.name=="nt"):
    import py_setenv as pyset 
    if ("API_Weatherapi.com" in os.environ):
        API=os.getenv("API_weatherapi.com") #to retrieve the key from the operating system
    else:
        API=input("Enter your API key: ")
        pyset.set_variable("API_Weatherapi.com",API,os.getenv("USERNAME"))   # to set environment variable
else:
    API=input("Enter your API key: ")

def weather_forcast(city,Api):
    baseurl="http://api.weatherapi.com/v1/current.json"
    p={'key':Api,'q':city,'aqi':"yes"}
    fetch_data=requests.get(baseurl,params=p)
    if (fetch_data.status_code ==200):
        data=fetch_data.json()
        temp_c=data["current"]["temp_c"]
        temp_f=data["current"]["temp_f"]
        time=datetime.now().time().strftime("%H:%M")
        location=data["location"]["name"]+","+data["location"]["country"]
        return f"\nThe weather for the day is..................\n->Location:{location}\n->Temperature:{temp_c}°C || {temp_f}°F\n->Date:{datetime.now().date()} {time}\n\n"
    else:
        return "\n->Unable to fetch data\n->Might be a issue with your city name or the API key.\n->Please check"

def mainmenu():
    global API
    root = Tk()
    root.title("Weather App")

    def get_weather():
        city = city_entry.get()
        if city:
            result = weather_forcast(city, API)
            result_label.config(text=result)
        else:
            messagebox.showerror("Error", "Please enter a city")

    Label(root, text="Enter city name in the format (city,country)").pack()
    city_entry = Entry(root)
    city_entry.pack()

    Button(root, text="Get Weather", command=get_weather).pack()

    result_label = Label(root, text="")
    result_label.pack()

    root.mainloop()

mainmenu()
