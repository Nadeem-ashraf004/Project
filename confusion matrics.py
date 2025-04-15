import matplotlib.pyplot as plt
import numpy as np
from sklearn import matrics
actual=np.random.binomial(1,.9,size=1000)
predict=np.random.binomial(1,.9,size=1000)
confusion_matrix=matrics.confusion_matrix(actual,predict)
cm_display=matrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix,cm_display_lable=[0,1])
cm_display.plot()
plt.show