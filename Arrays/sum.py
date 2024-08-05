def sum(array):
    total = 0
    for element in array:
        total += element
    return total
array = [1,2,3,4,5]
total_sum = sum(array)
print(total_sum)