# Tian Xiaoyang
# 26001904581
# week 5 exercise

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animate

#import necessary modules for this program

universe = 10 # set universe size
alive = 1 #set value for living cells
dead = 0 #set value for dead cells
vals = [alive, dead] #values used to switch the cell states "on" and "off"

grid = np.zeros((universe, universe)) #

# oscillator chosen is beaconandtwotails
osci = [
    [1,1,0,0,0,0,0],
    [1,0,0,0,0,0,0],
    [0,0,0,1,0,1,1],
    [0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0],
    [0,0,1,1,1,0,0],
    [0,0,1,0,0,0,0]
]

grid[0:7, 0:7] = osci

#define maze game of life
def animated_universe(framenumber, *args, **kwargs):
    global grid
    global animatedcount 
    newGrid = grid.copy()
    for i in range (universe): # set the rules for cells to become alive or dead
        for j in range(universe): # set the rules for cells to become alive or dead
            total = (grid[i, (j-1)%universe] + 
                     grid[i, (j+1)%universe] +
                     grid[(i-1)%universe, j] + 
                     grid[(i+1)%universe, j] + 
                     grid[(i-1)%universe, (j-1)%universe] + 
                     grid[(i-1)%universe, (j+1)%universe] + 
                     grid[(i+1)%universe, (j-1)%universe] + 
                     grid[(i+1)%universe, (j+1)%universe])/alive
            if grid[i, j] == alive:
                if(total<1) or (total >5): # this dictates that a living cell becomes dead if the total celss around are fewer than 2 ore more than 3
                    newGrid[i, j] = dead
                else:
                    newGrid[i, j] = alive
            else:
                if total == 3:
                    newGrid[i, j] = alive
                else:
                    newGrid[i, j] = dead # this dictates that dead cell becomes alive when total cells around are equal to 3
    
    if (osci==grid[0:7, 0:7]).all():
        print("pattern type is 'beaconeandtwotails' in numpy, too")
    grid = newGrid.copy()
    mat.set_data(grid)
    return mat


if __name__ == "__main__":
    user_choice = input("Choose the game of life pattern you'd like to animae")


fig, ax = plt.subplots()
mat = ax.matshow(grid) #plot the grid 
ani = animate.FuncAnimation(fig, animated_universe, interval = 100, frames=60, repeat=False) #set the interval for different frames at 2000 milliseconds 
plt.show() #render the animation
ani.save('oscillator.gif', writer='imagemagick', fps=60) # save the animation in a gif, of 60 fps
plt.close()