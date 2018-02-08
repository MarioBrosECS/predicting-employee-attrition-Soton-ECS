#!/usr/bin/python3

import csv
import os
import pandas as pd

# read csv file

filename = '../../data/hrOriginData.csv'
dataSet = pd.read_csv(filename)
print(dataSet)

# delete useless col 
del dataSet['EmployeeNumber']
del dataSet['EmployeeCount']


#TODO delete incomplete data
#TODO delete repeat data

#save csv
dataSet.to_csv('../../data/entireDataSet_Ernest.csv', index=False)

