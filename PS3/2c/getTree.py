# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:55:10 2017

@author: lu
"""

file = open("tree9.txt", "w")
for i in range(1, 98, 2):
    file.write(str(i) + "," + str(i+1) + "\n")
    file.write(str(i) + "," + str(i+2) + "\n")
file.write(str(98) + "," + str(100))
file.close()