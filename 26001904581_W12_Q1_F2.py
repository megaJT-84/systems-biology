# Tian Xiaoyang
# 26001904581

import numpy as np
import matplotlib.pyplot as plt
import random as rdm
import math as m

def errorFunc2(x):
    sum_func2 = sum([50 * m.sin(x[i]) + x[i]**2 + 100 for i in range(len(x))])
    return sum_func2
    # particles with a slower velocity can only travel so far in their spcae, no matter the iterations
    # according to the velocity update function, self.individualVelocity[i] = w * self.individualVelocity[i] + cognitiveVel + socialVel
    # however, constants in the function are all very small values, w = 0.5, c1 = 1, c2 = 2
    # so the change in velocity is not going to change much, and the position of each particle is not gonna change much either

#class for the action of single particles
class individualParticle:

    def __init__(self, x0):
        # initialize variables
        self.individualPosition = []# individual positions as empty list
        self.individualVelocity = []# individual velocities as empty list
        self.individualBestPosition = []# individual best positions as empty list
        self.individualBestError = -1# individual best errors as -1
        self.individualError = -1# individual errors as -1

        for i in range(0, numStartingLocation):
            self.individualVelocity.append(rdm.uniform(-1, 1))# append a randomly picked digit between -1 and 1 to the empty individual velocity list
            self.individualPosition.append(x0[i])# append the digit at the i index position in the x0 array to the empty individual position list

# function for evaluating the current fitness of agents
    def eval(self, costFunc):
        self.individualError = costFunc(self.individualPosition)
        # the current agent position is compared to that of individual best and updated if necessary
        if self.individualError < self.individualBestError or self.individualBestError == -1:
            self.individualBestPosition = self.individualPosition
            self.individualBestError = self.individualError

# update the particle velocity
    def update_vel(self, groupBestPosition):
        w = 2.5 # inertia weight of previous weight
        # the inertia weight can be changed to get a result easier
        c1 = 0.5 # cognitive constant (distance from the individual's known best position)
        # cognitive and social distances can be changed to affect the result
        c2 = 1 # social constant (distance form the group's known best position)
        for i in range(0, numStartingLocation):
            r1 = rdm.random()
            r2 = rdm.random()
            # update cognitive velocity and social velocity
            cognitiveVel = c1 * r1 *(self.individualBestPosition[i] - self.individualPosition[i])
            socialVel = c2 * r2 *(groupBestPosition[i] - self.individualPosition[i])
            self.individualVelocity[i] = w * self.individualVelocity[i] + cognitiveVel + socialVel

    # update the position of each agent based on the velocity updates
    def position_update(self, bounds):
        for i in range(0, numStartingLocation):
            self.individualPosition[i] - self.individualPosition[i] + self.individualVelocity[i] # update the individual position. the new individual postion is the sum of individual position and individual velocity
            if self.individualPosition[i] > bounds[i][1]: # if indi position is large than the bound max, assign the max value to the indi position
                self.individualPosition[i] = bounds[i][1]

            if self.individualPosition[i] < bounds[i][0]:# if indi position is smaller than the bound max, assign the min value to the indi position
                self.individualPosition[i] = bounds[i][0]

#swarm particle optimization function
def particleSwarmOP(costFunc, x0, bounds, num_particles, maxiter):
        # initilize the swarm
        global numStartingLocation
        numStartingLocation = len(x0)
        print(numStartingLocation)
        bestGroupError = -1
        groupBestPosition = [] # empty list for best group positions
        swarm = [] # empty swarm

        for i in range(0, num_particles):
            swarm.append(individualParticle(x0))
# loop to start the optimization process
        for i in range(0, maxiter):# evaluate agent's fitness
            for j in range(0, num_particles):
                swarm[j].eval(costFunc)
# step to find out the agent with the best position(minimum error) in the swarm
                if swarm[j].individualError < bestGroupError or bestGroupError == -1:
                    groupBestPosition = list(swarm[j].individualPosition)
                    bestGroupError = float(swarm[j].individualError)
# update velocities and positions inside the swarm
            for j in range(0, num_particles):
                swarm[j].update_vel(groupBestPosition)
                swarm[j].position_update(bounds)     
# print the final result with error
        print("after running the swarm of computer agents, the group\'s best position is " + 
        str(groupBestPosition) + "\n with  an error of " + str(bestGroupError))
#initialize variables
initialStartingPosition = [-15, 15]
minMaxBounds = [(-500, 500), (-500, 500)]
particleSwarmOP(errorFunc2, initialStartingPosition, minMaxBounds, num_particles = 150, maxiter = 500)

if __name__ == "__main__":
    plt.show()
