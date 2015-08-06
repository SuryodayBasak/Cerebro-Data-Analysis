# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:55:14 2015

@author: suryo
"""
"""
Need to cross corelate
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
        self.MidGamma_mean, self.MidGamma_median, self.MidGamma_variance = essentialStats(self.midGamma)
        self.Delta_mean, self.Delta_median, self.Delta_variance = essentialStats(self.delta)
        self.Theta_mean, self.Theta_median, self.Theta_variance = essentialStats(self.theta)      
        

        
    def showEssentialStats(self):
        
        print "\n\n",self.dataSetName,"\n\n"
        print "\tMEAN","\t\t","MEDIAN","\t","VARIANCE\n"
        print "Low Alpha\t",self.lowAlpha_mean,"\t",self.lowAlpha_median,"\t",self.lowAlpha_variance
        print "High Alpha\t",self.highAlpha_mean,"\t",self.highAlpha_median,"\t",self.highAlpha_variance
        print "Low Beta\t",self.lowBeta_mean,"\t",self.lowBeta_median,"\t",self.lowBeta_variance
        print "High Beta\t",self.highBeta_mean,"\t",self.highBeta_median,"\t",self.highBeta_variance
        print "Low Gamma\t",self.lowGamma_mean,"\t",self.lowGamma_median,"\t",self.lowGamma_variance
        print "Mid Gamma\t",self.MidGamma_mean,"\t",self.MidGamma_median,"\t",self.MidGamma_variance
        print "Delta\t",self.Delta_mean,"\t",self.Delta_median,"\t",self.Delta_variance
        print "Theta\t",self.Theta_mean,"\t",self.Theta_median,"\t",self.Theta_variance

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/hawkrattle/hawkrattle"
n = 10
hawkrattle = dataSetEssentials(s,n,"HAWKRATTLE")
hawkrattle.showEssentialStats()

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/vatican/vatican"
n = 10
hawkrattle = dataSetEssentials(s,n,"VATICAN")
hawkrattle.showEssentialStats()

s = "/home/suryo/MyStuff/MyDevelopment/Cerebro/Data Tools/Data/CerebroCSV/datasets/visionary/visionary"
n = 10
hawkrattle = dataSetEssentials(s,n,"VISIONARY")
hawkrattle.showEssentialStats()