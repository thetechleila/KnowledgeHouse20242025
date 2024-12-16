def filter_nondigits(data: list) -> list:
    squeaky = []
    for d in data:
        if d.strip().isdigit() == True:
            squeaky.append(int(d))
    return squeaky
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    pass


def filter_outliers(data: list) -> list:
    sparkle = []
    for d in data:
        if data > 30 and data < 250:
            sparkle.append(data)
    return sparkle
