#!/usr/bin/env python
# coding: utf-8
# Tian Xiaoyang
# 26001904581
# # main code

# In[4]:


import matplotlib.pyplot as plt
import numpy as np
import timeit 

start_time = timeit.default_timer()

n = 100
iteration_number = 100
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


# In[3]:
# due to hardware reasons, n was changed from 1000 to 100 to decrease running time.


