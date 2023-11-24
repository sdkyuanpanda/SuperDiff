import torch
import math
import numpy as np

def same_vectors_check(tensor1, tensor2):
    set1 = set(map(tuple, tensor1.tolist()))
    set2 = set(map(tuple, tensor2.tolist()))
    if set1 == set2:
        return True
    else:
        return False