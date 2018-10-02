from __future__ import division
from FinalCode2 import list_of_list_of_clusters
import math

'''--------------------------------------------------------------------------'''

def cluster_comparison(list1,list2):
    UNION = len(list(set().union(list1,list2)))
    INTERSECTION = len(list(set(list1) & set(list2)))
    ratio = INTERSECTION/UNION
    return ratio

P = []
def iteration(list_of_clusters1,list_of_clusters2):
    j=0
    for cluster in list_of_clusters1:
        for i in range(0, len(list_of_clusters2)):
            ratio_result = cluster_comparison(cluster, list_of_clusters2[i])
            P.append(ratio_result)
            '''print("The ratio between clusters {} and {} is {}".format(j, i, ratio_result))
            print("\n")'''
        j=j+1
    l=0
    for k in P:
        if k > 0.75:
            l=l+1
    O = l/math.sqrt(len(P))
    '''print ("H = {}".format(l))
    print ("sqrt of H+L+M = {}".format(math.sqrt(len(P))))'''
    print ("Ratio is {}".format(O))

def mean(lst):
    """calculates mean"""
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return (sum / len(lst))

def stddev(lst):
    """calculates standard deviation"""
    sum = 0
    mn = mean(lst)
    for i in range(len(lst)):
        sum += pow((lst[i]-mn), 2)
    return math.sqrt(sum/(len(lst)-1))

'''--------------------------------------------------------------------------'''

iteration(list_of_list_of_clusters[0], list_of_list_of_clusters[1])

U=[]
for element in P:
    if element > 0.8:
        U.append(element)

print ("Mean:{}".format(mean(U)))
print ("Standart Deviation:{}".format(stddev(U)))
