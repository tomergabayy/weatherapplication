import requests, json, datetime, pandas as pd

def get_lat_lon(place):
    api = f"https://geocoding-api.open-meteo.com/v1/search?name={place}"
    response=requests.get(api)
    if "results" not in response.json():
        return "error"
    lat = response.json()["results"][0]["latitude"]
    lon = response.json()["results"][0]["longitude"]
    FullPlace = response.json()["results"][0]["name"]+", "+response.json()["results"][0]["country"]
    return (lat,lon,FullPlace)

def get_forecast(lat_lon):
    #error handling
    if(lat_lon=="error"):
        return "error"
    
    api = f"https://api.open-meteo.com/v1/forecast?latitude={lat_lon[0]}&longitude={lat_lon[1]}&hourly=relative_humidity_2m&daily=temperature_2m_max&daily=temperature_2m_min&&current=temperature_2m"
    response = requests.get(api)

    #get the temratures
    days = response.json()["daily"]["time"]
    daytemps = response.json()["daily"]["temperature_2m_max"]
    nighttemps = response.json()["daily"]["temperature_2m_min"]

    #get the humidity
    hum_allweek = response.json()["hourly"]["relative_humidity_2m"]
    hum_avg=[]
    sum=0
    for i in range(0,len(hum_allweek)):
        sum+=hum_allweek[i]
        if i%23 == 0 and i != 0:
            sum+=hum_allweek[i]
            hum_avg.append(round(sum/24))
            sum=0

    forecast = {pd.Timestamp(days[i]).day_name(): (daytemps[i],nighttemps[i],hum_avg[i]) for i in range(len(days))}
    return forecast

def get_current_temp(lat_lon):
    api = f"https://api.open-meteo.com/v1/forecast?latitude={lat_lon[0]}&longitude={lat_lon[1]}&current=temperature_2m&current=relative_humidity_2m"
    response = requests.get(api)
    return (response.json()["current"]["temperature_2m"],response.json()["current"]["relative_humidity_2m"])

def create_new_json(form_data, parameter):
    try:
        # Generate filename based on current date and parameter
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        parameter=parameter.split(",")[0]
        file_name = f"{parameter}-{current_date}.json"
        
        # Full path to the new JSON file
        file_path = "/app/history/" + file_name
        
        # Write form_data to the new JSON file
        with open(file_path, 'w') as json_file:
            json.dump(form_data, json_file)
    except Exception as e:
        print("Error creating new JSON file:", e)



