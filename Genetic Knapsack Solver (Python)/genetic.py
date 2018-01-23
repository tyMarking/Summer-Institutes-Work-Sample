#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:11:41 2017

@author: tymarking
"""
import phenotype, fitnessFunctions, selectionFunctions, crossoverFunctions, mutators
import pylab

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def evolve(popSize, generations, Phenotype, fitnessF, selectionF, standardDiv, crossoverF, mutateF, muteProb):
    #origin pop
    pop = []
    valAtPop = []
    for i in range(popSize):
        pop.append(Phenotype.getRandomPhenotype())
    
    popWValue = fitnessF(pop)
    
    
    #loop
    for g in range(generations):
        #evaluate fitness
        popWValue = fitnessF(pop)
        #selection
        valAtPop.append(popWValue[0][1])
        parents = selectionF(popWValue, standardDiv)
        #crossover
        children = crossoverF(parents, popSize)
        #mutate
        children = mutateF(children, muteProb)
        
        pop = children
        #if (g%25 == 24):
            #print("Generation "+str(g+1)+" completed")
        
        
        
    popWValue = fitnessF(pop)
    valAtPop.append(popWValue[0][1])
    return valAtPop

vals = []
mins = []
maxes = []
for i in range(100):
    vals.append(evolve(500, 500, phenotype.KnapsackPhenotype, fitnessFunctions.knapsackFitness, selectionFunctions.carryWithGradiant25, 400, crossoverFunctions.triCross, mutators.probMutate, 0.17 ))
for i in range(len(vals[0])):
    mins.append(vals[0][i])
    maxes.append(vals[0][i])

avgVals = []
for i in range(len(vals[0])):
    sumVal = 0
    for val in vals:
        sumVal += val[i]
        if val[i] < mins[i]:
            mins[i] = val[i]
        if val[i] > maxes[i]:
            maxes[i] = val[i]
    avgVals.append(sumVal/len(vals))
    

pylab.plot(range(len(avgVals)), mins, '-r', label = "Min Value")
pylab.plot(range(len(avgVals)), maxes, '-g', label = "Max Value")
pylab.plot(range(len(avgVals)), avgVals, '-b', label = "Average Value")
pylab.legend(loc='lower right')
pylab.title("Knapsack Problem: 500 phenotypes")
pylab.xlabel("Generation")
pylab.ylabel("Value")
pylab.show()
