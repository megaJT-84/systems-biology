import numpy as np
import random
import string

from numpy.ma.core import append

dnalength = 13
for i in range (dnalength):
    random_string = []
    randdo = random_string.append(''.join(random.choices(string.printable) for i in range (dnalength)))
    print(randdo)