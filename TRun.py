# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 15:48:00 2017

@author: re
"""

import random as rnd

import numpy as np

class TRun():
    def __init__(self, Pole):
        self.Pole = Pole
        
        self.T = 50
        self.alpha = 0.95
        
    def Run(self):
        Pos = self.Pole.Mix()
        ds = self.Pole.Calc(Pos) - self.Pole.CalcSelf()
        
        if ds < 0:
            self.Pole.Change(Pos)
        else:
            p = np.exp(- ds / self.T)
            
            if p > rnd.random():
                self.Pole.Change(Pos)

            self.T = self.alpha * self.T

        return self.Pole.CalcSelf()
        
        
    