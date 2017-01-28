# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 11:32:36 2017

@author: re
"""

import matplotlib.pyplot as plt

import TQueen

import TRun

Pole = TQueen.TPole(20)

Run = TRun.TRun(Pole)

Curs = list()

for n in range(1000):
    cur = Run.Run()
    print(cur)
    Curs.append(cur)
    
    if cur == 0:
        print(Pole.Pos)
        break
    
plt.figure(1)
plt.plot(Curs)
plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Solution")
#plt.axis(ymin = 0, ymax = 1050, xmax = 28)
plt.show()
    
    
