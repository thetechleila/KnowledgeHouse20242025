import pandas as pd
import datetime

#Read the weather_data.csv file
df = pd.read_csv("weather_api_project/data/csv/weather_data.csv", header=0)

#Remove spaces 
df.columns = df.columns.str.strip()

#Convert date information to datetime
df.set_index("time")
df["time"] = pd.to_datetime(df["time"])


