Name: Lu Min
mlu821@bu.edu


####################files#######################
## ps1.pdf
   written part

## bi0.txt~bi9.txt
   example: 1,2,1 means there is an edge between node 1 and 2
            1,3,0 means there is no edge between node 1 and 2
   bipartite examples("bi9.txt" has 1000 nodes as required!)

## non0.txt~non9.txt
   non-bipartite examples("non9.txt" has 1000 nodes as required!)

## getExamples.py
   I get the 1000 nodes example by this code, no need in determining bipartite

## bipartite.py
   Main code for determining whether a graph is bipartite

#########how to run my code(in command line)##############

python bipartite.py bi0.txt
(for "bi*.txt", we will get result that these graphs are bipartite)

python bipartite.py non0.txt
(for "non*.txt", we will get result that these graphs are non-bipartite)