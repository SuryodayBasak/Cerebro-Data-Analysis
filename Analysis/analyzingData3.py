# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 22:49:14 2015

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

def essentialStats(array):
    analyzedMean = np.average(array)
    analyzedMedian = np.median(array)
    analyzedVariance = np.var(array)
    return analyzedMean,analyzedMedian,analyzedVariance


"""
ANALYZING HAWKRATTLE
"""
    
s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/hawkrattle/hawkrattle"
n = 10
hawkrattleLowAlpha, hawkrattleHighAlpha, hawkrattleLowBeta, hawkrattleHighBeta, hawkrattleLowGamma, hawkrattleMidGamma, hawkrattleDelta, hawkrattleTheta = getAllValues(s,n)

hawkrattleLowAlpha_mean, hawkrattleLowAlpha_median, hawkrattleLowAlpha_variance = essentialStats(hawkrattleLowAlpha)
hawkrattleHighAlpha_mean, hawkrattleHighAlpha_median, hawkrattleHighAlpha_variance = essentialStats(hawkrattleHighAlpha)
hawkrattleLowBeta_mean, hawkrattleLowBeta_median, hawkrattleLowBeta_variance = essentialStats(hawkrattleLowBeta)
hawkrattleHighBeta_mean, hawkrattleHighBeta_median, hawkrattleHighBeta_variance = essentialStats(hawkrattleHighBeta)
hawkrattleLowGamma_mean, hawkrattleLowGamma_median, hawkrattleLowGamma_variance = essentialStats(hawkrattleLowGamma)
hawkrattleMidGamma_mean, hawkrattleMidGamma_median, hawkrattleMidGamma_variance = essentialStats(hawkrattleMidGamma)
hawkrattleDelta_mean, hawkrattleDelta_median, hawkrattleDelta_variance = essentialStats(hawkrattleDelta)
hawkrattleTheta_mean, hawkrattleTheta_median, hawkrattleTheta_variance = essentialStats(hawkrattleTheta)

print "\n\nESSENTIAL STATS FOR DATASET HAWKRATTLE\n"
print "\tMEAN","\t\t","MEDIAN","\t","VARIANCE\n"
print "LowAlpha\t",hawkrattleLowAlpha_mean,'\t', hawkrattleLowAlpha_median,'\t', hawkrattleLowAlpha_variance
print "HighAlpha\t",hawkrattleHighAlpha_mean,'\t', hawkrattleHighAlpha_median,'\t', hawkrattleHighAlpha_variance
print "LowBeta\t",hawkrattleLowBeta_mean,'\t', hawkrattleLowBeta_median,'\t', hawkrattleLowBeta_variance
print "HighBeta\t",hawkrattleHighBeta_mean,'\t', hawkrattleHighBeta_median,'\t', hawkrattleHighBeta_variance
print "LowGamma\t",hawkrattleLowGamma_mean,'\t', hawkrattleLowGamma_median,'\t', hawkrattleLowGamma_variance
print "MidGamma\t",hawkrattleMidGamma_mean,'\t', hawkrattleMidGamma_median,'\t', hawkrattleMidGamma_variance
print "Delta\t",hawkrattleDelta_mean,'\t', hawkrattleDelta_median,'\t', hawkrattleDelta_variance
print "Theta\t",hawkrattleTheta_mean,'\t', hawkrattleTheta_median,'\t', hawkrattleTheta_variance


"""
ANALYZING VATICAN
"""

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/vatican/vatican"
n = 10
vaticanLowAlpha, vaticanHighAlpha, vaticanLowBeta, vaticanHighBeta, vaticanLowGamma, vaticanMidGamma, vaticanDelta, vaticanTheta = getAllValues(s,n)

vaticanLowAlpha_mean, vaticanLowAlpha_median, vaticanLowAlpha_variance = essentialStats(vaticanLowAlpha)
vaticanHighAlpha_mean, vaticanHighAlpha_median, vaticanHighAlpha_variance = essentialStats(vaticanHighAlpha)
vaticanLowBeta_mean, vaticanLowBeta_median, vaticanLowBeta_variance = essentialStats(vaticanLowBeta)
vaticanHighBeta_mean, vaticanHighBeta_median, vaticanHighBeta_variance = essentialStats(vaticanHighBeta)
vaticanLowGamma_mean, vaticanLowGamma_median, vaticanLowGamma_variance = essentialStats(vaticanLowGamma)
vaticanMidGamma_mean, vaticanMidGamma_median, vaticanMidGamma_variance = essentialStats(vaticanMidGamma)
vaticanDelta_mean, vaticanDelta_median, vaticanDelta_variance = essentialStats(vaticanDelta)
vaticanTheta_mean, vaticanTheta_median, vaticanTheta_variance = essentialStats(vaticanTheta)

print "\n\nESSENTIAL STATS FOR DATASET VATICAN\n"
print "\tMEAN","\t\t","MEDIAN","\t","VARIANCE\n"
print "LowAlpha\t",vaticanLowAlpha_mean,'\t', vaticanLowAlpha_median,'\t', vaticanLowAlpha_variance
print "HighAlpha\t",vaticanHighAlpha_mean,'\t', vaticanHighAlpha_median,'\t', vaticanHighAlpha_variance
print "LowBeta\t",vaticanLowBeta_mean,'\t', vaticanLowBeta_median,'\t', vaticanLowBeta_variance
print "HighBeta\t",vaticanHighBeta_mean,'\t', vaticanHighBeta_median,'\t', vaticanHighBeta_variance
print "LowGamma\t",vaticanLowGamma_mean,'\t', vaticanLowGamma_median,'\t', vaticanLowGamma_variance
print "MidGamma\t",vaticanMidGamma_mean,'\t', vaticanMidGamma_median,'\t', vaticanMidGamma_variance
print "Delta\t",vaticanDelta_mean,'\t', vaticanDelta_median,'\t', vaticanDelta_variance
print "Theta\t",vaticanTheta_mean,'\t', vaticanTheta_median,'\t', vaticanTheta_variance


"""
ANALYZING VISIONARY
"""

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/visionary/visionary"
n = 10
visionaryLowAlpha, visionaryHighAlpha, visionaryLowBeta, visionaryHighBeta, visionaryLowGamma, visionaryMidGamma, visionaryDelta, visionaryTheta = getAllValues(s,n)

visionaryLowAlpha_mean, visionaryLowAlpha_median, visionaryLowAlpha_variance = essentialStats(visionaryLowAlpha)
visionaryHighAlpha_mean, visionaryHighAlpha_median, visionaryHighAlpha_variance = essentialStats(visionaryHighAlpha)
visionaryLowBeta_mean, visionaryLowBeta_median, visionaryLowBeta_variance = essentialStats(visionaryLowBeta)
visionaryHighBeta_mean, visionaryHighBeta_median, visionaryHighBeta_variance = essentialStats(visionaryHighBeta)
visionaryLowGamma_mean, visionaryLowGamma_median, visionaryLowGamma_variance = essentialStats(visionaryLowGamma)
visionaryMidGamma_mean, visionaryMidGamma_median, visionaryMidGamma_variance = essentialStats(visionaryMidGamma)
visionaryDelta_mean, visionaryDelta_median, visionaryDelta_variance = essentialStats(visionaryDelta)
visionaryTheta_mean, visionaryTheta_median, visionaryTheta_variance = essentialStats(visionaryTheta)

print "\n\nESSENTIAL STATS FOR DATASET VISIONARY\n"
print "\tMEAN","\t\t","MEDIAN","\t","VARIANCE\n"
print "LowAlpha\t",visionaryLowAlpha_mean,'\t', visionaryLowAlpha_median,'\t', visionaryLowAlpha_variance
print "HighAlpha\t",visionaryHighAlpha_mean,'\t', visionaryHighAlpha_median,'\t', visionaryHighAlpha_variance
print "LowBeta\t",visionaryLowBeta_mean,'\t', visionaryLowBeta_median,'\t', visionaryLowBeta_variance
print "HighBeta\t",visionaryHighBeta_mean,'\t', visionaryHighBeta_median,'\t', visionaryHighBeta_variance
print "LowGamma\t",visionaryLowGamma_mean,'\t', visionaryLowGamma_median,'\t', visionaryLowGamma_variance
print "MidGamma\t",visionaryMidGamma_mean,'\t', visionaryMidGamma_median,'\t', visionaryMidGamma_variance
print "Delta\t",visionaryDelta_mean,'\t', visionaryDelta_median,'\t', visionaryDelta_variance
print "Theta\t",visionaryTheta_mean,'\t', visionaryTheta_median,'\t', visionaryTheta_variance