import string
import numpy as np
import random

target = "Tian Xiaoyang"
dnalength  = len(target)
populationsize = 20
generations = 5000
mutationchance = 100

def randomgene():
    rando_gene = random.choice(string.printable)
    return rando_gene

def inipopulation():
    initpop = []
    for i in range (populationsize):
        initpop.append(''.join(random.choice(string.printable) for i in range(dnalength)))

    return initpop

def fitness(competedna):
    fitness = 0
    return fitness

def mutation(competedna, mutationratio):
    mutateddna = 

    return muateddna