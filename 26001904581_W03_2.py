#!/usr/bin/env python
# coding: utf-8
# Tian Xiaoyang 
# 26001904581
# # main code

# In[11]:


import matplotlib.pyplot as plt
import numpy as np
import timeit 

start_time = timeit.default_timer()

n = 10
iteration_number = 10
M = np.zeros([n,n], int)
xvalues = np.linspace(-2, 0.5, n)
yvalues = np.linspace(-1, 1, n)
for u, x in enumerate(xvalues):
    for v, y in enumerate(yvalues):
        z = 0 + 0j
        C = complex(x, y)
        for i in range (iteration_number):
            z = z*z +C
            if abs(z)>2.0:
                M[v,u] = 1
                break
        plt.imshow(M, origin="lower", extent=(-2, 0.5, -1, 1))
        plt.gray()
        plt.show()
        
stop_time = timeit.default_timer()

print("Mandelbrot Set Took" + str (stop_time - start_time)[0:5] + "seconds to run")


# In[5]:


# line resolution is the main factor that affects the time it takes to run the code.
# line resolution has a large influence on running time while iteration number does not seem to have apparant effect.
# for both n = 10, iteration number = 10 took about 17 seconds, while iteration number = 1000 also took about 17 seconds
# for the same iteration number however, iteration_number = 100, n = 10 took about only 17 seconds while n= 100 took more than 20 minutes
# all code running were conducted on Mac book, which was the major reason why it took much longer than expected and necessary to run the code


# In[ ]:




