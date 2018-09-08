# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:44:56 2017

@author: lu
"""

from collections import deque
import networkx
import sys

class bipartite(object):    
    def uncolored(self, node):
        """
        Determine if this node is colored
        uncolored--return True
        colored----return False
        
        """
        if node not in self.colorings['black'] and node not in self.colorings['white']:
            return True
        else:
            return False

    def changeColor(self, node):
        """
        Change the color of node
        if it is black, change to white
        if it is white, change to black
        """
        if node in self.colorings['black']:
            return 'white'
        elif node in self.colorings['white']:
            return 'black'
            
    def canColor(self, node, color):
        """
        Determine if this node can be colored with given color
        can be colored with color--True
        else-----------------------False
        """
        neighbors = self.G[node].keys() # get all neighbors of the node
        return all([neighbor not in self.colorings[color] for neighbor in neighbors])


    def isBipartite(self, G):
        """
        If graph G is partite--True
        If G is not partite----False
        """
        self.G = G 
        
        self.colorings = {'black': set(), 'white': set()}
        start = G.nodes()[0] # the first node as initial node to start
        self.colorings['black'].add(start) # Once got the node, color black
        q = deque([start])
        while q:
            n = q.pop()
            next_color = self.changeColor(n)
            # get the neighbors who are not colored
            uncolored_neighbors = []
            for neighbor in G[n].keys():
                if self.uncolored(neighbor):
                    uncolored_neighbors.append(neighbor)

            for neighbor in uncolored_neighbors:
                # if this neighbor can be colored with given node,
                # just color it and add this neighbor to q
                if self.canColor(neighbor, next_color):
                    self.colorings[next_color].add(neighbor)
                    q.append(neighbor)
                # if can not be colored, then this graph is non-bipartite
                else:
                    return False
        # if not false, then G is partite
        return True

if __name__ == '__main__':
    """Main Part"""    
    # get the nodes and edges from txt file
    file = open(sys.argv[-1],"r")
    lineList = file.readlines()   
    file.close()
    s = ""
    for x in lineList[-1]:
        if x==",":
            break
        s += str(x)
    n = int(s) +1 # number of nodes in G
    G = networkx.Graph()
    ## add nodes to the graph G
    G.add_nodes_from([node for node in range(1, n+1)])
    ## get the edges between nodes
    edges = []
    for line in lineList:
        s = line.split(",")
        relation = [int(x) for x in s]
        # when they have edges, i append the connected to node to edges list.
        if relation[-1]==1:
            edges.append((relation[0],relation[1]))
    ## add edges to the graph G
    G.add_edges_from(edges)        
    ## get the result       
    print('Whether graph G is bipartite:', bipartite().isBipartite(G))