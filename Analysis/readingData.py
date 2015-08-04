# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:40:52 2015

@author: suryo
"""

import csv
import numpy as np
def getAllValues(s,n):
    
    allRows = []
    for i in range(1,n):  
        with open(s+str(i)+".csv",'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter=',',quotechar='|')
            for row in reader:
                intRow = []
                for j in range (0,8):
                    intRow.append(int(row[j]))
                allRows.append(intRow)
            return allRows

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data/CerebroCSV/datasets/hawkrattle/hawkrattle"
n = 10
hawkrattleValues = getAllValues(s,n)
print hawkrattleValues

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data/CerebroCSV/datasets/vatican/vatican"
n = 10
vaticanValues = getAllValues(s,n)
print vaticanValues

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data/CerebroCSV/datasets/visionary/visionary"
n = 10
visionaryValues = getAllValues(s,n)
print visionaryValues