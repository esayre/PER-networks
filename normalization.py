import math
import numpy as np
from words1 import A

D=[]
def output_dictionary_values(my_dict):
    for key, value in my_dict.items():
        D.append(value)

def magnitude(v):
    return math.sqrt(sum(v[i]*v[i] for i in range(len(v))))

def normalize(v):
    return(1/magnitude(v))*np.array(v)

"""def dot_product(v1,v2):
    for key1,value1 in v1.items():
            if key1 in v2:
                v3.append(value1*v2.values())
            else:
                v3.append(value1*0)
dot_product(A,B)"""

#main
output_dictionary_values(A)
magnitude(D)
L=normalize(D)

print D
print magnitude(D)
print L