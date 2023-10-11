#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weighted_sum = 0
    total_weights = 0

    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weights += weight

    return total_weighted_sum / total_weights
