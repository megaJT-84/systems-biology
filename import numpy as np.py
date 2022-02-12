import numpy as np
from scipy.stats import logistic
import math
import matplotlib.pyplot as plt
# Method using numpy
x = 0

def sigmoidA(x):
    return 1 / (1 + np.exp(-x))
# Method using scipy  (Cumulative Distribution Function)
logistic.cdf(x)
# Method using math
def sigmoidB(x):
    return 1 / (1 + math.exp(-x))
    
plt.show()
