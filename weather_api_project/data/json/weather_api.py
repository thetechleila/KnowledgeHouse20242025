import requests
import json
import pandas as pd

#Get the page through get method then Scrape the open-meteo.com/en/docs site
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York"

page = requests.get(URL)

#Convert page variable into json
api_in_json = page.json()

# Nested JSON data formatted as a dictionary 
hourly_data = api_in_json ["hourly"] 
json_data = {
    "time": hourly_data["time"],
    "temperature_2m": hourly_data["temperature_2m"],
    "relative_humidity_2m": hourly_data["relative_humidity_2m"],
    "precipitation": hourly_data["precipitation"],
    "surface_pressure": hourly_data["surface_pressure"]   
}

# Convert dictionary to JSON string
json_data = json.dumps(json_data)

# Convert JSON string to Pandas DataFrame
df = pd.read_json(json_data, orient="columns")

#Covert DataFrame into a CSV file called weather_data.csv
df.to_csv("weather_data.csv", index=False) 