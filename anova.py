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
    

class anova1:
    def __init__(x_array, y_array):
        self.x_array = x_array
        self.y_array = y_array
        self.nbr_diff_elem = element_counter(x_array)

