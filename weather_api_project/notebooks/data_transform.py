import pandas as pd
import datetime

#Read the weather_data.csv file
df = pd.read_csv("weather_api_project/data/csv/weather_data.csv", header=0)

#Remove spaces and drop null values
df.columns = df.columns.str.strip().dropna(how="any")

#Convert date information to datetime then set "time" as the index
df["time"] = pd.to_datetime(df["time"])
df.set_index("time", inplace=True)

#Calculate monthly medians on temperature, relative humidity, precipitation, and surface pressure for all available months then save as a new DataFrame
monthly_medians = df.resample('M').median()

#Convert the monthly medians DataFrame into a CSV file called "monthly_medians_mg.csv"
#monthly_medians.to_csv("monthly_medians_mg.csv")

#Calculate yearly medians on temperature, relative humidity, precipitation, and surface pressure for all available years then save a new DataFrame
yearly_medians = df.resample('Y').median()


#Convert the "yearly_medians" DataFrame into a CSV file called "yearly_medians_mg.csv"
#yearly_medians.to_csv("yearly_medians_mg.csv")

#Convert the br_final.csv file into a DataFrame then drop the "avg_unemp_perc" column to remove null data there and dropna() to remove all other nulls
#Convert to datetime
df_br1 = pd.read_csv("weather_api_project/data/csv/br_final.csv")
df_br1.set_index("year")
df_br1.dropna(how="all")
df_br1.drop(columns="avg_unemp_perc", inplace=True)



#Calculate yearly medians of millions_60kgs_bag, nonbear_mill_trees, bear_mill_trees from df_br1 for all years available for Minas Gerais
df_mg = df_br1[df_br1["subdivision"]=="Minas Gerais"]
minas_df =df_mg.groupby("year")[[
    "million_60kgs_bag",
    "nonbear_mill_trees",
    "bear_mill_trees"
]].median()


#Drop the year row 2018 due to NaN values in the nonbear_mill_trees and bear_mill_trees rows for that year


#Convert yearly_minas_df in a CSV file called "yearly_harvest_medians.csv"
#minas_df.to_csv("yearly_harvest_medians.csv")

#Merge the "yearly_medians" and "yearly_minas_df" DataFrames
