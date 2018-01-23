#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:12:57 2017

@author: tymarking
"""
import random

def top6(phenotypes):
    return phenotypes[:6]

def top6th(phenotypes):
    ret = []
    for i in range(int(len(phenotypes)/6)):
        ret.append(phenotypes[i])
    return ret


def gradiant25(phenotypes, standardDeviation):
    parentNum = (int)(len(phenotypes)/4)
    parents = []
    index = int(0)
    for i in range (parentNum):
        while index >= len(phenotypes) or phenotypes[index] in parents:
            index = int(abs(random.gauss(0,parentNum)))
        parents.append(phenotypes[index])
    return parents

def carryWithGradiant25(phenotypes, standardDeviation):
    parentNum = (int)(len(phenotypes)/4)
    parents = []
    parents.append(phenotypes[0])
    parents.append(phenotypes[1])
    parents.append(phenotypes[2])
    index = int(0)
    for i in range (parentNum):
        while index >= len(phenotypes) or phenotypes[index] in parents:
            index = int(abs(random.gauss(0,parentNum)))
        parents.append(phenotypes[index])
    return parents