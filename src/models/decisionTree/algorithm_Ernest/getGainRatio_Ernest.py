#!/usr/bin/python3

# compute the Gain-ratio for every feature

import csv
import pandas as pd
import math
import API_Ernest

# read csv file

filename = './data/data_Ernest/entireDataSet_Ernest.csv'
dataSet = pd.read_csv(filename)

ent_attrition = API_Ernest.entD(dataSet, 'Attrition')


#gain_department = gainD(dataSet, 'Department', ent_attrition, 'Attrition')


#compute every feature and get best one
gain = 0
gain_ratio = 0

for index in dataSet.columns :
    if index != 'Attrition':
        gain_department = API_Ernest.gainD(dataSet, index, ent_attrition, 'Attrition')
        IV_department = API_Ernest.getIV(dataSet, index)
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


