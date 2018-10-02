X={'a':5,'b':3,'c':2,'e':2}
Y={'b':5,'e':4,'f':5}
Z ={'l':6,'a':7,'c':1,'f':9,'r':4}
V={'k': 9,'o':4, 'b':4,'e':2}
O = {'i':2,'k':5,'o':3}

All_matrices = [X,Y,Z,V,O]

import math

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

Matrix = []
def In_general(Doc1,Doc2):
    for j,val in enumerate(Doc2):
        i=0
        while i < j:
            Matrix.append(dot_prod(Doc1[i],Doc2[j]))
            i=i+1


In_general(All_matrices,All_matrices)

print Matrix
print dot_prod(X,Y)
print dot_prod(X,Z)
print dot_prod(X,V)
print dot_prod(X,O)
print ('---------')
print dot_prod(Y,Z)
print dot_prod(Y,V)
print dot_prod(Y,O)
print ('---------')
print dot_prod(Z,V)
print dot_prod(Z,O)
print ('---------')
print dot_prod(V,O)