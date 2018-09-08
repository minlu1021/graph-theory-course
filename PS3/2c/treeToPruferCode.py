# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:26:11 2017

@author: lu
"""

import sys

# read tree
file = open(sys.argv[-1], "r")
lineList = file.readlines()
file.close()

tree = {}
for line in lineList:
    s = line.split(",")
    edges = [int(x) for x in s]
    key = str(edges[0])
    value = edges[1]
    if key not in tree:
        tree[key] = []
    tree[key].append(value)
    if str(value) not in tree:
        tree[str(value)] = []
    tree[str(value)].append(int(key))  

n = len(tree) # number of nodes in the tree
prufer = [] # initialize prufer code

# the length of prufer code is n-2, so need to leave 2 nodes
while n > 2:
    for i in range(1,len(tree)+1):
        # if it is the leaf node, add its neighbor
        if len(tree[str(i)])==1 :
            pru = tree[str(i)][0]
            prufer.append(pru)
            tree[str(i)].remove(pru) # remove added neighbor in leaf node list
            if i in tree[str(pru)]:
                tree[str(pru)].remove(i) # remove previous leaf node in the neighbor list
            break
    n -=1
print(prufer)


    
    