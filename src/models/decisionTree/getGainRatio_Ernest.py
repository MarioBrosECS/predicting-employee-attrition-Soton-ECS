#!/usr/bin/python3

# compute the Gain-ratio for every feature

import csv
import pandas as pd
import math

# read csv file

filename = '../../../data/entireDataSet_Ernest.csv'
dataSet = pd.read_csv(filename)

# compute Entropy
def entD (dataSet, feature) :
    values = dataSet[feature].value_counts(normalize=True)
    sum = 0
    for i in values :
        sum += i* math.log2(i)
    sum = -sum
    return sum

ent_attrition = entD(dataSet, 'Attrition')

# compute gain
def gainD(dataSet, feature, entDValue, entD_feature) :
    values = dataSet[feature].value_counts(normalize=True)
    num = len(values)
    departmentData = []
    entList = []
    sum = 0
    for i in range(num) :
        departmentData.append(dataSet[dataSet[feature] == values.index[i] ])
        entList.append (entD (departmentData[i], entD_feature))
        sum += values[values.index[i]] * entList[i]
    gain = entDValue - sum
    return gain 

#gain_department = gainD(dataSet, 'Department', ent_attrition, 'Attrition')

def getIV(dataSet, feature) :
    values = dataSet[feature].value_counts(normalize=True)
    num = len(values)
    sum = 0
    for i in range(num) :
        ratio = values[values.index[i]]
        sum += ratio * math.log2(ratio) 
    IV = -sum 
    return IV 

#compute every feature and get best one
gain = 0
gain_ratio = 0

for index in dataSet.columns :
    #print(index)
    if index != 'Attrition':
        gain_department = gainD(dataSet, index, ent_attrition, 'Attrition')
        IV_department = getIV(dataSet, index)
        #print(index)
        #print(gain_department)
        #print(IV_department)
        gain_ratio_department = gain_department / IV_department
        if gain_department > gain :
            gain = gain_department
            bestFeature = index
        if gain_ratio_department > gain_ratio :
            gain_ratio = gain_ratio_department
            bestRatioFeature = index

print('Best feature by gain is' ,bestFeature)
print('Its gain is ' ,gain)
print('Best feature by gain_ratio is' ,bestRatioFeature)
print('Its gain_ratio is ' ,gain_ratio)


