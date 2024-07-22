# list_operation.py

def find_maximum(numbers):
    """Returns the maximum element in the list."""
    if not numbers:
        return None
    return max(numbers)

def find_minimum(numbers):
    """Returns the minimum element in the list."""
    if not numbers:
        return None
    return min(numbers)

def calculate_sum(numbers):
    """Returns the sum of all elements in the list."""
    return sum(numbers)

def calculate_average(numbers):
    """Returns the average of all elements in the list."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def sort_list(numbers):
    """Returns the list sorted in ascending order."""
    return sorted(numbers)

