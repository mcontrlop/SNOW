import numpy as np
import matplotlib.pyplot as plt 

N = 20000

x = range(N)
y = np.random.rand(N)

fig = plt.figure()
plt.scatter(x,y,c='g',s=3)
plt.show()