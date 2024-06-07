# filesplitter.py

"""
Made with the express intent to split the
cursed VLA Calibrator .txt file before I
lose my sanity
"""

import os

# Path to the input file
input_file_path = 'calibrators.txt'
output_dir = 'split_calibrators/'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

with open(input_file_path, 'r') as file:
    lines = file.readlines()

    current_file = None
    current_file_path = None

    for line in lines:
        stripped_line = line.strip()

        if stripped_line:  # Check if line is not empty
            if current_file is None:
                # New file, get the IAU Name for the file name
                iau_name = stripped_line.split()[0]
                current_file_path = os.path.join(output_dir, f'{iau_name}.txt')
                current_file = open(current_file_path, 'w')

            current_file.write(line)
        else:
            # Close the current file and reset
            if current_file:
                current_file.close()
                current_file = None

    # Ensure the last file is closed
    if current_file:
        current_file.close()

print("Files created successfully!")