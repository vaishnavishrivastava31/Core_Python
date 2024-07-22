numbers= [1,2,3,4,5]
def largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number>largest:
            largest = number
    return largest
largest_number = largest_number(numbers)
print(largest_number)
