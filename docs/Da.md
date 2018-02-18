# An Da's work
## 	Data clean
### delete the useless cols
- EmployeeCount
- EmployeeNumber
- Over18
- OverTime
### change the character string to int
- such as change the department to 1, 2 and 3
### standardization

		data = (data - data.mean(axis = 0))/(data.std(axis = 0))

## K-means
in this part, the kmeans is used to cluster. besides, the number of dataset in each cluster had been counted


		kmodel = KMeans(n_clusters = k)  

		kmodel.fit(data.ix[0:999,0:27])
KMeans(k) is the number of clusters

data.ix[0:999,0:27] is test data set
## visualization
### introdution
this part use pygal to make a rader chart to show the different clusters has different features. 5 features were selected at random. it include ['department','education','EnvironmentSatisfaction','HourlyRate','MonthlyIncome']. for example, the first clusters influenced greatly by environment satisfaction.
## Conclusion
the results of kmeans are not well. the result is random variable. 





