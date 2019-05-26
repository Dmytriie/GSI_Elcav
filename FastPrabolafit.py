#Small script to make plot of my a/aerr measurements for different elliptical cavities.
import numpy as np
import sys
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import curve_fit
from matplotlib.lines import Line2D

dots = np.array([(1,25.26),(2,37.85),(3,24.89), (4, 25.78), (5, 39.31), (6, 39.85), (7, 29.87), (8, 39.48), (9, 24.68) ])
x = dots[:,0]
y = dots[:,1]
matplotlib.rcParams.update({'font.size': 16})
matplotlib.rcParams['axes.edgecolor'] = 'limegreen'
matplotlib.rcParams['axes.facecolor'] = 'black'
matplotlib.rcParams['axes.labelcolor'] = 'limegreen'
matplotlib.rcParams['xtick.color'] = 'limegreen'
matplotlib.rcParams['ytick.color'] = 'limegreen'
matplotlib.rcParams['text.color'] = 'limegreen'
matplotlib.rcParams['figure.facecolor'] = 'black'
#matplotlib.rc('axes',edgecolor='r')
'''
plt.plot(x[0],y[0],color='#FF0000', marker = 'X')
plt.plot(x[1],y[1],color='#11CC00', marker = 'X')
plt.plot(x[2],y[2],color='#0000FF', marker = 'X')
plt.plot(x[3],y[3],color='#FF00FF', marker = 'X')
plt.plot(x[4],y[4],color='#CCC400', marker = 'X')
plt.plot(x[5],y[5],color='#CC0065', marker = 'X')
plt.plot(x[6],y[6],color='#0069CC', marker = 'X')
plt.plot(x[7],y[7],color='#056B00', marker = 'X')
plt.plot(x[8],y[8],color='#0016CC', marker = 'X')
'''
plt.plot(x,y,'b:', markerfacecolor = '#FF0000', markeredgecolor = '#FF0000', linewidth=2, linestyle = '-',markersize=6, marker = 'o')
#plt.tick_params(axis='x', colors='black')

plt.xlabel('Simulation number')
plt.ylabel('Resolution/Resolution error')
plt.title('Resolution to Resolution error ratio')
plt.tight_layout()
plt.savefig('SimRes.eps', bbox_inches='tight')	
plt.savefig('SimRes.pdf', bbox_inches='tight')
plt.show()
