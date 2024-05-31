################################
# Github Repo link
# Your Name
# Your Section 
# Your Student ID Number
################################
# REFERENCES
# Links that you referred while solving 
# the problem
# http://link.to.an.article/video.com 
################################
# SOLUTION
# Your Solution Score: <total sum>
################################
# Function to read the input file and process each line
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return lines
 
# Function to extract the two-digit number from each line
def extract_number(line):
    first_digit = None
    last_digit = None
    
    # Find the first digit
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    
    # Find the last digit
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    return 0

# Function to calculate the total sum of the extracted numbers
def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        total_sum += extract_number(line)
    return total_sum

# Main function to read the file, process it, and print the solution
def print_solution(file_name):
    lines = read_input(file_name)
    total_sum = calculate_sum(lines)
    print(f"The total sum from the given input file {file_name} is {total_sum}")

# Run the solution with the given file
file_name = '178.txt'  
print_solution(file_name)
