import pandas as pd
import csv

filename = '../../groupcoursework/WA_Fn-UseC_-HR-Employee-Attrition.csv'

data = pd.read_csv(filename)

df = pd.DataFrame(data)

for item in range(df.columns.size):
    df[df.isnull().values == True]         #search the empty block

attribute = list(data);                    #get the feature names

for Rows_index in range(0, len(attribute)):

    count = 0.0

    if (isinstance(df[attribute[Rows_index]].value_counts().index[0], str)):

        for Columns_value in range(0,len(df[attribute[Rows_index]].value_counts().index)):

            temp = df[attribute[Rows_index]].value_counts().index

            charts = temp[Columns_value]

            df[attribute[Rows_index]] = df[attribute[Rows_index]].replace(charts, count)

            count = count + 1
    else:

        continue


df.to_csv('../../groupcoursework/quantifyDataSet_Bang.csv', index=False)