import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
df=pd.read_csv('')
d={'Uk':0,'USA':1,'N':2}
df['nationality']=df['nationality'].map(d)
d1={'yes':0,'no':1}
df['Go']=df['Go'].map(d1)
features=['age','experienc','nationality','rank']
X=df[features]
y=df['Go']
dtree=DecisionTreeClassifier
d1tree=dtree.fit(X,y)
tree.plot_tree(d1wtree,feature_names=features)