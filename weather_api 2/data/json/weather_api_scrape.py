import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

#Scrape the open-meteo.com/en/docs site
URL = "https://api.open-meteo.com/v1/forecast"
data = {
    "latitude": -21.72,
    "longitude": -45.39,
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "surface_pressure"],
    "timezone": "America/New_York",
    "start_date": "2022-01-01",
    "end_date": "2023-12-31"
    
}
page = requests.get("https://api.open-meteo.com/v1/forecast")
soup = BeautifulSoup(page.content, "html.parser")


weather_scrape = json.dumps(soup)
print(weather_scrape)