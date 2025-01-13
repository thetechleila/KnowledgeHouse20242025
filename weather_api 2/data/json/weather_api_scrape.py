import requests
from bs4 import BeautifulSoup
import html2text
import json
import pandas as pd

#Get the page through get method then Scrape the open-meteo.com/en/docs site
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York"
weather_params = {
    "latitude": -21.72,
    "longitude": -45.39,
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "surface_pressure"],
    "timezone": "America/New_York",
    "start_date": "2022-01-01",
    "end_date": "2023-12-31"
    
}

page = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York")

#Save Open-Meteo Page Content as weather_scrape.html (just in case & for future reference)
with open ("weather_scrape.html", "w") as html_file:
    html_file.write(page.text)
    
#Parse Open-Meteo Page and store page in the "soup" variable
soup = BeautifulSoup(page.content, "html.parser")

text_only_webpage = soup.findAll(string=True)
string = ''.join(text_only_webpage)
print(text_only_webpage)