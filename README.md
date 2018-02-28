# predicting-employee-attrition-Soton-ECS
## Table of Contents
1. ### [Description](#description-1)
2. ### [Deadline Tables](#deadline-tables-1)
    - [Dates of Meetings and Other Tasks](#dates-of-meetings-and-other-tasks)
    - [Deadline of The Group Coursework](#deadline-of-the-group-coursework)
    - [Overdue Deadlines](#overdue-deadlines)
3. ### [Weekly Summary of The Work](#weekly-summary-of-the-work-1)
    - [Yang Zhou ~ Ernest ~ moonsin](#yang-zhou--ernest--moonsin)
    - [Bang Du ~ Tedbang](#bang-du--tedbang)
    - [Da An ~ windknow123](#da-an--windknow123)
    - [Zihan Wang ~ wzhyzrsyj](#zihan-wang--wzhyzrsyj)
    - [Mardhiyyah Rafrin](#mardhiyyah-rafrin)
4. ### [Work Flow](#work-flow-1)
5. ### [Tech Stack](#tech-stack-1)
6. ### [Project Structure](#project-structure-1)

## [Description](#table-of-contents)
A repo for Human Resources Analytics by using data mining

## [Deadline Tables](#table-of-contents)
### Dates of Meetings and Other Tasks
| Tasks | Dates | Hand in Links | Tasks Status |
| :-----: | :-----: | :--------------: | :-------------: |
| Next Meeting | TBC | TBC | TBC |

### Deadline of The [Group Coursework](http://comp6237.ecs.soton.ac.uk/cw/coursework1.html)
| Tasks | Dates | Hand in Links | Tasks Status |
| :-----: | :-----: | :--------------: | :-------------: |
| Presentation | 12/13/14/15-Mar-2018 | In Class | Time TBC |
| Conference Paper | 16-May-2018 16:00 | [Final Paper Hand in](http://handin.ecs.soton.ac.uk/handin/1718/COMP6237/2/) | Open |

### Overdue Deadlines
| Tasks | Dates | Hand in Links | Tasks Status |
| :-----: | :-----: | :--------------: | :-------------: |
| Build Algorithm | Delayed to 14-Feb-2018 11:45 | Talk Through After Class | Closed |
| Review of Brief | 15-Feb-2018 00:00 | [First Brief Hand in](http://handin.ecs.soton.ac.uk/handin/1718/COMP6237/1/) | Closed |
| Project Brief | 16-Feb-2018 16:00 | [Brief Hand in](http://handin.ecs.soton.ac.uk/handin/1718/COMP6237/1/) | Closed 2nd Ver. handed |
| Basic Algorithm Talk | 19-Feb-2018 16:00 | Talk Through After Class | Closed |

## [Weekly Summary of The Work](#table-of-contents)
1. [Yang Zhou ~ Ernest ~ moonsin](#yang-zhou--ernest--moonsin)
2. [Bang Du ~ Tedbang](#bang-du--tedbang)
3. [Da An ~ windknow123](#da-an--windknow123)
4. [Zihan Wang ~ wzhyzrsyj](#zihan-wang--wzhyzrsyj)
5. [Mardhiyyah Rafrin](#mardhiyyah-rafrin)

### [Yang Zhou ~ Ernest ~ moonsin](#weekly-summary-of-the-work-1)
1. Decision Tree (Python) - 84%
    - Choosing best node for the three
        - Comparing information ratio to select the best feature.
    - Handling continuous values
        - To maximize the information gain by using dichotomies and greedy algorithms.
    - Post pruning
        - To improve the generalisation ability.
        
2. Logistic Regression (Python) - 87%
    - Getting the expression of logistic regression by using sigmoid function.
    - Using maximum likelihood method and get an expression.
    - Using Newton's method to get the unknown parameter of the expression.

3. Data Cleaning (Python)
    - Deleted useless columns
    - Deleted repeating data
    - Compared information gain & information gain ratio
    - Data Segmentation
        - Randomly divides data into training and test set with the ratio of 3:1
    - Data Regularization
        - To normalize the data which transforms a value into a new value between 0 and 1. (More on quantified data)

### [Bang Du ~ Tedbang](#weekly-summary-of-the-work-1)
1. PCA (R) - 87~88%
    - Logistic Regression
    - Stepwise Regression
    - Random Forest after using PCA.  Then construct ROC and K-fold cross-validation (Under Construction)
    
2. Data Cleaning (Python)
    - Data Quantisation

3. Data Analysis (R)
    - Correlation Coefficient
        - Using describe method to observe data information which includes mean, variance etc.
        - Using cor method to find the correlation coefficient between each feature and other ones.
    - Stepwise Regression
        -To find the unbalanced data

### [Da An ~ windknow123](#weekly-summary-of-the-work-1)
1. K-means (Python) - May be discarded

2. Fisher (Python) - 86.7%
    - with K-fold cross-validation

3. Data Cleaning (Python)
    - Deleted useless columns
    - Change the character string into int
    - Data Standardisation

4. Data Visualization
    - Showing that different clusters have different features in a radar chart.

### [Zihan Wang ~ wzhyzrsyj](#weekly-summary-of-the-work-1)
1. Random Forest (R) - 83%
    - Random Survival Forest (R) appears to have less accuracy result, may be discarded.

2. Data Visualization (To be proved)
    - A graph of decision tree
    - Analysis to the features

### [Mardhiyyah Rafrin](#weekly-summary-of-the-work-1)
1. SVM - 85%
    - When tried normalisation, it will be reduced to 83%.

2. Data Analysis
    - Had paper about imbalance dataset for SVM. (Under construction)
    
3. Data Cleaning
    - Basic data cleaning to be applied with SVM.

## [Work Flow](#table-of-contents)
Follow Github Flow

## [Tech Stack](#table-of-contents)

### Python3 and main related modules
- pandas

### Tableau
### matlab
### R

## [Project Structure](#table-of-contents)
Follow the structure from [https://n3xtchen.github.io/n3xtchen/data\_analytics/2017/05/17/data-science-project-rule][1]

[1]:	https://n3xtchen.github.io/n3xtchen/data_analytics/2017/05/17/data-science-project-rule
