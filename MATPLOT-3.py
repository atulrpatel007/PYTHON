import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(3,2,1)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(3,2,2)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(3,2,3)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(3,2,4)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(3,2,5)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(3,2,6)
plt.plot(x,y)

plt.show()