import listoperations

def main():
    # Prompt user to enter a list of numbers
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]  # Convert input to list of floats

    # Perform operations using the list_operation module
    max_value = listoperations.find_maximum(numbers)
    min_value = listoperations.find_minimum(numbers)
    sum_value = listoperations.calculate_sum(numbers)
    average_value = listoperations.calculate_average(numbers)
    sorted_list = listoperations.sort_list(numbers)

    # Print results
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")
    print(f"Sum of elements: {sum_value}")
    print(f"Average of elements: {average_value}")
    print(f"Sorted list: {sorted_list}")

if __name__ == "__main__":
    main()

