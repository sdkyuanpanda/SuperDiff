import numpy as np
import csv
import math

# Function to convert a list of strings to CSV format
def strings_to_csv(data_list, file_path):
    with open(file_path, 'w') as f:
        for item in data_list:
            f.write(item + '\n')

def store_valid_to_csv(valid_generated_compounds, output_file):
    """
    Store valid generated superconductors to output_file
    """
    # Use the function to save the array to the CSV file
    strings_to_csv(valid_generated_compounds, output_file)
    
    # checks:
    # ensure correct CSV file writing
    test_array_generated = np.genfromtxt(output_file, delimiter=',', dtype = str)
    assert(np.size(test_array_generated) == np.size(valid_generated_compounds))

    for i in range(np.size(test_array_generated)):
        if test_array_generated[i] != valid_generated_compounds[i]:
            raise Exception("Non equal elements - fix parsing")
    
    print("Array has been successfully saved to CSV file.")