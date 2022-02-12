import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# total population
N = 10000
#number of infected at time t=0
I0 = 55
#number of removed (due to immunity or death) at t=0
R0 = 0
#all susceptible individuals at t=0
S0 = N - I0 - R0
#contact rate
beta = 0.3
# infectious period (inverse of number of days) or recovery time
gamma = float(3/7)
# time from day 0 to day 100 in 1-hour increments
t = np.linspace(0, 100, num=2400)

# differential equations os SIR model
def SIRmodel(compartmentValues, t, N, beta, gamma):
    S, I, R = compartmentValues
    dSdt = -beta* S * I / N
    dIdt = beta * S * I / N - gamma*I
    dRdt = gamma*I
    return dSdt, dIdt, dRdt

compartmentValues0 = S0, I0, R0
#integrate SIR equations over time grid
# then return numerical solutions
SIRmodelSolve = odeint(SIRmodel, compartmentValues0, t, args = (N, beta, gamma))
S, I, R = SIRmodelSolve.T

# white background
fig = plt.figure(facecolor = "w")
# 1*1 grid with one plot
ax = fig.add_subplot(1, 1, 1, facecolor = '#eeeeee', axisbelow = True)
#plot the data for three separate curves: S(t)
ax.plot(t, S/N, "b", alpha = 0.2, lw = 1, label = "susceptible")
ax.plot(t, I/N, "r", lw = 2, label = "infected")
ax.plot(t, R/N, "g", alpha = 0.2, lw = 1, label = "removed")
# axes labeling
ax.set_xlabel("time, in days")
ax.set_ylabel("individuals (in " + str(N) + "s)")
#print the graph legends
ax.legend()
plt.show()