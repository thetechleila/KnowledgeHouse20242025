import requests
import json
import pandas as pd

#Request the data from the open-meteo.com/en/docs site
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York"

page = requests.get(URL)

#Write out website data in JSON format
api_in_json2 = page.json()

with open ("weather_2json_api.json", "w") as file:
    json.dump(api_in_json2, file)

#Extract relevant data from the "hourly" dictionary in api_in_json2
hourly_data = api_in_json2["hourly"]

#Create DataFrame from the "hourly_data"
df = pd.DataFrame(hourly_data)

#Covert DataFrame into a CSV file called weather_data.csv
df.to_csv("weather_data2.csv", index=False) 