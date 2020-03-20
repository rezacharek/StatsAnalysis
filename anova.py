import numpy as np
import basicstats as bs
import math
import matplotlib.pyplot as plt
import statistics

def element_counter(array):
    counter = 0
    elements = set()
    for x in array:
        if(x not in elements):
            elements.add(x)
            counter += 1
    return counter

def redefine_arrays(nbr_diff_elem, x_array, y_array):
    pass

class anova1:
    def __init__(x_array, y_array):
        self.x_array = x_array
        self.y_array = y_array
        self.nbr_diff_elem = element_counter(x_array)
        #https://towardsdatascience.com/1-way-anova-from-scratch-dissecting-the-anova-table-with-a-worked-example-170f4f2e58ad

