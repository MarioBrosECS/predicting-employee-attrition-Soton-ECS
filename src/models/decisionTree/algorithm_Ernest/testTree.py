import pandas as pd
import pickle


testFileName = './data/data_Ernest/testData_holdOut_Ernest.csv'

testDataSet = pd.read_csv(testFileName)

#print(entireAttrSet)
Tree = {}
currentTreeNode = {}

#pickle.dump(decisionTree, open("./models/decisionTree_Ernest", "wb"))

Tree = pickle.load(open("./models/decisionTree_Ernest", "rb"))

def featureClass(tree, data):
    curNode = list(tree.keys())
    if curNode[0] == 'Attrition' :
        return tree['Attrition']
    else :
        keyList = list(tree[curNode[0]].keys())
        if(ifContinuous(keyList)) :
            if(eval(str(data[curNode[0]]) + keyList[0])) :
                return featureClass(tree[curNode[0]][keyList[0]],data)
            else :
                return featureClass(tree[curNode[0]][keyList[1]],data)
        else :
            return featureClass(tree[curNode[0]][data[curNode[0]]],data)

def ifContinuous(keyList) :
    for i in keyList :
        if '>=' in str(i) :
            return True
    return 0 

correct = 0
for i in range(len(testDataSet)) :
    indexFeatureClass =featureClass(Tree, testDataSet.loc[i])
    print(indexFeatureClass)
    if(indexFeatureClass == testDataSet.loc[i]['Attrition']):
        correct += 1
    
#featureClass(Tree,testDataSet)
print(correct/len(testDataSet))
