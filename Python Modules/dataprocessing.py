from statistics import mean, median, mode, StatisticsError

def calculate_mean(numbers):
    return mean(numbers)

def calculate_median(numbers):
    return median(numbers)

def calculate_mode(numbers):
    try:
        return mode(numbers)
    except StatisticsError:
        return "No unique mode"