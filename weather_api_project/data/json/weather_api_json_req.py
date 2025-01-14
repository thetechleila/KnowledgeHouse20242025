import requests
import json
import pandas as pd

#Get the page through get method then Scrape the open-meteo.com/en/docs site
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York"

page = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York")

#Convert page variable into json without metadata
api_in_json = page.json()

#Turn json object into dictionary 
