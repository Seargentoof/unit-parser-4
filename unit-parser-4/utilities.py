"""
Utilities for the unitParser 4 program. 

Dawson Lin, 7/25/2023
"""


"""
Reads a file line-by-line and returns it as a list lines. 
"""
def read_file_lines(filePath):
    try:
        with open(filePath, 'r') as file:
            lines = [line.rstrip('\n') for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print(f"File '{filePath}' not found.")
        return []
    except IOError:
        print(f"Error reading file '{filePath}'.")
        return []
    
"""
Takes a string representation of a number num, strips it of commas, 
and returns it as a string. 
"""
def remove_commas(num: str) -> str:
    # Remove commas from the string representation of the number
    cleaned_num = num.replace(",", "")
    return cleaned_num

