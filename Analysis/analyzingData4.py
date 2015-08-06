# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:55:14 2015

@author: suryo
"""

import csv
import numpy as np

def essentialStats(array):
   analyzedMean = np.average(array)
   analyzedMedian = np.median(array)
   analyzedVariance = np.var(array)
   return analyzedMean,analyzedMedian,analyzedVariance
   
class dataSetEssentials(object):
    
    def __init__(self,s,n,name):
        
        self.lowAlpha    = []
        self.highAlpha   = []
        self.lowBeta     = []
        self.highBeta    = []
        self.lowGamma    = []
        self.midGamma    = []
        self.delta       = []
        self.theta       = []
    
        limit = 0
        for i in range(1,n):
            with open(s+str(i)+".csv",'rb') as csvfile:
                reader = csv.reader(csvfile,delimiter=',')
                for row in reader:
                    limit += 1
                
                    if limit > 2:
                        self.lowAlpha.append(int(row[0]))
                        self.highAlpha.append(int(row[1]))
                        self.lowBeta.append(int(row[2]))
                        self.highBeta.append(int(row[3]))
                        self.lowGamma.append(int(row[4]))
                        self.midGamma.append(int(row[5]))
                        self.delta.append(int(row[6]))
                        self.theta.append(int(row[7]))
                        
        self.dataSetName = name
        self.lowAlpha_mean, self.lowAlpha_median, self.lowAlpha_variance = essentialStats(self.lowAlpha)
        self.highAlpha_mean, self.highAlpha_median, self.highAlpha_variance = essentialStats(self.highAlpha)
        self.lowBeta_mean, self.lowBeta_median, self.lowBeta_variance = essentialStats(self.lowBeta)
        self.highBeta_mean, self.highBeta_median, self.highBeta_variance = essentialStats(self.highBeta)
        self.lowGamma_mean, self.lowGamma_median, self.lowGamma_variance = essentialStats(self.lowGamma)
        self.midGamma_mean, self.midGamma_median, self.midGamma_variance = essentialStats(self.midGamma)
        self.Delta_mean, self.Delta_median, self.Delta_variance = essentialStats(self.delta)
        self.Theta_mean, self.Theta_median, self.Theta_variance = essentialStats(self.theta)      
        
    def showEssentialStats(self):

        print "\n\n","SHOWING ESSENTIAL STATS FOR",self.dataSetName,"\n\n"
        print "\tMEAN","\t\t","MEDIAN","\t","VARIANCE\n"
        print "Low Alpha\t",self.lowAlpha_mean,"\t",self.lowAlpha_median,"\t",self.lowAlpha_variance
        print "High Alpha\t",self.highAlpha_mean,"\t",self.highAlpha_median,"\t",self.highAlpha_variance
        print "Low Beta\t",self.lowBeta_mean,"\t",self.lowBeta_median,"\t",self.lowBeta_variance
        print "High Beta\t",self.highBeta_mean,"\t",self.highBeta_median,"\t",self.highBeta_variance
        print "Low Gamma\t",self.lowGamma_mean,"\t",self.lowGamma_median,"\t",self.lowGamma_variance
        print "Mid Gamma\t",self.midGamma_mean,"\t",self.midGamma_median,"\t",self.midGamma_variance
        print "Delta\t",self.Delta_mean,"\t",self.Delta_median,"\t",self.Delta_variance
        print "Theta\t",self.Theta_mean,"\t",self.Theta_median,"\t",self.Theta_variance
        print "\n\n"
        
    def attributeCorrelation(self):
        print "CORRELATIONS:\n"
        print "Low-Alpha|High-Alpha:\t",np.correlate(self.lowAlpha,self.highAlpha)[0]
        print "Low-Alpha|Low-Beta:\t",np.correlate(self.lowAlpha,self.lowBeta)[0]
        print "Low-Alpha|High-Beta:\t",np.correlate(self.lowAlpha,self.highBeta)[0]
        print "Low-Alpha|Low-Gamma:\t",np.correlate(self.lowAlpha,self.lowGamma)[0]
        print "Low-Alpha|Mid-Gamma:\t",np.correlate(self.lowAlpha,self.midGamma)[0]
        print "Low-Alpha|Delta:\t",np.correlate(self.lowAlpha,self.delta)[0]
        print "Low-Alpha|Theta:\t",np.correlate(self.lowAlpha,self.theta)[0]
        print "\n"
        
        print "High-Alpha|Low-Beta:\t",np.correlate(self.highAlpha,self.lowBeta)[0]
        print "High-Alpha|High-Beta:\t",np.correlate(self.highAlpha,self.highBeta)[0]
        print "High-Alpha|Low-Gamma:\t",np.correlate(self.highAlpha,self.lowGamma)[0]
        print "High-Alpha|Mid-Gamma:\t",np.correlate(self.highAlpha,self.midGamma)[0]
        print "High-Alpha|Delta:\t",np.correlate(self.highAlpha,self.delta)[0]
        print "High-Alpha|Theta:\t",np.correlate(self.highAlpha,self.theta)[0]
        print "\n"
        
        print "Low-Beta|High-Beta:\t",np.correlate(self.lowBeta,self.highBeta)[0]
        print "Low-Beta|Low-Gamma:\t",np.correlate(self.lowBeta,self.lowGamma)[0]
        print "Low-Beta|Mid-Gamma:\t",np.correlate(self.lowBeta,self.midGamma)[0]
        print "Low-Beta|Delta:\t",np.correlate(self.lowBeta,self.delta)[0]
        print "Low-Beta|Theta:\t",np.correlate(self.lowBeta,self.theta)[0]
        print "\n"
        
        print "High-Beta|Low-Gamma:\t",np.correlate(self.highBeta,self.lowGamma)[0]
        print "High-Beta|Mid-Gamma:\t",np.correlate(self.highBeta,self.midGamma)[0]
        print "High-Beta|Delta:\t",np.correlate(self.highBeta,self.delta)[0]
        print "High-Beta|Theta:\t",np.correlate(self.highBeta,self.theta)[0]
        print "\n"
        
        print "Low-Gamma|Mid-Gamma:\t",np.correlate(self.lowGamma,self.midGamma)[0]
        print "Low-Gamma|Delta:\t",np.correlate(self.lowGamma,self.delta)[0]
        print "Low-Gamma|Theta:\t",np.correlate(self.lowGamma,self.theta)[0]
        print "\n"
        
        print "Mid-Gamma|Delta:\t",np.correlate(self.midGamma,self.delta)[0]
        print "Mid-Gamma|Theta:\t",np.correlate(self.midGamma,self.theta)[0]
        print "\n"
        
        print "Delta|Theta:\t",np.correlate(self.delta,self.theta)[0]
        print "\n\n"

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/hawkrattle/hawkrattle"
n = 10
hawkrattle = dataSetEssentials(s,n,"HAWKRATTLE")
hawkrattle.showEssentialStats()
hawkrattle.attributeCorrelation()

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/vatican/vatican"
n = 10
vatican = dataSetEssentials(s,n,"VATICAN")
vatican.showEssentialStats()
vatican.attributeCorrelation()

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/visionary/visionary"
n = 10
visionary = dataSetEssentials(s,n,"VISIONARY")
visionary.showEssentialStats()
visionary.attributeCorrelation()