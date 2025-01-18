import pandas as pd
import datetime

#Read the weather_data.csv file
df = pd.read_csv("weather_api_project/data/csv/weather_data.csv", header=0)

#Remove spaces 
df.columns = df.columns.str.strip().dropna(how="any")

#Convert date information to datetime 
df["time"] = pd.to_datetime(df["time"])
df.set_index("time", inplace=True)

#Calculate monthly medians on temperature, relative humidity, precipitation, and surface pressure then save a new DataFrame
monthly_medians = df.resample('M').median()

#Calculate yearly medians on temperature, relative humidity, precipitation, and surface pressure then save a new DataFrame
yearly_medians = df.resample('Y').median()

#Convert the br_final.csv file into a DataFrame
df_br = pd.read_csv("weather_api_project/data/csv/br_final.csv")
df_br.set_index("year")


#Calculate yearly medians on temperature, relative humidity, precipitation, and surface pressure then save a new DataFrame from br_final.csv
#This dataframe will include the following harvest data: million_60kgs, nonbear_mill_trees, bear_mill_trees, avg_unemp_perc for 2022-2023
minas_df = df_br.filter(items=["subdivision", "non_bear_mills"])
print(minas_df)

