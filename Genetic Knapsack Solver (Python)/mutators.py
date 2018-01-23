# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:51:45 2018

@author: Ty
"""
import random

def probMutate(phenotypes, probability):
    for pheno in phenotypes:
        for i in range(len(pheno.itemsIn)):
            if random.random() < probability:
                if pheno.itemsIn[i] == 0:
                    pheno.itemsIn[i] = 1
                else:
                    pheno.itemsIn[i] = 0
    return phenotypes