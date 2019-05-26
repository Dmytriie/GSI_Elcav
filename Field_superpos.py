#small script to build a plot of filed profiles for the cavities to investigate the cross-talking effect
import numpy as np
import sys
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit

Cildata = np.genfromtxt(sys.argv[1], skip_header = 2)
Eldata = np.genfromtxt(sys.argv[2], skip_header = 2)

fig = plt.figure()
plt.style.use('classic')
matplotlib.rcParams.update({'font.size': 11})
#matplotlib.rcParams['axes.edgecolor'] = 'limegreen'
#matplotlib.rcParams['axes.facecolor'] = 'black'
#matplotlib.rcParams['axes.labelcolor'] = 'limegreen'
#matplotlib.rcParams['xtick.color'] = 'limegreen'
#matplotlib.rcParams['ytick.color'] = 'limegreen'
#matplotlib.rcParams['text.color'] = 'limegreen'
#matplotlib.rcParams['figure.facecolor'] = 'black'

ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Z, cm')
ax.set_ylabel('|Ez/Ez_max|')
ax.set_title(" Field distribution for elliptical and cylindrical cavities ")
xmin = float(np.amin(Cildata[:, 2]))
xmax = float(np.amax(Cildata[:, 2])) 
ymin = float(np.amin(Cildata[:, 5]))
ymax = float(np.amax(Cildata[:, 5]))

ax.plot(Cildata[:, 2], abs(Cildata[:, 5]) / np.amax(abs(Cildata[:, 5])), label="Cylindrical cavity")
ax.plot(Eldata[:, 2], abs(Eldata[:, 5]) / np.amax(abs(Cildata[:, 5])), label="Elliptical cavity")

#ax.plot(Cildata[:, 2], abs(Cildata[:, 5]) , label="Cylindrical cavity")
#ax.plot(Eldata[:, 2], abs(Eldata[:, 5]) , label="Elliptical cavity")

plt.axvline(x=3.75, label='cavity thickness 7.5 cm', c=(1,0,0))
plt.axvline(x=-3.75, c=(1,0,0))

ax.set_xticks(np.arange(-40.0, 41.0	, step=10.0))
ax.set_xticks(np.arange(-40.0, 41.0	, step=5.0),  minor = True)
ax.legend( loc=1, borderaxespad=0.,   prop={'size': 8})
ax.set_yscale('log')
ax.set_yticks([10E0, 10E-1, 10E-2, 10E-3, 10E-4, 10E-5, 10E-6, 10E-7, 10E-8, 10E-9, 10E-10, 10E-11, 10E-12, 10E-13, 10E-14, 10E-15, 10E-16])
ax.grid(which = 'both')
plt.tight_layout()
plt.savefig('CirCav.pdf', bbox_inches='tight')	
plt.show()
