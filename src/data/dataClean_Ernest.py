#!/usr/bin/python3

import csv
import pandas as pd

# read csv file

filename = '../../data/data_Ernest/hrOriginData.csv'
dataSet = pd.read_csv(filename)

# delete useless col 
del dataSet['EmployeeNumber']
del dataSet['EmployeeCount']
del dataSet['Over18']
del dataSet['StandardHours']



#TODO delete incomplete data
#TODO delete repeat data
dataSet.drop_duplicates(keep='first', inplace=True)

#save csv
dataSet.to_csv('../../data/data_Ernest/entireDataSet_Ernest.csv', index=False)

