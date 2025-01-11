import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

#Scrape the open-meteo.com/en/docs site
URL = "https://api.open-meteo.com/v1/forecast"
page = requests.get("https://api.open-meteo.com/v1/forecast")
soup = BeautifulSoup(page.content, "html.parser")



#Get the JSON object of the result of page = requests.get("https://api.open-meteo.com/v1/forecast")
