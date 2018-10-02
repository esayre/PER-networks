X={'a':5,'b':3,'c':2,'e':2}
Y={'b':5,'e':4,'f':5}
Z ={'l':6,'a':7,'c':1,'f':9,'r':4}
V={'k': 9,'o':4, 'b':4,'e':2}
O = {'i':2,'k':5,'o':3}

All_matrices = [X,Y,Z,V,O]

import math

from word import L
from words import A

def magnitude (v1):
    mag = 0
    for value in v1.values():
        mag += value**2
    scalar = math.sqrt(mag)
    return scalar

def dot_prod(v1,v2):
    dot = 0
    for key in v1.keys():
        if key in v2.keys():
            dot += (v1[key]/magnitude(v1))* (v2[key]/magnitude(v2))
    return dot

print magnitude(X)
print magnitude(Y)
print dot_prod(X,Y)