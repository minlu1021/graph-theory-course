# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:26:12 2017

@author: lu
"""
import sys

parent = {}
rank = {}

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for v in graph['vertices']:
        parent[v] = v
        rank[v] = 0

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        if find(u) != find(v):
            union(u, v)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree


if __name__ == "__main__":
    # get all the nodes in the graph
    file = open(sys.argv[-1], "r")
    lineList = file.readlines()
    file.close()
    
    # add the nodes to list vertices
    vertices = []
    s = ""
    for x in lineList[-1]:
        if x==",":
            break
        s += str(x)       
    for i in range(1, int(s) + 2):
        vertices.append(str(i))

    # add edges with weight    
    edges = []
    for line in lineList:
        s = line.split(",")
        weight = [int(x) for x in s]
        edges.append((weight[2], str(weight[0]), str(weight[1])))
    
    # the minimum spanning tree path
    G = {'vertices': vertices, 'edges': set(edges)}
    print(kruskal(G))
    
    
    