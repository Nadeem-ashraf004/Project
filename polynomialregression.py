from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
import numpy as np
np.random.seed(42)
X=6*np.random.ramd(100,1)-3
y=0.5*X**2+X+2+np.random.randn(1)
poly_feature=PolynomialFeatures(degree=2,include_bais=False)
X_poly=poly_feature.fit_transform(X)
poly_reg = LinearRegression
poly_reg.fit(X_poly,y)
X_new=np.linespace(-3,3,100).reshape(100,1)
X_new_poly=poly_feature.transform(x_new)
y_new=poly_reg.predict(X_new_poly)
plt.scatter(X,y,alpha=0.7,label='Original Data')
plt.plot(X_new,y_new,color='green',linedwidth=2,lable='poly regression')
plt.tilte("polynomial regression")
plt.xlabel('X')
plt.ylabel('y')
plt.show()
