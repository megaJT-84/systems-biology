from typing import MutableSequence
import numpy as np
import string
import random

def mutateString(DNA):
    dna_char = random.choice(string.ascii_letters + string.punctuation + string.digits)
    dna_index = random.randint(0, len(DNA))
    dna_int = random.randint(1,10)
    if dna_int == 1:
        DNA = DNA[:dna_index] + dna_char + DNA[dna_index+1:]
    return DNA
dna = mutateString(input("enter initial DNA string: "))

compete_DNA = mutateString(dna)

target_DNA = "Tian Xiaoyang_!9017"

def fitness1(x, y, n):
    fit_val = 0
    x = compete_DNA
    y = target_DNA
    n = len(target_DNA)
    for i in range (n):
       fit_val= x[i] - y[i]
    return fit_val

def fitness2(x, y, n):
    x = compete_DNA
    y = target_DNA
    n = len(target_DNA)
    for i in range (n):
        fit_val2= (x[i] - y)[i]*(x[i] - y[i])
    return fit_val2

def fitness3(x, y, n):
    x = compete_DNA
    y = target_DNA
    n = len(target_DNA)
    for i in range (n):
        if x[i] != y[i]:
            fit_val3 = 1
    return fit_val3

def fitness_():
    x = compete_DNA
    y = target_DNA
    n =len(target_DNA)
    fit_val = 0
    for i in range(n):
        if x [i] != y[i]:
            fit_val += 1
    return fit_val

def fitness_():
    x = compete_DNA
    y = target_DNA
    n =len(target_DNA)
    fit_val = 0
    for i in range(n):
        if x [i] == y[i]:
            fit_val += 1
    return fit_val

def fitness_():
    x = compete_DNA
    y = target_DNA
    n =len(target_DNA)
    fit_val = 0
    if len(y) == n:
        fit_val = 1
    return fit_val

dna = mutateString(input("enter initial DNA string: "))

print("mutated DNA: ", dna)
