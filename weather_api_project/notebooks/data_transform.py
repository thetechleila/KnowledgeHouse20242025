import pandas as pd
import datetime

#Read the weather_data.csv file
df = pd.read_csv("weather_api_project/data/csv/weather_data.csv", header=0)

#Remove spaces 
df.columns = df.columns.str.strip()

#Convert date information to datetime 
df["time"] = pd.to_datetime(df["time"])
df.set_index("time", inplace=True)

#Calculate monthly medians on temperature, relative humidity, precipitation, and surface pressure then save a new DataFrame
monthly_medians = df.resample('M').median()
