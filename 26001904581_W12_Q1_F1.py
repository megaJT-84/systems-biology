import numpy as np
import matplotlib.pyplot as plt
import random as rdm
import math as m

def errorFunc(x): # define different math functions to calculate the errors
    sum_func1 = sum([5 * (x[i] - 20)**2 for i in range (len(x))])
    # the expected minimum would be 0
    # in order to get zero based on function 1
    # for all 5 * (x[i] - 20)**2, x[i] must be 20, then 5 * (x[i] - 20)**2 would be 0    
    return sum_func1

#class for the action of single particles
class individualParticle:

    def __init__(self, x0):
        # initialize variables
        self.individualPosition = [] # individual positions as empty list
        self.individualVelocity = [] # individual velocities as empty list
        self.individualBestPosition = [] # individual best positions as empty list
        self.individualBestError = -1 # individual best errors as -1
        self.individualError = -1 # individual errors as -1

        for i in range(0, numStartingLocation):
            self.individualVelocity.append(rdm.uniform(-1, 1)) # append a randomly picked digit between -1 and 1 to the empty individual velocity list
            self.individualPosition.append(x0[i]) # append the digit at the i index position in the x0 array to the empty individual position list

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
        c1 = 1 # cognitive constant (distance from the individual's known best position)
        c2 = 2 # social constant (distance form the group's known best position)
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
        for i in range(0, maxiter):
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
        return groupBestPosition, bestGroupError

#initialize variables
initialStartingPosition = [-15, 15]
minMaxBounds = [(-2500, 2500), (-2500, 2500)]
particleSwarmOP(errorFunc, initialStartingPosition, minMaxBounds, num_particles = 150, maxiter = 500)

if __name__ == "__main__":
    plt.show()
