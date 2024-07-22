import dataprocessing

def main():
    # Prompt user to enter a list of numbers
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]  # Convert input to list of floats

    # Calculate mean, median, and mode
    mean_value = dataprocessing.calculate_mean(numbers)
    median_value = dataprocessing.calculate_median(numbers)
    mode_value = dataprocessing.calculate_mode(numbers)

    # Print results
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Mode: {mode_value}")
if __name__ == "__main__":
    main()