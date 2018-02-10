import pandas as pd
import math

# compute Entropy
def entD (dataSet, feature) :
    values = dataSet[feature].value_counts(normalize=True)
    sum = 0
    for i in values :
        sum += i* math.log2(i)
    sum = -sum
    return sum

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

# compute IV
def getIV(dataSet, feature) :
    values = dataSet[feature].value_counts(normalize=True)
    num = len(values)
    sum = 0
    for i in range(num) :
        ratio = values[values.index[i]]
        sum += ratio * math.log2(ratio) 
    IV = -sum 
    return IV 

