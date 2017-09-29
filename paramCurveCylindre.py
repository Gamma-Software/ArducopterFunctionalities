import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

#theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#z = np.linspace(-2, 2, 100)
#r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)

a=10
b=1
p=1
t=np.linspace(0, 10*np.pi,1000)
x=a*np.cos(t)
y=p*a*np.sin(t)
z=b*t

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
