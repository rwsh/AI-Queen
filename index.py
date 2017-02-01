# -*- coding: utf-8 -*-
"""
AI.Lector.ru

Автор: Р.В. Шамин
"""

import matplotlib.pyplot as plt

import TQueen

import TRun

Pole = TQueen.TPole(8) # размерность доски

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
plt.show()
    
    
