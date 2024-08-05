from collections import Counter

def count_frequencies(arr):
    counter = Counter(arr)
    return counter

# Example usage
array = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
frequencies = count_frequencies(array)

# Print the result
for element, count in frequencies.items():
    print(f"Element {element}: {count} times")
