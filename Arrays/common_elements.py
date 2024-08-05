def find_common_elements(array1, array2):
    # Convert the arrays to sets to find common elements
    set1 = set(array1)
    set2 = set(array2)

    # Find the intersection of both sets
    common_elements = set1.intersection(set2)

    # Convert the set back to a list
    return list(common_elements)


# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
print(find_common_elements(array1, array2))
