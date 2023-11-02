import requests
API="cb6b65b6dc8c47cb9bf124135230111"
def weather_forcast(city,Api):
    baseurl="http://api.weatherapi.com/v1/current.json"
    p={'key':Api,'q':city}
    fetch_data=requests.get(baseurl,params=p)
    if (fetch_data.status_code ==200):
        data=fetch_data.json()
        temp_c=data["current"]["temp_c"]
        temp_f=data["current"]["temp_f"]
        loaction=data["location"]["name"]+","+data["location"]["country"]
        return {'loc':loaction,'celcious':temp_c,"faren":temp_c}
