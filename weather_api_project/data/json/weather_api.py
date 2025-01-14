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
    
#Remove HTML tag & metadata from the BeautifulSoup variable soup with the get_text() method then saving as json file

#soup.get_text() removes the HTML tags & metadata, leaving only the text
clean_page = soup.get_text()

#saves cleaned data as weather_json_api.json. The "with" statement automatically closes file 
with open("weather_json_api.json", "w") as file:
    file.write(clean_page)
    
#Convert the json file 'weather_json_api.json' into a CSV file
#First step is to convert the json file into a Python dictionary
with open ("weather_json_api.json", "r") as file:
    csv_data = file.read()

parsed_csv_data = json.loads(csv_data)

#Second - Create a DataFrame from the dictionary 'parsed_csv_data'
df = pd.DataFrame.from_dict(parsed_csv_data, orient="columns")

df.to_csv("weather_data.csv", index=False)
