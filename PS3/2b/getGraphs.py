# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:32:02 2017

@author: lu
"""
import random

file = open("kru9.txt", "w")
for i in range(1, 100):
    for j in range(i+1, 101):
        file.write(str(i) + "," + str(j) + "," + str(random.randint(1, 10)) + "\n")

file.close()

file = open("kru7.txt", "w")
for i in range(1, 50):
    for j in range(i+1, 51):
        file.write(str(i) + "," + str(j) + "," + str(random.randint(1, 100)) + "\n")

file.close()