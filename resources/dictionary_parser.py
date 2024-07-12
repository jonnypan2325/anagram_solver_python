import json
from pathlib import Path

input_file_path = Path('resources/dictionary.txt')
output_file_path = Path('dictionary.json')

input_file = open(input_file_path, 'r')
output_file = open(output_file_path, 'w')

def check_bounds():
    while True:
        decide = input("Set upper/lower bounds? [y/n]: ").strip().lower()
        if decide == "y":
            try:
                lower_bound = int(input('Enter lower word length bound (positive integer): '))
                upper_bound = int(input('Enter upper word length bound (positive integer): '))
                if lower_bound > 0 and upper_bound >= lower_bound:
                    return (lower_bound, upper_bound)
                else:
                    print('Invalid input, try again.')
            except ValueError:
                print('Please enter valid positive integers.')
        elif decide == "n":
            return (0, 100)
        else:
            print('Invalid input, please enter "y" or "n".')
try:
    output_file.write('[')
    first = True 
    lower_bound, upper_bound = check_bounds() 
    for line in input_file:
        stripped_line = line.strip().lower()
        if not stripped_line or ' ' in stripped_line:
            continue
        if lower_bound <= len(stripped_line) <= upper_bound:
            if not first:
                output_file.write(',\n')
            else:
                first = False
            json.dump(stripped_line, output_file)
    output_file.write(']')

finally:
    input_file.close()
    output_file.close()
