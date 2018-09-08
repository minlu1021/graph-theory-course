Name: Lu Min
mlu821@bu.edu


####################files#######################
## ps2.pdf
   written part

## eu0.txt~eu9.txt
   example: 1,2 means there is an edge between node 1 and 2, and node 1 directs to node 2.
            
   Eulerian examples("eu9.txt" has 1000 nodes as required!)

## non0.txt~non9.txt
   non-Eulerian examples("non9.txt" has 1000 nodes as required!)

## getExamples.py
   I get the 1000 nodes example by this code

## eulerian.py
   Main code for determining whether a digraph is Eulerian

#########how to run my code(in command line)##############

python eulerian.py eu0.txt
(for "eu*.txt", we will get result that these digraphs are Eulerian and its Eulerian circuit)
(we can also change the source node of Eulerian circuit, if you would like to change it.)
// change in eulerian.py in line 145 which is the last line.
// change to(source=1 means change start node to node 1, we can change to any node in digraph):
// print("Eulerian circuit: ", list(eulerian().eulerian_circuit(g, source=1)))

python eulerian.py non0.txt
(for "non*.txt", we will get result that these digraphs are non-Eulerian)