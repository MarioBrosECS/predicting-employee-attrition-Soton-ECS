from sklearn.cluster import KMeans
import pandas as pd
from collections import Counter
import pygal

datafile = 'data2.xlsx' #the data after Preliminary cleaning(change the character string to int)
data = pd.read_excel(datafile)
#standardization

data = (data - data.mean(axis = 0))/(data.std(axis = 0))
data.columns=['Std'+i for i in data.columns] #表头重命名。
print('the result of standardization')
print(data.ix[0:6,0:5]) # a part of data after standardization
k = 5                       #the number of clusters需要进行的聚类类别数
#data=data.ix[0:10,0:500]

kmodel = KMeans(n_clusters = k)
kmodel.fit(data.ix[0:999,0:27]) # train the mode
#kmodel.cluster_centers_ #the centre of cluster
#kmodel.labels_ #查看各样本对应的类别
print('cluster_centers')
print(kmodel.cluster_centers_)
print('labels')
print( Counter(kmodel.labels_))
centre1=kmodel.cluster_centers_[0,:]
centre1_feature=[centre1[2],centre1[5],centre1[11], centre1[16], centre1[22]]
# change the center from negative to postive
centre1_feature=[i+2 for i in centre1_feature]
# make the radar chart->data visualization
radar_chart = pygal.Radar(fill = True, range=(0,4))
# 添加雷达图的标题
radar_chart.title = 'results'
# 添加雷达图各顶点的含义 随便挑了5个
radar_chart.x_labels = ['department','education','EnvironmentSatisfaction','HourlyRate','MonthlyIncome']

# 绘制两条雷达图区域

radar_chart.add('feature1', centre1_feature)

# save the image ,open the image in the project folder
radar_chart.render_to_file('radar_chart.svg')