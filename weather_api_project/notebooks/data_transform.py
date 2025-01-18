import pandas as pd
import datetime

#Read the weather_data.csv file
df = pd.read_csv("weather_api_project/data/csv/weather_data.csv", header=0)

#Remove spaces and drop null values
df.columns = df.columns.str.strip().dropna(how="any")

#Convert date information to datetime then set "time" as the index
df["time"] = pd.to_datetime(df["time"])
df.set_index("time", inplace=True)

#Calculate monthly medians on temperature, relative humidity, precipitation, and surface pressure then save as a new DataFrame
monthly_medians = df.resample('M').median()

#Convert the monthly medians DataFrame into a CSV file
#monthly_medians.to_csv("monthly_medians_mg.csv")

#Calculate yearly medians on temperature, relative humidity, precipitation, and surface pressure then save a new DataFrame
yearly_medians = df.resample('Y').median()

#Convert the "yearly_medians" DataFrame into a CSV file
#yearly_medians.to_csv("yearly_medians_mg.csv")

#Convert the br_final.csv file into a DataFrame and drop null values
df_br1 = pd.read_csv("weather_api_project/data/csv/br_final.csv")
df_br1.dropna(inplace=True)


#Calculate yearly medians on temperature, relative humidity, precipitation, and surface pressure then save a new DataFrame from br_final.csv
#This dataframe will include the following harvest data: million_60kgs, nonbear_mill_trees, bear_mill_trees, avg_unemp_perc for 2022-2023
