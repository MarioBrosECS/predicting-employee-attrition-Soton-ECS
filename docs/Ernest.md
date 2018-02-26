# Ernest’s work

- [Data Clean](#data-clean)
- [Data Segmentation](#data-segmentation)
- [Regularization](#regularization)
- [Decision Tree](#decision-tree)
- [Logistic Regression](#logistic-regression)
- [Conclusion](#conclusion)

## Data Clean 

### hard code to delete useless cols

including: 
- EmployeeCount
- EmployeeNumber
- Over18
- OverTime

### delete repeat data

The new dataSet named entireDataSet\_Ernest.csv is created in data/data\_Ernest dict. 

### compare information gain and information gain ratio

/src/models/decisionTree/algorithm\_Ernest/getGainRatio_Ernest.py is used to calculated for each Feature's information gain and information gain rate, the results saved in / references. We can use this indicator to filter out useless features.

## Data Segmentation

The data set is randomly divided into training set and test set in the ratio of 3: 1.

The new dataSets are in data/data\_Ernest dict.

## Regularization

Regularization.py is used to normalize the data, it transform a value into a new value between 0 and 1. The new value between 0 and 1 is obtained by calculating the ratio of the value to the difference between the maximum value and the minimum value of the feature.(This work is based on Ted's quantified data.)

## Decision Tree 

### Brief Introduction

In this part, the following scripts are used to build the decision tree:

- API\_Ernest.py
- decisionTree.py
- postpruning.py
- testTree.py

API\_Ernest.py saves the main common functions for this part.

decisionTree.py is used to build the decision tree by using train Dataset. The decision tree will be created in /models dict.

postpruning.py is used to do postpruning on the decision tree to improve its generalization.

testTree.py can be used to test the decision tree by using test data set.

/models/decisionTree\_Ernest is used to save the decision tree while decisionTree\_Postpruninged\_Ernest is used to save the postpruninged tree.

### Usage

- run src/data/devideData\_hold-out\_Ernest.py to devide the whole data set.
- run src/models/decisionTree/algorithm\_Ernest/decisionTree.py to build decision tree.
- run src/models/decisionTree/algorithm\_Ernest/postpruning.py to do postpruning on the tree.
- run src/models/decisionTree/algorithm\_Ernest/testTree.py to test.

### Main Algorithm

#### How to select best node for the three

Firstly, calculate information gain of all left features on this node. Then calculate the information gain ratio for the features above the average of information gain. Then compare these infomation ratio and select best feature.

#### How to handle continuous values

Using dichotomies and greedy algorithms, select the demarcation point that maximizes the current information gain.

#### Pruning

The reason why use postpruning is that it can better improve the generalization ability, and the current data less, making the pruning process time will not be too long

### Result

The accuracy was improved by pruning. However, it is still around 84%.

## Logistic Regression 


### Brief Introduction

In this part, the logistic.py can be used to run the logistic regression algorithm. 

This training is mainly based on mathematical projections.


### Main Algorithm

Based on Sigmoid function, we can get the expression of logistic regression. Then we can use maximum likelihood method and get a expression. We can use different methods on how to get the unknown parameter of this expression, such as the gradient descent method and Newton's method. In this script, we have used Newton's method.

### Unbalanced data

We found that there was a very unbalanced situation with the data, which could affect the results. Therefore, we adjust the threshold of judgment according to the ratio of positive and negative training data.

### Result

The result is reasonable, its accuracy is around 87%. It might be improved if we improve features.

## Conclusion 

The initial result is satisfactory but still needs to be further improved.


A test
