import pandas as pd
import pickle
import API_Ernest


testFileName = './data/data_Ernest/testData_holdOut_Ernest.csv'

testDataSet = pd.read_csv(testFileName)

#print(entireAttrSet)
Tree = {}
currentTreeNode = {}

#pickle.dump(decisionTree, open("./models/decisionTree_Ernest", "wb"))

#Tree = pickle.load(open("./models/decisionTree_Ernest", "rb"))
Tree = pickle.load(open("./models/decisionTree_Postpruninged_Ernest", "rb"))

correct = 0
forceCorrect = 0
for i in range(len(testDataSet)) :
    indexFeatureClass = API_Ernest.featureClass(Tree, testDataSet.loc[i])
    #print(indexFeatureClass)
    if(indexFeatureClass == testDataSet.loc[i]['Attrition']):
        correct += 1
    if(testDataSet.loc[i]['Attrition'] == 'No') :
        forceCorrect += 1
    
print(correct/len(testDataSet))
print(forceCorrect/len(testDataSet))
