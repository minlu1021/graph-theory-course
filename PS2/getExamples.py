# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:42:31 2017

@author: lu
"""

file = open("eu9.txt","w")
for i in range(999):
    file.write(str(i) + "," + str(i+1) + "\n")
file.write("999,0")
file.close()