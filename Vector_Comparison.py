from words1 import v1
from words2 import v2
from words3 import v3
from words4 import v4
from words5 import v5
from words6 import v6
from words7 import v7
from words8 import v8
from words9 import v9
from words10 import v10

All_matrices = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]

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
            Matrix.append('v{0}v{1}:{2}'.format(i+1,j+1,dot_prod(Doc1[i],Doc2[j])))
            i=i+1


In_general(All_matrices,All_matrices)
print dot_prod(v9,v10)
print Matrix
print max(Matrix)