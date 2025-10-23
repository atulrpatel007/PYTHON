import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A","B","C","D","E","F"])
y = np.array([2,3,4,2,1,0])
plt.bar(x,y)
plt.show()
plt.barh(x,y)
plt.show()
x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()
y = np.array([35,25,25,15])
mylabels = ["Apple","Banana","Cherry","Dates"]
plt.pie(y,labels=mylabels,startangle=90)
plt.show()