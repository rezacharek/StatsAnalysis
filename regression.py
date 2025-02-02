import numpy as np
import basicstats as bs
import math
import matplotlib.pyplot as plt
import statistics
from termcolor import colored
from scipy import stats
from rich.console import Console
from rich.table import Column, Table
import os

class linear_regression:
    def __init__(self, x_array, y_array):
        self.length_x = len(x_array)
        self.length_y = len(y_array)

        if(self.length_x == self.length_y and self.length_x != 0):
            self.x_array = x_array
            self.y_array = y_array
            self.analysis()
        else:
            raise ValueError("The length of X and Y differ or at least one of them is equal to zero")

    def analysis(self):
        ### Computation of Beta0 and Beta1
        self.cxy = 0
        self.mean_x = bs.mean(self.x_array)
        self.mean_y = bs.mean(self.y_array)

        self.standart_deviation_squared_x = bs.standart_deviation(self.x_array)
        self.standart_deviation_squared_y = bs.standart_deviation(self.y_array)
        
        self.rxy = 1

        for i in range(self.length_x):
            self.cxy += (self.x_array[i] - self.mean_x) * (self.y_array[i] - self.mean_y)
        
        self.cxy = self.cxy/self.length_x
        self.rxy = self.cxy/( self.standart_deviation_squared_x *self.standart_deviation_squared_y)

        self.beta_one = self.cxy/bs.empirical_variance(self.x_array)
        self.beta_zero = self.mean_y - self.beta_one*self.mean_x
    
        #computation of the mmserror
        self.minimal_mean_squared_error = bs.empirical_variance(self.y_array)*(1-self.rxy**2)

        #computation of residuals:
        self.empirical_residuals = self.y_array - self.beta_one*self.x_array - self.beta_zero*np.repeat(1,self.length_x)
        self.residual_variance = bs.empirical_variance(self.empirical_residuals)

        #computation of sigma:
        self.sigma_squared_estimator = self.length_x/(self.length_x - 2)*self.residual_variance


    def beta_values(self):
        return self.beta_zero, self.beta_one

    
    def plot(self):
        plt.plot(self.x_array,self.y_array,'o')
        self.regression_line = self.beta_one*self.x_array + self.beta_zero*np.repeat(1,self.length_x)
        plt.plot(self.x_array,self.regression_line)
        plt.show()

    
    def mmserror(self):
        return self.minimal_mean_squared_error

    
    def sigma(self):
        return self.sigma_squared_estimator

    
    def hypothesis_test(self):
        pass

    def confidence_interval(self, alpha=0.05):
        a = self.beta_one
        b = self.beta_one
        a -= self.sigma_squared_estimator*(stats.t.ppf(1-alpha,self.length_x - 2))/(self.standart_deviation_squared_x * math.sqrt(self.length_x))
        b += self.sigma_squared_estimator*(stats.t.ppf(1-alpha,self.length_x - 2))/(self.standart_deviation_squared_x * math.sqrt(self.length_x))
        
        self.int_beta_one = [a,b]

        c = - stats.t.ppf(1-alpha, self.length_x - 2 )*self.sigma_squared_estimator
        d = stats.t.ppf(1-alpha, self.length_x - 2 )*self.sigma_squared_estimator

        c *= math.sqrt(self.standart_deviation_squared_x**2 + self.mean_x**2)
        d *= math.sqrt(self.standart_deviation_squared_x**2 + self.mean_x**2)

        c /= (self.standart_deviation_squared_x * math.sqrt(self.length_x))
        d /= (self.standart_deviation_squared_x * math.sqrt(self.length_x))

        c += self.beta_zero
        d += self.beta_zero
        
        self.int_beta_zero = [c,d]

        return self.int_beta_one, self.int_beta_zero

    def info(self):
        os.system("clear")
        console = Console()
        table = Table(show_header=True, header_style="bold yellow")
        table.add_column("Beta Zero")
        table.add_column("Beta One")
        table.add_column("Minimal Mean Squared Error")
        table.add_column("Sigma Squared Estimator")
        
        table.add_row("[#9deaff]"+str(self.beta_zero)+"[/#9deaff]", "[#9deaff]"+str(self.beta_one)+"[/#9deaff]", "[#9deaff]"+str(self.minimal_mean_squared_error)+"[/#9deaff]", "[#9deaff]"+str(self.sigma_squared_estimator)+"[/#9deaff]")
        console.print(table)


class multiple_linear_regression:
    def __init__(self, x_matrix, y_array):
            self.x_matrix = x_matrix
            self.y_array = np.transpose(y_array)
            self.beta_matrix()

    def beta_matrix(self):
        x = np.ones((len(self.x_matrix),len(self.x_matrix[0])+1))
        for i in range(len(self.x_matrix)):
            for j in range(1,len(self.x_matrix[0])+1):
                x[i][j] = self.x_matrix[i][j-1]
        

        self.x_matrix = x.copy()
        self.beta = np.dot(np.transpose(self.x_matrix) , self.x_matrix)
        self.beta = np.linalg.inv(self.beta)
        self.beta = np.dot(self.beta, np.transpose(self.x_matrix)) 
        self.beta = np.dot(self.beta, self.y_array)

        return self.beta
    
    def info(self):
        # os.system("clear")
        # console = Console()
        # table = Table(show_header=True, head_style="bold yellow")
        print(colored(self.beta, "green"))

class logistic_regression:
    pass
    
    
