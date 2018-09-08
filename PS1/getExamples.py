# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:23:56 2017

@author: lu
"""

file = open("bi9.txt", "w")
for i in range(1,1000):
    for j in range(i+1,1001):
        if j==i+1 and i%2==1:
            file.write(str(i))
            file.write(",")
            file.write(str(j))
            file.write(",1\n")
        else:
            file.write(str(i))
            file.write(",")
            file.write(str(j))
            file.write(",0\n")

file.close()