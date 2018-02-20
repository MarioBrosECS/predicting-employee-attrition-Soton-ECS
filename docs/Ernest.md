# Ernest’s work

- [Data Clean](#dataClean)
- [Decision Tree](#DecisionTree)
- [Conclusion](#Conclusion)

<h2 id= 'dataClean'> Data Clean </h2>

### hard code to delete useless cols
including: 
- EmployeeCount
- EmployeeNumber
- Over18
- OverTime

### delete repeat data
The new dataSet named entireDataSet\_Ernest.csv is created in data/data\_Ernest dict. 

## Data segmentation
The data set is divided into training set and test set in the ratio of 3: 1.

The new dataSets are n data/data\_Ernest dict.

<h2 id= 'DecisionTree'> Decision Tree </h2>

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

<h2 id= 'logisticRegression'> Logistic Regression </h2>

<h2 id = 'Conclusion'> Conclusion </h2>

The initial result is not entirely satisfactory and needs to be further improved.


