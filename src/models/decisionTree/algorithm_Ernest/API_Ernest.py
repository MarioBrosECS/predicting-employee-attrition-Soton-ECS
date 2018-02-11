import math

# compute Entropy
def entD (dataSet, feature) :
    values = dataSet[feature].value_counts(normalize=True)
    sum = 0
    for i in values :
        sum += i* math.log2(i)
    sum = -sum
    return sum


# compute gain and IV, return a Dict
def getGainDicByFeature(dataSet, feature, entDValue, entD_feature) :

    valuesRateList = dataSet[feature].value_counts(normalize=True)
    num = len(valuesRateList)
    valuesList = dataSet[feature]

    attiData = []
    entList = []
    entSum = 0
    sum = 0

    # Use dichotomy to handle continuous discrete attributes
    # Judge whether it is a continuous value
    if( len(valuesRateList) >=15 and str(valuesList[0]).isdigit()) :

        #order
        orderedDataSet = dataSet.sort_values(by=feature)
        orderedValuesList = orderedDataSet[feature].reset_index(drop=True)

        bestBoundary = ( orderedValuesList[0] + orderedValuesList[1] ) / 2
        bestGain = 0

        ListNum = len(valuesList)
        
        #Loops get the best demarcation
        for i in range(ListNum) :
            P = (i+1)/ListNum
            attiData = []
            entList = []

            attiData.append(orderedDataSet[0:i+1])
            attiData.append(orderedDataSet[i+1:])

            entList.append( entD( attiData[0], entD_feature ))
            entList.append( entD( attiData[1], entD_feature ))

            entSum = P * entList[0] + (1-P) * entList[1]
            gain = entDValue - entSum

            if gain >= bestGain :
                bestGain = gain
                bestBoundary = ( orderedValuesList[i] + orderedValuesList[i+1] ) / 2;
                IV = -(P* math.log2(P) + (1-P) * math.log2(1 - P))

        return {'gain': bestGain, 'IV':IV, 'continuous': True, 'bestBoundary': bestBoundary}

    else :
        for i in range(num) :
            attiData.append(dataSet[dataSet[feature] == valuesRateList.index[i] ])
            entList.append (entD (attiData[i], entD_feature))
            entSum += valuesRateList[valuesRateList.index[i]] * entList[i]

            ratio = valuesRateList[valuesRateList.index[i]]
            sum += ratio * math.log2(ratio)

        IV = -sum
        gain = entDValue - entSum
        return {'gain':gain, 'IV':IV, 'continuous': False}



