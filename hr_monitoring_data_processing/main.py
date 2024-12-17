"""
The main Python module that combines cleaner and metrics functions in order to
perform comprehensive analysis

    Process heart rate data from the specified file, clean it, calculate metrics, 
    and save visualizations.

    Args:
        filename (str): The path to the data file (e.g., 'data/data1.txt').

    Steps:
        1. Read the file into a list of strings.
        2. Use `filter_nondigits` to clean the data and remove invalid entries.
        3. Use `filter_outliers` to remove unrealistic heart rate samples (<30 or >250).
        4. Calculate rolling maximums, averages, and standard deviations using functions from `metrics.py`.
        5. Save the plots to the `images/` folder:
            - Rolling maximums -> 'images/maximums.png'
            - Rolling averages -> 'images/averages.png'
            - Rolling standard deviations -> 'images/stdevs.png'

    Returns:
        list[int], list[int], list[int]: You will return the maximums, averages, and stdevs (in this order).
    open file and read into the 'data' list
    return all 3 lists
"""

from metrics import window_max, window_average, window_stddev
from cleaner import filter_nondigits, filter_outliers

import matplotlib.pyplot as plt


#Opens the .txt file then reads that info. The info is then appended to the "data" list after conversion
#into a string
data = []

def run(filename: str) -> None:
    file = open(filename)
    for line in file:
        data.append(str(line))
    return data


#The 'filter_nondigits' function is called to filter out non numerical values from the 'data' list
data = filter_nondigits(data)

#The 'filter_outliers' function is called to filter outliers from the 'data' list
data = filter_outliers(data)

#This should create images for the maximums of our heart rate data. Our window size is 6 (n=6). Maximums comes from 
#importing window_max
#plt.subplots() creates the figure & a grid of subplots

maximums = window_max(data, 6)
fig, ax = plt.subplots()
ax.plot(maximums)



if __name__ == "__main__":
    run("hr_monitoring_data_processing/data/data1.txt")
