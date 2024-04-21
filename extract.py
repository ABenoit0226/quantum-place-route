import csv

def read_last_line_of_csv(file_path):
    """Reads the last line from a CSV file."""
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        last_line = None
        for line in reader:
            last_line = line  # This will end up being the last line
        return last_line

def percent_reduction(values):
    """Calculates percent reduction of the biggest value from the other three."""
    numbers = list(map(float, values))  # Convert all values to floats
    max_value = max(numbers)
    reductions = [(max_value - value) / max_value * 100 for value in numbers if value != max_value]
    return reductions

def main(file_path):
    # Extract the last line from the CSV
    last_line = read_last_line_of_csv(file_path)
    
    # Calculate percent reductions
    if last_line and len(last_line) >= 4:
        reductions = percent_reduction(last_line[-4:])  # Take the last 4 values
        print("Percent reductions from the biggest of the last four values:")
        for reduction in reductions:
            print(f"{reduction:.2f}%")
    else:
        print("Error: The last line does not contain at least 4 values.")

# File path to the CSV file
file_path = 'mod/tests/qubit100vals256max.csv'
main(file_path)
