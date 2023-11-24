import numpy as np
import math
import torch

def cform_from_vector(form_vector: torch.Tensor, chem_table: list[str]) -> str:
    """
    Helper Function to Turn R^{1x96} Vector back into Chemical Formula
    
    :param form_vector: Vector encoding of chemical formula
    :param chem_table: Periodic table of elements 1 to 96
    
    :return: String chemical formula
    """
    cform = ""
    for i in range(0, len(chem_table)):
        if form_vector[i] != 0.0:
            cform += f"{chem_table[i]}{form_vector[i]}"
    return cform