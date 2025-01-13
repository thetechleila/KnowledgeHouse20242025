import requests
from bs4 import BeautifulSoup
import html2text
import json
import pandas as pd

#Get the page through get method then Scrape the open-meteo.com/en/docs site
URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York"

page = requests.get("https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure&timezone=America%2FNew_York")

#Parse Open-Meteo Page and store page in the "soup" variable
soup = BeautifulSoup(page.content, "html.parser")

#Save Open-Meteo Page Content as weather_scrape.html (just in case & for future reference)
with open ("weather_scrape.html", "w") as html_file:
    html_file.write(page.text)
    
#Remove HTML tag & metadata from the BeautifulSoup variable soup with the get_text() method then saving as text file
clean_page = soup.get_text()

with open("weather_json_api.txt", "w") as file:
    file.write(clean_page)

    
#Convert text file into JSON structure below

#Weather Data to be written to the JSON file
weather_params = {
    "latitude": -21.72,
    "longitude": -45.39,
    "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "surface_pressure"],
    "timezone": "America/New_York",
    "start_date": "2022-01-01",
    "end_date": "2023-12-31"
    
}

#Setting up json.dumps to contain info
weather_data_json = json.dumps(weather_params, indent=4)

#Write Weather Data to a json file, outfile.write() automatically closes the file when the block is exited
with open ("real_weather_api.json", "w") as outfile:
    outfile.write(weather_data_json)
    


