import matplotlib.pyplot as plt
import numpy as np

# x coordniates. a list of number from between -25 to 75
x = np.linspace(-10, 50, num = 750)
# different functions, for y coordinates
y1 = 5 * (x - 20)**2 # assign result from function 1 to all y coordinates
y2 = 50 * np.sin(x) + x**2 + 100# assign result from function 2 to all y coordinates
y3 = 15 * np.sin((x/5)**2) * (75 * np.cos(x/13)) * (3 * np.sin(x/6)) + x**2 + 300# assign result from function 3 to all y coordinates
#plot the graphs
plt.plot(x, y1, color = "red" ) # graph for function 1 is red
plt.plot(x, y2, color = "blue" )# graph for function 2 is blue
plt.plot(x, y3, color = "yellow" ) # graph for function 3 is yellow
plt.show()