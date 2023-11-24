import math
import numpy as np
import torch
from typing import Tuple
from typing import List
import csv

# file import
from helper_formula_parse import *
from supercon_wtypes_parse import *
from helper_dataset_shuffle import *
from helper_reverse_formula import *


def create_datasets(torch_diffusion_data_raw, TEST_SIZE_FACTOR, USE_VALIDATION_SET):
    """
    Creates test and val datasets. Shuffles data as well. Set USE_VALIDATION_SET = False for just shuffling.
    """
    # dataset creation: split train and validation set
    diffusion_raw_size = torch_diffusion_data_raw.size(0)
    if USE_VALIDATION_SET == True:
        TEST_SIZE_FACTOR = TEST_SIZE_FACTOR # ~Same ratio as CIFAR-10
    else:
        TEST_SIZE_FACTOR = 0
    test_diffusion_data_size = math.floor(diffusion_raw_size * TEST_SIZE_FACTOR)
    train_diffusion_data_size = diffusion_raw_size - test_diffusion_data_size
    assert(train_diffusion_data_size + test_diffusion_data_size == diffusion_raw_size)

    indices = torch.randperm(diffusion_raw_size)
    indices_train = indices[:train_diffusion_data_size]
    indices_test = indices[train_diffusion_data_size:]

    torch_diffusion_data_raw_train = torch_diffusion_data_raw[indices_train]
    torch_diffusion_data_raw_test = torch_diffusion_data_raw[indices_test]

    assert(torch_diffusion_data_raw_train.size(0) == train_diffusion_data_size)
    assert(torch_diffusion_data_raw_test.size(0) == test_diffusion_data_size)

    print(f"Train Data Size: {torch_diffusion_data_raw_train.size(0)} | Test Data Size: {torch_diffusion_data_raw_test.size(0)}")

    assert(same_vectors_check(torch.cat((torch_diffusion_data_raw_train, torch_diffusion_data_raw_test), dim=0), torch_diffusion_data_raw) == True)
    return torch_diffusion_data_raw_train, torch_diffusion_data_raw_test


def prepare_datasets_for_classes(SUPERCON_DATA_FILE, element_table, TEST_SIZE_FACTOR, return_test_sets):
    supercon_wtypes_raw_index, supercon_wtypes_vector_formulas, supercon_wtypes_raw_tc, supercon_wtypes_raw_labels, supercon_wtypes_vector_formulas_wlabels = preprocess_supercon_wtypes(SUPERCON_DATA_FILE, element_table)

    # ready 4 datasets: unconditional, cuprates, pnictides, and others
    
    torch_diffusion_data_raw_unconditional = torch.from_numpy(supercon_wtypes_vector_formulas).to(torch.float32)
    
    # parse out cuprate, pnictide, and others datasets
    supercon_wtypes_vector_formulas_wlabels = supercon_wtypes_vector_formulas_wlabels.astype(float)
    
    diffusion_data_raw_cuprates = []
    diffusion_data_raw_pnictides = []
    diffusion_data_raw_others = []
    for i in range(np.size(supercon_wtypes_vector_formulas_wlabels, 0)):
        if float(supercon_wtypes_vector_formulas_wlabels[i, -1:]) == 1.0:
            diffusion_data_raw_cuprates.append(supercon_wtypes_vector_formulas_wlabels[i, :-1])
        elif float(supercon_wtypes_vector_formulas_wlabels[i, -1:]) == 2.0:
            diffusion_data_raw_pnictides.append(supercon_wtypes_vector_formulas_wlabels[i, :-1])
        elif float(supercon_wtypes_vector_formulas_wlabels[i, -1:]) == 3.0:
            diffusion_data_raw_others.append(supercon_wtypes_vector_formulas_wlabels[i, :-1])
    
    diffusion_data_raw_cuprates = np.array(diffusion_data_raw_cuprates)
    diffusion_data_raw_pnictides = np.array(diffusion_data_raw_pnictides)
    diffusion_data_raw_others = np.array(diffusion_data_raw_others)
    
    torch_diffusion_data_raw_cuprates = torch.from_numpy(diffusion_data_raw_cuprates).to(torch.float32)
    torch_diffusion_data_raw_pnictides = torch.from_numpy(diffusion_data_raw_pnictides).to(torch.float32)
    torch_diffusion_data_raw_others = torch.from_numpy(diffusion_data_raw_others).to(torch.float32)

    print(torch_diffusion_data_raw_unconditional.size())
    print(torch_diffusion_data_raw_cuprates.size())
    print(torch_diffusion_data_raw_pnictides.size())
    print(torch_diffusion_data_raw_others.size())
    
    # make sure size of the 3 sub datasets adds up the same
    assert(torch_diffusion_data_raw_cuprates.size(0) + torch_diffusion_data_raw_pnictides.size(0) + torch_diffusion_data_raw_others.size(0) == torch_diffusion_data_raw_unconditional.size(0))

    torch_diffusion_data_raw_unconditional_train, torch_diffusion_data_raw_unconditional_test = create_datasets(torch_diffusion_data_raw_unconditional, TEST_SIZE_FACTOR, return_test_sets)
    torch_diffusion_data_raw_cuprates_train, torch_diffusion_data_raw_cuprates_test = create_datasets(torch_diffusion_data_raw_cuprates, TEST_SIZE_FACTOR, return_test_sets)
    torch_diffusion_data_raw_pnictides_train, torch_diffusion_data_raw_pnictides_test = create_datasets(torch_diffusion_data_raw_pnictides, TEST_SIZE_FACTOR, return_test_sets)
    torch_diffusion_data_raw_others_train, torch_diffusion_data_raw_others_test = create_datasets(torch_diffusion_data_raw_others, TEST_SIZE_FACTOR, return_test_sets)

    if not return_test_sets:
        return torch_diffusion_data_raw_unconditional_train, torch_diffusion_data_raw_cuprates_train, torch_diffusion_data_raw_pnictides_train, torch_diffusion_data_raw_others_train
    else:
        return torch_diffusion_data_raw_unconditional_train, torch_diffusion_data_raw_cuprates_train, torch_diffusion_data_raw_pnictides_train, torch_diffusion_data_raw_others_train, torch_diffusion_data_raw_unconditional_test, torch_diffusion_data_raw_cuprates_test, torch_diffusion_data_raw_pnictides_test, torch_diffusion_data_raw_others_test




