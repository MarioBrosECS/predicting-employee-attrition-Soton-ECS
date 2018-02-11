#!/usr/bin/python3

import csv
import pandas as pd
import math
import API_Ernest

filename = './data/data_Ernest/entireDataSet_Ernest.csv'
dataSet = pd.read_csv(filename)
atrrSet = {}

API_Ernest.attrSetGenerate(dataSet)

#def treeGenerate(dataSet, atrrSet) :



