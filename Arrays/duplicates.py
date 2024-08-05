def remove_duplicates(arr):
    return list(set(arr))

# Example usage
array_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 6, 6]
array_without_duplicates = remove_duplicates(array_with_duplicates)

print("Array with duplicates:", array_with_duplicates)
print("Array without duplicates:", array_without_duplicates)
