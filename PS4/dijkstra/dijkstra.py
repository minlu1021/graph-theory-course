# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:03:40 2017

@author: lu
"""

import sys
"""
The format of the graph G is a dictionary.
Key is the node number,
Value is a list of list, and each list is the connected vertex
and the edge weight.
Example:
G = {"1": [[2,7],[3,9],[6,14]], "2": [[1,7],[3,10],[4,15]],
     "3": [[1,9],[2,10],[4,11],[6,2]], "4": [[2,15],[3,11],[5,6]], 
     "5": [[4,6],[6,9]], "6": [[1,14],[3,2],[5,9]]}  
"""

## read files
file = open(sys.argv[-1], "r")
lineList = file.readlines()   
file.close()
# get graph G with weights
G = {}
for line in lineList[:-2]:
    s = line.split(",")
    weight = [int(i) for i in s]
    if str(weight[0]) in G:
        G[str(weight[0])].append([weight[1],weight[2]])
    elif str(weight[0]) not in G:
        G[str(weight[0])] = [[weight[1],weight[2]]]
    if str(weight[1]) in G:
        G[str(weight[1])].append([weight[0],weight[2]])
    elif str(weight[1]) not in G:
        G[str(weight[1])] = [[weight[0],weight[2]]]
# get start and end node
sline = lineList[-2].split(":")
eline = lineList[-1].split(":")
start = int(sline[-1])
end = int(eline[-1])

# Initialize a dictionary for implementing dijkstra algo 
dijk = {}
for i in range(1, len(G)+1):
    # initialize start to every node to inf
    # the value list would have another element: minimum edge weight from wich node
    dijk[i] = [9999999999] 
dijk[start] = [0, start]

# initialize a selected list, representing that the node has been selected as 
# the minimum weigth to start node.
selected = [0 for i in range(len(G)+1)]
selected[0] = -1 # I don't have node 0
selected[start] = 1
for l in G[str(start)]:
    dijk[l[0]] = [l[1], start]

while 0 in selected:
    mini = 9999999999
    for i in range(1, len(G)+1):
        # if this node is selected, it can not compare to other unselected nodes
        if selected[i] != 0:
            continue
        # find the mini weight from start to each node
        elif selected[i] == 0:
            if dijk[i][0] < mini:
                mini = dijk[i][0]
                snode = i
    # snode is the next selected minimum weight node
    selected[snode] = 1
    if 0 not in selected:
        break
    # get weight of neighbors of snode
    for l in G[str(snode)]:
        if (mini + l[1]) < dijk[l[0]][0]:
            dijk[l[0]][0] = mini + l[1]
            if len(dijk[l[0]])==1:
                dijk[l[0]].append(snode)
            else:
                dijk[l[0]][1] = snode
            
# Find the path from end
path = []
node = dijk[end][1]
path.append(end)
path.append(node)
while node!=start:
    node = dijk[node][1]
    path.append(node)
realPath = [i for i in reversed(path)]

print("Start from: ", start)
print("To end: ", end)
print("Path of Dijkstra in graph G: ", realPath)
print("The minimum weight sum from start to end: ", dijk[end][0])


