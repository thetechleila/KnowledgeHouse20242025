def filter_nondigits(data: list) -> list:
    only_digits = []
    for d in data:
        if d.strip().isdigit() == True:
            only_digits.append(int(d))
    return only_digits
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    pass

#Filters out data that is less than 30 AND data that is less than 250. This info is appended to the list, outcasts
def filter_outliers(data: list) -> list:
    outcasts = []
    for d in data:
        if data > 30 and data < 250:
            outcasts.append(data)
    return outcasts
