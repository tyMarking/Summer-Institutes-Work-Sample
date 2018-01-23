#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 18:12:47 2017

@author: tymarking
"""
import phenotype
#max weight
maxWeight = 750

def knapsackFitness(phenotypes):
    ret = []
    for pheno in phenotypes:
        if pheno.weight > maxWeight:
            ret.append((pheno, 0))
        else:
            ret.append((pheno, pheno.value))
    ret.sort(key=lambda pheno: pheno[1], reverse = True)
    return ret


phenos = []
phenos.append(phenotype.KnapsackPhenotype([0,1,1,1,1]))
phenos.append(phenotype.KnapsackPhenotype([0,1,1,1,0]))
phenos.append(phenotype.KnapsackPhenotype([0,0,1,0,0]))
phenos.append(phenotype.KnapsackPhenotype([1,1,1,1,1]))

#print("hi")
#print(knapsackFitness(phenos))
    