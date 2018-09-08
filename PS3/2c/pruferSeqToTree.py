# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 19:29:49 2017

@author: lu
"""

import sys

# get prufer sequence
file = open(sys.argv[-1],"r")
line = file.readline()
file.close()
s1 = line.replace("[", "")
s2 = s1.replace("]", "")
s = s2.split(",")
prufer = [int(x) for x in s]
n = len(prufer) + 2 # number of nodes in the tree

# get the degree of each node
degree = {}
for i in range(1,n+1):
    degree[i] = 1
for x in prufer:
    degree[x] += 1

# generate tree
tree = {}
for i in range(1,n+1):
    tree[str(i)] = []
index = 0 # index in prufer list
while index<len(prufer):
    for i in range(1,n+1):
        # connect the node of degree 1 with the prufer sequence node
        if degree[i] == 1:
            tree[str(i)].append(prufer[index])
            tree[str(prufer[index])].append(i)
            degree[i] -= 1 # decrease 1  of leaf node to 0
            degree[prufer[index]] -= 1 # decrease 1 of the neighbor of leaf node
            break
    index += 1 # go through prufer sequence list

# connect the last two nodes
two = []
for i in range(1, n+1):
    if degree[i] == 1:
        two.append(i)
tree[str(two[0])].append(two[1])
tree[str(two[1])].append(two[0])
print(tree)
