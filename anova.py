import numpy as np
import basicstats as bs
import math
import matplotlib.pyplot as plt
import statistics
import scipy.stats
from termcolor import colored


class anova1:
    def __init__(self,quantitative_variable, qualitative_variable, data):
        self.quantitative_variable = quantitative_variable
        self.qualitative_variable = qualitative_variable
        self.data = data
        self.anova_analysis()
    
    def anova_analysis(self):
        #compute overall mean
        self.overall_mean = self.data[self.quantitative_variable].mean()

        #compute Sum of Squares Total
        print(colored(self.overall_mean, "red"))
        self.data['overall_mean'] = self.overall_mean
        
        self.ss_total = sum((self.data[self.quantitative_variable] - self.data['overall_mean'])**2)
        
        #compute group means
        self.group_means = self.data.groupby(self.qualitative_variable).mean()
        self.group_means = self.group_means.rename(columns = {self.quantitative_variable : 'group_mean'})
        # print(colored(self.data, "cyan"))
        # self.data['group_mean'] = self.group_means
        # print(colored(self.data, "green"))
        self.data = self.data.merge(self.group_means, left_on = self.qualitative_variable, right_index=True)
        

        #compute Sum of Squares Residual
        self.ss_residual = sum((self.data[self.quantitative_variable] - self.data['group_mean'])**2)

        #compute Sum of Squares Model
        self.ss_explained = sum(( self.data['group_mean'] -self.data['overall_mean_x'])**2)
        
        #compute Mean Square Residual
        self.n_groups = len(set(self.data[self.qualitative_variable]))
        self.n_obs = self.data.shape[0]
        self.df_residual = self.n_obs - self.n_groups
        self.ms_residual = self.ss_residual / self.df_residual

        #compute Mean Square Explained
        self.df_explained = self.n_groups - 1
        self.ms_explained = self.ss_explained / self.df_explained

        #compute F-value
        self.f = self.ms_explained / self.ms_residual

        #compute p-value
        self.p_value = 1 - scipy.stats.f.cdf(self.f, self.df_explained, self.df_residual)

