# Tian Xiaoyang
# 26001904581
#

import numpy as np
import random
import string

# define variables
target = 'Tian Xiaoyang'
dnalength = len(target)
population_size = 20
generation = 50
mutateChance = 100

# define function that generates a random character, a gene in this case
def randomGene():
    rand_g = random.choice(string.printable)
    return rand_g

# define function that sets up the initial population size, etc
def inipopulation():
    inipop = []
    for i in range (population_size): # add a randomly generated string to the inipop array, initially empty
        inipop.append(''.join(random.choice(string.printable) for i in range(dnalength))) # initilize the population with randomly generated DNA
    return inipop #return output of the function, initial population

# define function that sets up the fitness function
def Fit_Func1(competing_DNA):
    total = 0
    for i in range(len(competing_DNA)):
        fitness = abs(((ord(competing_DNA[i]) - ord(target[i])))) # the fitness value is the absolute value of difference between the target DNA and the competing DNA at this position in both DNAs
        total = (total + fitness) # final fitness value = 1 divided by total sum of all fitness values
    return total #return output of the function, fitness


def Fit_Func2(competing_DNA):
    total = 0
    for i in range(len(competing_DNA)):
        fitness = (ord(competing_DNA[i]) - ord(target[i]))**2 # the fitness value is the square of difference between the target DNA and the competing DNA at this position in both DNAs
        total = total + fitness # final fitness value = 1 divided by total sum of all fitness values
    return total

def Fit_Func3(competing_DNA):
    total = 0
    for i in range(len(competing_DNA)):
        fitness = (ord(target[i])- ord(competing_DNA[i]))*1# if the value of character in target dna at this position is different from the value of character in competing dna at this position, for every time there's a difference, 1 is added
        total = total + fitness # final fitness value = 1 divided by total sum of all fitness values
    return total

# define function that generates and returns the string that is mutated
def mutation(competing_DNA, mutation_ratio):
    mutatedDNA = '' # initilizae the mutataed DNA
    random_gene = randomGene() # sets up the random gene that will replace a gene in the DNA
    index_DNA = random.randint(0, len(competing_DNA)) #pick a random integer that falls within the length of the competing DNA
    mutate_prob= random.randint(0, mutation_ratio) # the chance of mutation is 1/100
    if mutate_prob == 1: # set up the mutation process that has a 1/100 chance to happen
        competing_DNA[index_DNA] = random_gene # assign the randomly generated gene from random gene function to the index position in this DNA
        mutatedDNA = competing_DNA #assign the new competing DNA to variable mutated DNA
    return mutatedDNA #return output of the function, the mutated DNA

# define function that recombines 2 strings to form a new one, a new DNA
def recombo(compete_DNA1, compete_DNA2):
    dna_index = random.randint(0, len(compete_DNA2)) # sets up the index as a random integer that falls within length of DNA2, which will be hsorter
    DNA1 = compete_DNA1[0:dna_index] + compete_DNA2[dna_index:] # cut competing DNA1 and DNA2 into 2 halves, combine first half of DNA1 with second half of DNA2 
    DNA2 = compete_DNA2[0:dna_index] + compete_DNA1[dna_index:] # cut competing DNA1 and DNA2 into 2 halves, combine first half of DNA2 with second half of DNA1
    return DNA1, DNA2 #return output of the function, recombined DNAs

# define function that sets up the weight for DNA choice
def weightedDNAchoice(competeDNAfitpair):
    probs = [competeDNAfitpair[i][1] for i in range(len(competeDNAfitpair))]
    probs = np.array(probs)
    probs /= probs.sum()
    return competeDNAfitpair [np.random.choice(len(competeDNAfitpair), 1, p= probs)[0]][0] #return output of the function

currentpop = inipopulation()
for i in range(generation):
    lastfitarray = []
    for k in currentpop:
        lastfitarray.append(Fit_Func3(k)) # print generation number, and the fittest string for the current generation
    print("the fittest DNA for generation", i, "is ---", currentpop[lastfitarray.index(min(lastfitarray))],
    "--- with penalty", min(lastfitarray))
#return a new population with each one's fittest
population_weighted = []
for individual in currentpop:
    indipenalty = Fit_Func3(individual) # use the value "individual" for fitness function
    if indipenalty == 0:
        DNAfitpair = (individual, 1.0)
    else:
        DNAfitpair = (individual, 1.0/indipenalty)
    population_weighted.append(DNAfitpair)

    # reset population and repopulate with randomly selected, mutated and recombined DNAs
currentpop = []
for m in range(int(population_size/2)):
    # random select DNA, weighted by the fitness function
    fittestDNA1 = weightedDNAchoice(population_weighted)
    fittestDNA2 = weightedDNAchoice(population_weighted)
    # recombination of DNAs
    fittestDNA1, fittestDNA2 = recombo(fittestDNA1, fittestDNA2)
    # mutation has a chance of 1/mutatechance
    fittestDNA1 = mutation(fittestDNA1, mutateChance)
    fittestDNA2 = mutation(fittestDNA2, mutateChance)
    #combine DNAs and form a new population for the next iteration
    currentpop.append(fittestDNA1)
    currentpop.append(fittestDNA2)

# create an array value for each DNA in the population
lastfitarray = []
for g in currentpop:
    lastfitarray.append(Fit_Func3(g))
print("fittest string at ", generation, "is: ", currentpop[lastfitarray.index(min(lastfitarray))])
