import requests
import json
import pandas as pd

#Get the page through get method then Scrape the open-meteo.com/en/docs site
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York"

page = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York")

#Convert page variable into json without metadata
api_in_json = page.json()

# Nested JSON data
json_data = {
    "name": ["John", "Jane", "Bob"],
    "age": [25, 30, 35],
    "city": ["New York", "San Francisco", "Chicago"],
    "children": [
        {"child_name": "Mary", "child_age": 5},
        {"child_name": "Tom", "child_age": 3},
        {"child_name": "Kate", "child_age": 2}
    ]
}

# Convert dictionary to JSON string
json_data = json.dumps(json_data)

# Convert JSON string to Pandas DataFrame
df = pd.read_json(json_data, orient="columns")

df.to_csv("weather_data.csv", index=False) 