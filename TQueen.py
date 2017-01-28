# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 11:33:06 2017

@author: re
"""

import random as rnd

class TPole():
    def __init__(self, N):
        self.N = N
        self.Pos = list()
        for n in range(self.N):
            self.Pos.append(n)
            
    def Mix(self):
        Pos = list()
        for p in self.Pos:
            Pos.append(p)
            
        i = 0
        j = 0
        while i == j:
            i = rnd.randint(0, self.N - 1)
            j = rnd.randint(0, self.N - 1)
            
        a = Pos[i]
        Pos[i] = Pos[j]
        Pos[j] = a
    
        return Pos
        
    def Calc(self, Pos):
        res = 0
        
        for n in range(self.N):
            k = n - 1
            while k >= 0:
                if Pos[k] == (Pos[n] + (n - k)):
                    res = res + 1

                if Pos[k] == (Pos[n] - (n - k)):
                    res = res + 1
                k = k - 1

            k = n + 1
            while k < self.N:
                if Pos[k] == (Pos[n] + (k - n)):
                    res = res + 1

                if Pos[k] == (Pos[n] - (k - n)):
                    res = res + 1
                k = k + 1
                
        return res

    def CalcSelf(self):
        return self.Calc(self.Pos)
    
    def Change(self, Pos):
        self.Pos = Pos