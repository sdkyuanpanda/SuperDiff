import pandas
import numpy as np
import csv
import math
import smact
from smact.screening import pauling_test
import itertools
from fractions import Fraction
import functools
from pymatgen.core.composition import Composition

def smact_validity(comp, count,
                   use_pauling_test=True,
                   include_alloys=True):
    """
    Define smact validation function. Basic Charge Neutrality and Electronegativity Balance checks.
    Same method as https://github.com/cseeg/DiSCoVeR-SuperCon-NOMAD-SMACT/blob/main/main.ipynb on SuperCon
    Adapted from CDVAE (https://arxiv.org/abs/2110.06197)
    """
    global compositions
    space = smact.element_dictionary(comp)
    smact_elems = [e[1] for e in space.items()]
    electronegs = [e.pauling_eneg for e in smact_elems]
    ox_combos = [e.oxidation_states for e in smact_elems]
    if len(set(comp)) == 1:
        return True
    if include_alloys:
        is_metal_list = [elem_s in smact.metals for elem_s in comp]
        if all(is_metal_list):
            return True

    threshold = np.max(count)
    compositions = []
    for ox_states in itertools.product(*ox_combos):
        stoichs = [(c,) for c in count]
        # Test for charge balance
        cn_e, cn_r = smact.neutral_ratios(
            ox_states, stoichs=stoichs, threshold=threshold)
        # Electronegativity test
        if cn_e:
            if use_pauling_test:
                try:
                    electroneg_OK = pauling_test(ox_states, electronegs)
                except TypeError:
                    # if no electronegativity data, assume it is okay
                    electroneg_OK = True
            else:
                electroneg_OK = True
            if electroneg_OK:
                for ratio in cn_r:
                    compositions.append(
                        tuple([comp, ox_states, ratio]))
    compositions = [(i[0], i[2]) for i in compositions]
    compositions = list(set(compositions))
    if len(compositions) > 0:
        return True
    else:
        return False


def filter_for_valid_generated_compounds(generated_superconductors_raw):
    """
    :param generated_superconductors_raw: Np array of basic raw output generated superconductors.
    """
    generated_supercon_raw_df = pandas.DataFrame(generated_superconductors_raw)
    generated_supercon_raw_df.rename(columns={0: 'formula'}, inplace=True)
    
    vals2 = []
    for i in generated_supercon_raw_df['formula']:
      form_dict = Composition(i).to_reduced_dict

      comp = tuple(form_dict.keys())

      count = list(form_dict.values())

      #find least common multiple to get count as a tuple of ints
      denom_list = [(Fraction(x).limit_denominator()).denominator for x in count]
      lcm = functools.reduce(lambda a,b: a*b//math.gcd(a,b), denom_list)

      count_list = []
      for i in count:
        count_list.append(int(i*lcm))

      count = tuple(count_list)

      #vals2 is a list of Boolean corresponding to each formula's validity
      vals2.append(smact_validity(comp, count))
    
    ### 6730/12415 formulas are valid (54%) - from https://github.com/cseeg/DiSCoVeR-SuperCon-NOMAD-SMACT/blob/main/main.ipynb on SuperCon
    ### append Boolean vals to train_df

    generated_supercon_raw_df['is_valid'] = vals2
    
    # Convert DataFrame to NumPy array
    generated_supercon_tested = generated_supercon_raw_df.values
    
    valid_generated_compounds = []
    for i in range(np.size(generated_supercon_tested, 0)):
        if generated_supercon_tested[i][1] == True:
            valid_generated_compounds.append(generated_supercon_tested[i][0])
            
    valid_generated_compounds = np.array(valid_generated_compounds)
    valid_generated_compounds_size = np.size(valid_generated_compounds)
    print(valid_generated_compounds_size) 

    return valid_generated_compounds, valid_generated_compounds_size