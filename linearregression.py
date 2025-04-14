from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
X=2*np.random.rand(100,1)
Y=4+3*X+np.random.randn(100,1)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
model=LinearRegression
model.fit(X_train,Y_train)
Y_pred=model.predict(X_test)
plt.scatter(X,Y,alpha=0.7,label='Original data')
plt.plot(X_test,Y_pred,color='red',linewidth='Linear regression')
plt.title('linear regression in python ')
plt.ylabel('Y')
plt.xlabel('X')
plt.show()
mse=mean_squared_error(Y_test,Y_pred)
print(f"mean square error :{mse}")
