import re

def extract_and_sum_numbers(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Regular expression to match integers and floating-point numbers (both positive and negative)
        pattern = r'-?\d+(?:\.\d+)?'
        numbers = re.findall(pattern, content)

        # Convert extracted numbers to float
        numbers = [float(num) for num in numbers]

        # Display results
        print(f"Extracted numbers: {numbers}")
        print(f"Sum of all numbers: {sum(numbers)}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Specify the filename
filename = r'D:\PythonFiles\AMTH-450\Assignment_1\regex-sum-42.txt'
extract_and_sum_numbers(filename)


