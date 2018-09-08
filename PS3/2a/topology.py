# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:19:59 2017

@author: lu
"""
import itertools

X = [1,2,3,4]
# All the subsets from X
sets = []
def findsubsets(S,m):
    return set(itertools.combinations(S, m))
    
for i in range(5):
    subsets = findsubsets(X, i)
    for subset in subsets:
        sets.append(list(subset))

# Get all possible combinations
topology = []
for i in range(3,17):
    combinations = itertools.combinations(sets, i)
    for combination in combinations:
        topology.append(list(combination))

# remove combinations without empty set and itself
res = []
for t in topology:
    if [] in t and X in t:
        res.append(t)
res.append([[],[1,2,3,4]]) # empty set and itself is a topology

# Intersection of two subsets must also be in the topology set
# Union of two subsets must also be in the topology set
for t in res[:]:
    length = len(t)
    for i in range(length-1):
        for j in range(i+1, length):
            set1 = t[i]
            set2 = t[j]
            # Intersection
            inter = list(set(set1) & set(set2))
            # Union
            union = list(set(set1) | set(set2))
            if inter not in t or union not in t:
                if t in res:
                    res.remove(t)

# output to txt file
file = open("outcome.txt", "w")
file.write("The total number of topologies: " + str(len(res)) + "\n")
for topology in res:
    file.write(str(topology) + "\n")
file.close()
    




 