import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure
ax = plt.subplot()

x = np.linspace(0,2*np.pi,1000)
y = np.sin(x)

ax.plot(x,y)
ax.grid()

plt.show()
# plt.savefig('Sinus.eps', format='eps')