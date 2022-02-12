from typing import MutableSequence
import numpy as np
import string
import random

def mutateString(DNA):
    letter_punc = string.ascii_letters + string.punctuation + string.digits
    dna_str = (''.join(random.choice(letter_punc)for i in range(len(DNA))))
    dna_int = random.randint(1,10)
    for i in range (len(DNA)):
        if dna_int == 1:
            DNA = dna_str.replace(DNA, dna_str)
            print(DNA)
    return DNA

for i in range (random.randint(0,100)):
    dna = mutateString(input("enter initial DNA string: "))
    print("mutated DNA: ", dna)
