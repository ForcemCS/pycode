import pandas as pd
import numpy as  np 
import matplotlib as mpl
import matplotlib.pyplot as plt


#print(mpl.style.available)

mpl.style.use('seaborn-v0_8-darkgrid')

fig, ax  = plt.subplots()
# plt.show()

x_pts = np.linspace(-2 * np.pi , 2 * np.pi , 100)
y_pts = np.sin(x_pts)

##在画布上画线图
ax.plot(x_pts,y_pts, label = 'sin(x)')
ax.plot(x_pts, np.cos(x_pts), label = 'cos(x)')


ax.set_xlabel('X-AXIS ')
ax.set_ylabel('y-AXIS ')

ax.set_title('Trigonometric Function Graph')
ax.legend()
plt.show()