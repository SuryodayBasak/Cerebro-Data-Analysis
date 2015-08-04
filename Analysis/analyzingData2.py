# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:32:10 2015

@author: suryo
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

def getAllValues(s,n):
    
    cols_0 = []
    cols_1 = []
    cols_2 = []
    cols_3 = []
    cols_4 = []
    cols_5 = []
    cols_6 = []
    cols_7 = []
    
    for i in range(1,n):  
        with open(s+str(i)+".csv",'rb') as csvfile:
            reader = csv.reader(csvfile,delimiter=',')
            for row in reader:
                cols_0.append(int(row[0]))
                cols_1.append(int(row[1]))
                cols_2.append(int(row[2]))
                cols_3.append(int(row[3]))
                cols_4.append(int(row[4]))
                cols_5.append(int(row[5]))
                cols_6.append(int(row[6]))
                cols_7.append(int(row[7]))
            return cols_0,cols_1,cols_2,cols_3,cols_4,cols_5,cols_6,cols_7

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data/CerebroCSV/datasets/hawkrattle/hawkrattle"
n = 10
hv0, hv1, hv2, hv3, hv4, hv5, hv6, hv7 = getAllValues(s,n)
plt.figure("hv1,hv5")
plt.xlabel("hv1")
plt.ylabel("hv5")
plt.plot(hv1,hv5,'ro')
plt.axis([0,10000,0,10000])
plt.show()

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