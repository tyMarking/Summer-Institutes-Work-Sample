#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:12:26 2017

@author: tymarking
"""
import random

"""
70
 73
 77
 80
 82
 87
 90
 94
 98
106
110
113
115
118
120

135
139
149
150
156
163
173
184
192
201
210
214
221
229
240




"""

globalItems = [(135,70),(139,73),(149,77),(150,80),(156,82),(163,87),(173,90),(184,94),(192,98),(201,106),
               (210,110),(214,113),(221,115),(229,118),(240,120)]

class KnapsackPhenotype(object):
    
    itemsIn = [0]*len(globalItems)
    weight = 0
    value = 0
    
    def __init__(self, items):
        self.itemsIn = items
        self.weight = 0
        self.value = 0
        for i in range(len(items)):
            if self.itemsIn[i] == 1:
                self.weight += globalItems[i][1]
                self.value += globalItems[i][0]
        
    @classmethod
    def getRandomPhenotype(cls):
        newItems = []
        for i in range(len(globalItems)):
            newItems.append(random.randint(0,1))
        return KnapsackPhenotype(newItems)