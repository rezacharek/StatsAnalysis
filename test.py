import regression as reg
import numpy as np
from scipy import stats
from termcolor import colored
i= 0
j = 50
m =500
x = np.linspace(0, j, m)
beta1 = 5
beta0 = 3

# y = beta1 * x + beta0*np.repeat(1,m) + np.random.normal(0,0,m)
# print(beta0*np.repeat(1,25))
# plt.plot(x,y)
# [beta00,beta11] = linear_egression(x,y,"LeastSquares")
# print(beta00)
# y2 = beta11 * x + beta00*np.repeat(1,100) 
# plt.plot(x,y2, color="red")
# plt.show()

# model = reg.linear_regression(x,y)
# model.plot()

# model.info()

# print(model.confidence_interval())

# x = [1,2,3,4,5,6]
# y = [1,2,3,4,5,6]


# x_1 = np.array([1,2,3])
# x_2 = np.array([0,4,0])
# x_3 = np.array([1,4,0])
# x_4 = np.array([1,-2,3])
# x = np.array([x_1,x_2,x_3,x_4])
# beta = np.array([2,3,7])

# y = np.dot(x,beta) + np.repeat(1,4) 
# print(colored(y,"magenta"))

# model = reg.multiple_linear_regression(x,y)
# print(model.info())
# model.info()
# [beta_zero,beta_one] = linear_egression(x,y,"LeastSquares")
# print(beta_zero)
# print(beta_one)
# print("Variances")
# print(statistics.variance(x))
# print(statistics.variance(y))\
# print(stats.t.ppf(1-0.025, 999))
