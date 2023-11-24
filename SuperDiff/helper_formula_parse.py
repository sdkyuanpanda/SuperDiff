import numpy as np
import math


def split_scform_to_char(scform_str: str) -> list[str]:
    """
    Split chemical formula string into list of characters.

    :param sc_str: Chemical formula as a string
    """
    split_sc_char = []

    for character in scform_str:
        split_sc_char.append(character)

    return split_sc_char


def merge_sc_char(split_sc_char: list[str]) -> list[str]:
    """
    Merge characters into list of useful element symbols and quantity numbers.

    :param split_sc_char: Chemical formula split by character
    """
    split_sc = []
    temp_numstr = ""
    temp_alphastr = ""

    for i in range(len(split_sc_char)):
        if split_sc_char[i].isalpha() == True:
            if temp_numstr != "":
                split_sc.append(temp_numstr)

            temp_alphastr += split_sc_char[i]
            temp_numstr = ""
        else:
            if temp_alphastr != "":
                split_sc.append(temp_alphastr)
            temp_alphastr = ""
            temp_numstr += split_sc_char[i]

    if temp_numstr != "":
        split_sc.append(temp_numstr)

    if temp_alphastr != "":
        split_sc.append(temp_alphastr)

    return split_sc


def split_sc_to_vector(split_sc: list[str], chem_tableDS: list[str]) -> np.ndarray:
    """
    Converts list of chemical elements and quantities to vector in R^(1x96), with index matching elements
    in periodic table from 1 to 96

    :param split_sc: list of chemical elements and associated quantities
    :param chem_tableDS: periodic table of first 96 elements
    """
    sc_vector = np.zeros((1, 96))  # replace size if not R^(8x96)
    for i in range(len(split_sc)):
        if split_sc[i].isalpha() == True:
            for j in range(len(chem_tableDS)):
                if split_sc[i] == chem_tableDS[j]:
                    if i + 1 < len(split_sc):
                        sc_vector[0][j] = float(split_sc[i + 1])  # split_sc[i+1] contains associated quantity
                    else:
                        sc_vector[0][j] = 1.0  # verify if none at the end = 1.0

    sc_vector = sc_vector.squeeze()  # remove outer parathesis, decrease dimension

    return sc_vector
