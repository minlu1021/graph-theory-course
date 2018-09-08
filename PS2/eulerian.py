# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:42:04 2017

@author: lu
"""

import networkx
from operator import itemgetter
import sys

class eulerian(object):
    def is_eulerian(self, G):
        """
        Return True if G is an Eulerian graph, False otherwise.
        """
        if G.is_directed():
            # Every node must have equal in degree and out degree
            for n in G.nodes_iter():
                if G.in_degree(n) != G.out_degree(n):
                   return False
            # Must be strongly connected
            if not networkx.is_strongly_connected(G):
                return False
        else:
            # An undirected Eulerian graph has no vertices of odd degrees
            for v,d in G.degree_iter():
                if d % 2 != 0:
                    return False
            # Must be connected
            if not networkx.is_connected(G):
                return False
        return True
    
    def eulerian_circuit(self, G, source=None):
        """
        Return the edges of an Eulerian circuit in G.
        Result contains the path.
        If we define the source node, the path will start from that node.
        """
        if not self.is_eulerian(G):
            print("This digraph is not Eulerian. It does not have Eulerian circuit!")
            return
        # Copy graph structure (not attributes)
        g = G.__class__(G) 

        # Set starting node
        if source is None:
            v = next(g.nodes_iter())
        else:
            v = source
    
        if g.is_directed():
            degree = g.in_degree
            edges = g.in_edges_iter
            get_vertex = itemgetter(0)
        else:
            degree = g.degree
            edges = g.edges_iter
            get_vertex = itemgetter(1)

        vertex_stack = [v]
        last_vertex = None
        while vertex_stack:
            current_vertex = vertex_stack[-1]
            if degree(current_vertex) == 0:
                if last_vertex is not None:
                    yield (last_vertex, current_vertex)
                last_vertex = current_vertex
                vertex_stack.pop()
            else:
                random_edge = next(edges(current_vertex))
                vertex_stack.append(get_vertex(random_edge))
                g.remove_edge(*random_edge)
        
    def de_bruijn(self, k, n):   
        """
        de Bruijn sequence for alphabet k
        and subsequences of length n.
        """
        try:
            alphabet = list(map(str, range(k)))
    
        except (ValueError, TypeError):
            alphabet = k
            k = len(k)
    
        a = [0] * k * n
        sequence = []
    
        def db(t, p):
            if t > n:
                if n % p == 0:
                    sequence.extend(a[1:p + 1])
            else:
                a[t] = a[t - p]
                db(t + 1, p)
                for j in range(a[t - p] + 1, k):
                    a[t] = j
                    db(t + 1, t)
        db(1, 1)
        return "".join(alphabet[i] for i in sequence)
        

if __name__ == '__main__':
    """
    Main Part
    """
    """
    test a simple digraph G
    """
#    G = networkx.DiGraph({0:[3], 1:[2], 2:[3], 3:[0, 1]})
#    print("G is eulerian: ", eulerian().is_eulerian(G))
#    print("Eulerian circuit: ", list(eulerian().eulerian_circuit(G)))    
#    print("De Bruijin sequences of length 5: ")
#    print(eulerian().de_bruijn(2,5))
    
    # read file
    file = open(sys.argv[-1], "r")
    lineList = file.readlines()
    file.close()
    
    # get the nodes and nodes they oriented
    dic = {}
    s = ""
    for x in lineList[-1]:
        if x==",":
            break
        s += str(x)
    n = int(s) +1 # number of nodes in G
    
    for i in range(n):
        for line in lineList:
            s = line.split(",")
            nodes = [int(x) for x in s]
            if (nodes[0] == i):
                if i in dic:
                    dic[i].append(nodes[1])
                if i not in dic:
                    dic[i] = [nodes[1]]
                    
    # Digraph T is read from the txt files
    g = networkx.DiGraph(dic)
    print("g is eulerian: ", eulerian().is_eulerian(g))
    print("Eulerian circuit: ", list(eulerian().eulerian_circuit(g)))    
    
    
    
    
    
    
    
    
    
    
    