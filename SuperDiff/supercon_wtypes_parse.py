import numpy as np
import math
from typing import Tuple
from helper_formula_parse import *

# Function to read and parse the .dat file
def parse_dat_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            # Assuming four columns in the .dat file
            if len(parts) == 4:
                # Convert data to appropriate types if needed
                index = int(parts[0])
                name = parts[1]
                tc = float(parts[2])
                label = int(parts[3])
                data.append([index, name, tc, label])
            else:
                print(f"Warning: Skipping line '{line}' as it does not have four columns.")

    return np.array(data)

def preprocess_supercon_wtypes(FILE_NAME: str, element_table: list[str]) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    function for preprocessing Supercon with types.
    
    :param FILE_NAME: file name of supercon with types
    :param element_table: list of elements symbols
    """
    supercon_wtypes_raw = parse_dat_file(FILE_NAME)

    # assert correct # of rows
    assert(np.size(supercon_wtypes_raw, 0) == 16708)

    supercon_wtypes_raw_index = supercon_wtypes_raw[:, 0]
    supercon_wtypes_raw_formulas = supercon_wtypes_raw[:, 1]
    supercon_wtypes_raw_tc = supercon_wtypes_raw[:, 2]
    supercon_wtypes_raw_labels = supercon_wtypes_raw[:, 3]

    # assert correct #
    assert(np.size(supercon_wtypes_raw_index) == 16708)
    assert(np.size(supercon_wtypes_raw_formulas) == 16708)
    assert(np.size(supercon_wtypes_raw_tc) == 16708)
    assert(np.size(supercon_wtypes_raw_labels) == 16708)

    # convert supercon_wtypes_raw_formulas strings into vectors in R^{1x96}
    supercon_wtypes_vector_formulas = []
    for i in range(np.size(supercon_wtypes_raw_formulas)):
        split_formula_char = split_scform_to_char(supercon_wtypes_raw_formulas[i])
        merge_formula_char = merge_sc_char(split_formula_char)
        vector_formula = split_sc_to_vector(merge_formula_char, element_table)
        supercon_wtypes_vector_formulas.append(vector_formula)
    
    # convert to np array
    supercon_wtypes_vector_formulas = np.array(supercon_wtypes_vector_formulas)
    assert(np.size(supercon_wtypes_vector_formulas, 0) == np.size(supercon_wtypes_raw_formulas))

    # vector formulas with labels
    supercon_wtypes_vector_formulas_wlabels = np.column_stack((supercon_wtypes_vector_formulas, supercon_wtypes_raw_labels))
    
    return supercon_wtypes_raw_index, supercon_wtypes_vector_formulas, supercon_wtypes_raw_tc, supercon_wtypes_raw_labels, supercon_wtypes_vector_formulas_wlabels