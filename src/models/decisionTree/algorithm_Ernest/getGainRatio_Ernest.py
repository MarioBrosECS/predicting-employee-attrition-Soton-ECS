#!/usr/bin/python3

# compute the Gain-ratio for every feature

import csv
import pandas as pd
import math
import API_Ernest

# read csv file

filename = './data/data_Ernest/DataCleanByTed.csv'
dataSet = pd.read_csv(filename)

ent_attrition = API_Ernest.entD(dataSet, 'Attrition')
entireAttrSet = API_Ernest.attrSetGenerate(dataSet)


#gain_department = gainD(dataSet, 'Department', ent_attrition, 'Attrition')


#compute every feature and get best one
gain = 0
gain_ratio = 0
gainDic = {}
for index in dataSet.columns :
    if index != 'Attrition':

        gainDic_feature = API_Ernest.getGainDicByFeature(dataSet, index, ent_attrition, 'Attrition', entireAttrSet)

        gain_ratio_feature = gainDic_feature['gain'] / gainDic_feature['IV']
        gainDic[index] = [ gainDic_feature['gain'], gain_ratio_feature]
        if gainDic_feature['gain'] > gain :
            gain = gainDic_feature['gain']
            bestFeature = index

        if gain_ratio_feature > gain_ratio :
            gain_ratio = gain_ratio_feature
            bestRatioFeature = index

df = pd.DataFrame(gainDic,index=['gain','gain ratio'])
print('Best feature by gain is' ,bestFeature)
print('Its gain is ' ,gain)
print('Best feature by gain_ratio is' ,bestRatioFeature)
print('Its gain_ratio is ' ,gain_ratio)


df.to_csv('./reference/InformationGain.csv', index=False)
