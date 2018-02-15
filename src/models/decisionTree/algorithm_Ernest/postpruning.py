#!/usr/bin/python3

import pandas as pd
import API_Ernest
import pickle
from copy import deepcopy

filename = './data/data_Ernest/trainData_holdOut_Ernest.csv'
testFileName = './data/data_Ernest/testData_holdOut_Ernest.csv'

testDataSet = pd.read_csv(testFileName)
dataSet = pd.read_csv(filename)

predictfeature = 'Attrition'
entireAttrSet = API_Ernest.attrSetGenerate(dataSet)

decisionTree = pickle.load(open("./models/decisionTree_Ernest", "rb"))

def getAccuracy(Tree,testDataSet) :
    correct = 0
    for i in range(len(testDataSet)) :
        indexFeatureClass =API_Ernest.featureClass(Tree, testDataSet.loc[i])
        #print(indexFeatureClass)
        if(indexFeatureClass == testDataSet.loc[i][predictfeature]):
            correct += 1

    return(correct/len(testDataSet))


def postpruning(Tree, trainData) :
    print('postpruning function')
    curNode = list(Tree.keys())[0]

    if FaOfLeaf(Tree) :
        #print('Father of Leaf')
        Acc = getAccuracy(decisionTree,testDataSet)
        bestClass = API_Ernest.getClass(trainData, predictfeature)
        leaves = deepcopy(Tree)
        Tree.clear()
        Tree[predictfeature] = bestClass

        newAcc = getAccuracy(decisionTree,testDataSet)

        if newAcc > Acc :
            print('restart')
            postpruning(decisionTree, dataSet)
        else :
            #Tree = deepcopy(leaves)
            Tree.clear()
            node = list(leaves.keys())[0]
            Tree[node] = {}
            for index in leaves[node] :
                Tree[node][index] = {}
                Tree[node][index][predictfeature] =  leaves[node][index][predictfeature]
            return
    else :
        if curNode == predictfeature :
            return
        else :
            for index in Tree[curNode] :
                childTrainData = getChildTrainData(Tree, curNode, index, trainData)
                postpruning(Tree[curNode][index], childTrainData)


def FaOfLeaf(Tree) :
    curNode = list(Tree.keys())[0]

    if curNode == predictfeature :
        return False

    else :

        for index in Tree[curNode] :
            nextNode = list(Tree[curNode][index].keys())[0]
            if nextNode != predictfeature :
                return False

        return True


def getChildTrainData(Tree, attr, value, trainData) :

    if (entireAttrSet[attr]['ifContinuous']) :
        subData =eval( 'trainData.loc[dataSet[attr]' + value +']')
    else :
        subData = trainData.loc[trainData[attr] == value ]
    return subData


postpruning(decisionTree, dataSet)

pickle.dump(decisionTree, open("./models/decisionTree_Postpruninged_Ernest", "wb"))
