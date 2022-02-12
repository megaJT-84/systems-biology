#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate


# In[49]:


universe = 50
alive = 1
dead = 0
vals = [alive, dead]
grid = np.random.choice(vals, universe*universe, p = [0.1, 0.9]).reshape(universe, universe)

def animated_universe(framenumber, *args, **kwargs):
    global grid
    global animatedcount
    newGrid = grid.copy()
    for i in range (universe):
        for j in range(universe):
            total = (grid[i, (j-1)%universe] + 
                     grid[i, (j+1)%universe] +
                     grid[(i-1)%universe, j] + 
                     grid[(i+1)%universe, j] + 
                    grid[(i-1)%universe, (j-1)%universe] + 
                    grid[(i-1)%universe, (j+1)%universe] + 
                    grid[(i+1)%universe, (j-1)%universe] + 
                    grid[(i+1)%universe, (j+1)%universe])/alive
            if grid[i, j] == alive:
                if(total<2) or (total >3):
                    newGrid[i, j] = dead
            else:
                if total == 3:
                    newGrid[i, j] = alive
    grid = newGrid.copy()
    mat.set_data(grid)
    return mat
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animate.FuncAnimation(fig, animated_universe, interval = 3)
plt.show()
#ani.save('animation.gif', writer = 'imagemagick', fps = 30)


# In[45]:


# when alive and dead dont change, alive = 1, dead = 0. universe size is the only value that changes
# universe size was experimented to reach a highest value of 750, and a lowest value of 4
# 


# In[ ]:




