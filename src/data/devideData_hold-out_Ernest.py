#!/usr/bin/python3

import pandas as pd

filename = './data/data_Ernest/entireDataSet_Ernest.csv'
dataSet = pd.read_csv(filename)

trainData_Rate = 0.75
testData = pd.DataFrame(columns = dataSet.columns)
indexNum = 0

# get trainSet randomly
trainSet = dataSet.sample(frac = trainData_Rate)

# filter trainSet to create testSet
for i in dataSet.index :
    if i not in trainSet.index :
        testData.loc[indexNum] = dataSet.loc[i] 
        indexNum += 1
        
trainSet.reset_index(drop=False)

#save csv
trainSet.to_csv('./data/data_Ernest/trainData_holdOut_Ernest.csv', index=False)
testData.to_csv('./data/data_Ernest/testData_holdOut_Ernest.csv', index=False)

