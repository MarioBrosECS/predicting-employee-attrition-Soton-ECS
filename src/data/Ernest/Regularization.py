import pandas as pd

filename = './data/data_Ernest/DataCleanByTed.csv'

# dataSet values should be already transferred into numbers
dataSet = pd.read_csv(filename)

#print(dataSet)
for index in dataSet :
    if index != 'Attrition' :
        for i in range(len(dataSet[index])) :
            #print(dataSet[index][i])    
            if i == 0 :
                max = dataSet[index].loc[i]
                min = dataSet[index].loc[i]
            else :
                if dataSet[index].loc[i] > max :
                    max = dataSet[index].loc[i] 
                elif dataSet[index].loc[i] < min :
                    min = dataSet[index].loc[i]
        for i in range(len(dataSet[index])) :
            dataSet[index].loc[i] = ((dataSet[index].loc[i] - min) / (max - min))
            #print(dataSet[index].loc[i])

dataSet.to_csv('./data/data_Ernest/DataCleanByTed_regularizated.csv', index=False)
