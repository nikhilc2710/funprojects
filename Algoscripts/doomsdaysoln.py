import numpy as np
import pandas as pd
from fractions import Fraction

def solution(m):
    if m == [[0]]:
        return [1, 1]
    else:
        return run_matrix_computation(m)

def run_matrix_computation(starting_ore_matrix):
    numpy_matrix = convert_to_numpy_matrix(starting_ore_matrix)
    ordered_matrix = order_matrix(numpy_matrix)
    absorption_matrix, split_index = create_absorption_matrix(ordered_matrix)
    R, Q = store_R_and_Q(absorption_matrix, split_index)
    FR = compute_FR(R, Q)
    first_row = get_first_row_of_FR(FR)
    common_denominator, fraction_list = calculate_common_denominator(first_row)
    return return_int_array(common_denominator, fraction_list)

def convert_to_numpy_matrix(original_matrix):
    return np.asarray(original_matrix)

def order_matrix(numpy_matrix):
    labeled_dataframe = pd.DataFrame(data=numpy_matrix)
    index_order = labeled_dataframe.sum(axis=1).sort_values(ascending=True).index
    converted_matrix = convert_matrix_to_fractions(labeled_dataframe)
    return converted_matrix.iloc[index_order, index_order]

def convert_matrix_to_fractions(original_matrix):
    for i in range(len(original_matrix.index)):
        sum = original_matrix.sum(axis=1).iloc[i]
        if sum != 0:
            for j in range(len(original_matrix.columns)):
                if original_matrix.iloc[i, j]:
                    original_matrix.iloc[i, j] = original_matrix.iloc[i, j] / sum
    return original_matrix

def create_absorption_matrix(sorted_matrix):
    count = 0
    for i in range(len(sorted_matrix.index)):
        if not(sorted_matrix.sum(axis=1).iloc[i]):
            sorted_matrix.iloc[i, i] = 1
            count = count + 1
    return sorted_matrix, count

def store_R_and_Q(absorption_matrix, split_index):
    return split_into_new_matrices(absorption_matrix, split_index)

def split_into_new_matrices(absorption_matrix, split_index):
    numpy_matrix = absorption_matrix.to_numpy()
    R = numpy_matrix[split_index:, :split_index]
    Q = numpy_matrix[split_index:, split_index:]
    return R, Q

def calculate_F(R, Q):
    num_rows, num_cols = Q.shape
    I = np.identity(num_rows)
    IQ = I - Q
    return np.linalg.inv(IQ)

def compute_FR(R, Q):
    F = calculate_F(R, Q)
    return np.matmul(F, R)

def get_first_row_of_FR(FR):
    return FR[0, :]

def calculate_common_denominator(list):
    fraction_list = convert_to_fractions(list)
    list_denominators = get_denominators(fraction_list)
    GCD = calculate_greatest_common_denominator(list_denominators)
    return GCD, fraction_list

def convert_to_fractions(list):
    fraction_list = []
    for i in range(len(list)):
        fraction_list.append(Fraction(list[i]).limit_denominator())
    return fraction_list

def get_denominators(fractions):
    denominators = []
    for i in range(len(fractions)):
        denominators.append(fractions[i].denominator)
    return denominators

def calculate_greatest_common_denominator(denominators):
    GCD = 0
    if len(denominators) == 1:
        return denominators
    else:
        for i in range(len(denominators) - 1):
            cur_GCD = np.lcm(denominators[i], denominators[i + 1])
            if cur_GCD > GCD:
                GCD = cur_GCD
    return GCD

def return_int_array(denominator, fractions):
    final_list = []
    for i in range(len(fractions)):
        if(not fractions[i].numerator):
            final_list.append(0)
        else:
            multiplier = denominator/fractions[i].denominator
            final_list.append(int(fractions[i].numerator * multiplier))
    final_list.append(int(denominator))
    return final_list