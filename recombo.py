import random
import string
import numpy as np

def mutateString(DNA1, DNA2):
    dna_index = random.randint(0, len(DNA2))
    DNA1 = DNA1[0:dna_index] + DNA2[dna_index:]
    DNA2 = DNA2[0:dna_index] + DNA1[dna_index:]
    return DNA1, DNA2
    
compete_DNA = mutateString()
target_DNA = "Tian Xiaoyang_!9017"

def fitness1(x, y, n):
    x = compete_DNA
    y = target_DNA
    n = len(target_DNA)
    for i in range (n):
        fit_val = x - y
        return fit_val

def fitness2(x, y, n):
    x = compete_DNA
    y = target_DNA
    n = len(target_DNA)
    for i in range (n):
        fit_val = (x - y)*(x - y)
    return fit_val

def fitness3(x, y, n):
    x = compete_DNA
    y = target_DNA
    n = len(target_DNA)
    for i in range (n):
        if x != y:
            fit_val = 1
    return fit_val

dna = mutateString(input("enter DNA 1: "), input("enter DNA 2: "))

print("mutated DNA: ", dna)
