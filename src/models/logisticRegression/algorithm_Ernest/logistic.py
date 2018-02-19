import numpy as np
import pandas as pd
import math

def sigmoid(inX) :  
    return 1.0/(1+ math.exp(-inX)) 

def P1(beta, x) :
    return math.exp(np.dot(beta.T, x))/(1 + math.exp(np.dot(beta.T, x)))

def P2(beta, x) :
    return 1/(1 + math.exp(np.dot(beta.T, x)))

def fx(X, Y, beta) :
    sum = 0
    for i in range(len(Y)) :
        Xi = X[:,i]
        Xi.shape = (len(X),1)
        sum += np.dot(Xi,(Y.loc[i] - P1(beta,Xi))) 
    return -sum

def dx(X,Y, beta) :
    sum = 0
    for i in range(len(Y)) :
        Xi = X[:,i]
        Xi.shape = (len(X),1)

        Xx = np.dot(Xi, Xi.T)
        Xxp = np.dot(Xx, P1(beta, Xi))
        dx1 = np.dot(Xxp,(1-P1(beta, Xi)))
        sum += dx1 
    return sum

filename = './data/data_Ernest/trainDataCleanByTed.csv'
testfilename = './data/data_Ernest/testDataCleanByTed.csv'
dataSet = pd.read_csv(filename)
testDataSet = pd.read_csv(testfilename)
 

X = dataSet.drop('Attrition', axis=1)
addOne = np.ones((len(X),1))
X = np.c_[X,addOne]

X = X.T
Y = dataSet['Attrition']
#x0 = np.array(X.loc[0],dtype=np.float)

beta = np.zeros((len(X), 1))
lastBeta = beta.copy()

for i in range(5000) :
    if i == 0 :
       fx1 = fx(X, Y, beta)
       dx1 = dx(X, Y, beta)
       newBeta = beta - np.dot(np.linalg.inv(dx1), fx1)
    else :
        if(np.linalg.norm(newBeta - lastBeta) > 0.000000001) :
            lastBeta = newBeta.copy()
            fx2 = fx(X, Y, lastBeta)
            dx2 = dx(X, Y, lastBeta)
            newBeta = lastBeta - np.dot(np.linalg.inv(dx2), fx2)
            #print(np.linalg.norm(lastBeta - newBeta))
        else :
            break

beta = newBeta

X = testDataSet.drop('Attrition', axis=1)
addOne = np.ones((len(X),1))
X = np.c_[X,addOne]

X = X.T
Y = testDataSet['Attrition']
correct = 0
List = Y.value_counts(normalize=True)
print(List)

for i in range(len(Y)) :
    Xi = X[:,i]
    Xi.shape = (len(X),1)
    inX = np.dot(beta.T, Xi)
    value = sigmoid(inX) 

    rate = value / (1 - value)
    reviseRate = rate * (List[1]/List[0])

    if reviseRate > 1 and Y[i] == 1:
        correct += 1
    elif reviseRate <= 1 and Y[i] == 0 :
        correct += 1

print(correct/len(Y))
