import numpy as np
import matplotlib.pyplot as plt
import string, random, math

# this function turns a decimal integer input from user into a binary code for the rule set
user_int=int(input('please enter the no. in decimal format: '))
x=user_int
k=[]
while ( user_int>0):
    rem=int(float(user_int%2))
    k.append(rem)
    user_int=(user_int-rem)/2
k.append(0)
string=""
for j in k[::-1]:
    string=string+str(j)
print('The binary no. for %d is %s'%(x, string))