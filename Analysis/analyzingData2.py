# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:32:10 2015

@author: suryo
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

def getAllValues(s,n):
    
    lowAlpha    = []
    highAlpha   = []
    lowBeta     = []
    highBeta    = []
    lowGamma    = []
    midGamma    = []
    delta       = []
    theta       = []
    
    limit = 0
    for i in range(1,n):
        with open(s+str(i)+".csv",'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader:
                limit += 1
                
                if limit > 2:
                    lowAlpha.append(int(row[0]))
                    highAlpha.append(int(row[1]))
                    lowBeta.append(int(row[2]))
                    highBeta.append(int(row[3]))
                    lowGamma.append(int(row[4]))
                    midGamma.append(int(row[5]))
                    delta.append(int(row[6]))
                    theta.append(int(row[7]))
                    
            return lowAlpha,highAlpha,lowBeta,highBeta,lowGamma,midGamma,delta,theta

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/hawkrattle/hawkrattle"
n = 10
hawkrattleLowAlpha, hawkrattleHighAlpha, hawkrattleLowBeta, hawkrattleHighBeta, hawkrattleLowGamma, hawkrattleMidGamma, hawkrattleDelta, hawkrattleTheta = getAllValues(s,n)
plt.figure("hv1,hv5")
plt.xlabel("hv1")
plt.ylabel("hv5")
plt.plot(hawkrattleLowAlpha,hawkrattleHighAlpha,'ro')
plt.axis([0,10000,0,10000])
plt.show()

"""
s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data/CerebroCSV/datasets/vatican/vatican"
n = 10
hv0, hv1, hv2, hv3, hv4, hv5, hv6, hv7 = getAllValues(s,n)
plt.figure("hv1,hv5")
plt.xlabel("hv1")
plt.ylabel("hv5")
plt.plot(hv1,hv5,'ro')
plt.axis([0,10000,0,10000])
plt.show()

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data/CerebroCSV/datasets/visionary/visionary"
n = 10
hv0, hv1, hv2, hv3, hv4, hv5, hv6, hv7 = getAllValues(s,n)
plt.figure("hv1,hv5")
plt.xlabel("hv1")
plt.ylabel("hv5")
plt.plot(hv1,hv5,'ro')
plt.axis([0,10000,0,10000])
plt.show()
"""