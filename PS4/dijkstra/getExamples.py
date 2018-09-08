# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 19:01:06 2017

@author: lu
"""
import random
#file = open("dij8.txt", "w")
#for i in range(1,100):
#    for j in range(i+1,101):
#        file.write(str(i)+","+str(j)+","+str(random.randint(1,100))+"\n")
#file.write("start:"+str(random.randint(1,100))+"\n")
#file.write("end:"+str(random.randint(1,100)))
#file.close()

file = open("dij9.txt", "w")
for i in range(1,100):
    if (i%3 == 1):
        file.write(str(i)+","+str(i+1)+","+str(random.randint(1,100))+"\n")
        file.write(str(i)+","+str(i+2)+","+str(random.randint(1,100))+"\n")
        file.write(str(i)+","+str(i+3)+","+str(random.randint(50,100))+"\n")
    elif (i%3 == 0):
        file.write(str(i)+","+str(i+1)+","+str(random.randint(1,100))+"\n")
    elif (i%3 == 2):
        file.write(str(i)+","+str(i+2)+","+str(random.randint(1,100))+"\n")
file.write("start:"+str(1)+"\n")
file.write("end:"+str(100))
file.close()