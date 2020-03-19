import numpy as np
import math
def mean(values):
    if (isinstance(values, list) or isinstance(values, np.ndarray)):
        if(len(values) != 0):
            return sum(values)/len(values)
        else:
            raise ValueError("The array is empty")
    elif (isinstance(values, np.ndarray)):
        print("Yes")
    else:
        print("Fuck")

def empirical_variance(array):
    mean_ = mean(array)
    deviation = 0.0
    for i in range(len(array)):
        deviation += (float(array[i]) - mean_)**2
    return deviation/len(array)

# def quantile():

def standart_deviation(array):
    return math.sqrt(empirical_variance(array))

# def geometric_mean():

# def harmic_mean():

# def median():

# def sum():

# def empirical_variance():

