import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale=StandardScaler

df=pd.raed_csv('file name')
X=df[['Age' , 'sex']]

scaledx=scale.fit_transform(X)
print(X)