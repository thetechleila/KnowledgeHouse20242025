"""
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    
    maximums = []
"""


def window_max(data: list, n: int) -> list:
    maximums = []
    for h in range(0, len(data), n):
        alist = data[h: h + n]
        maximums.append(max(alist))
    return maximums

#print(window_max(window_max, 6))
    


"""
#This will calculate the average of all values in the list by getting the sum of all values then dividing the sum 
by the amount of elements in the list. The averages with then be appended to the list win_avg and win_avg is 
returned
"""

def window_average(data: list, n: int) -> list:
    win_avg = []
    for b in range (0, len(data), n):
        actual_averg = sum(window_average)/len(window_average)
        win_avg.append(actual_averg)
    return win_avg

"""
This function calculates the standard deviation step by step. We find the average by dividing the sum of the window by the length of 
the window. Then the variance is determined using the average and length. The standard dev will be the square root of the variance. 
The standard deviation is then rounded to only have 2 decimal spaces and appended to the list 'devia'

devia - short for deviation
"""

def window_stddev(data: list, n: int) -> list:
    devia = []
    for w in range(0,len(data), n):
        window = data[w:w+n]
        if len(window) == 1:
            continue
        window_average = sum(window) / len(window)
        variance = sum((w- window_average)** 2 for w in window) / (len(window) -1)
        std_dev = variance ** 0.5
        devia.append(round(std_dev,2))
    return devia
