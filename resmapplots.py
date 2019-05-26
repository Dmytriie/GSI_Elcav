#this small script will build three resmap plots on one layout because this was needed for NIMB paper
import numpy as np
import sys
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import curve_fit

data1=np.genfromtxt(sys.argv[1], skip_header=2)
data2=np.genfromtxt(sys.argv[2], skip_header=2)
data3=np.genfromtxt(sys.argv[3], skip_header=2)
data=np.append(np.genfromtxt(sys.argv[1], skip_header=2), np.genfromtxt(sys.argv[2], skip_header=2), axis = 1)
data=np.append(data, np.genfromtxt(sys.argv[3], skip_header=2), axis = 1)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel ('X-position, cm')
ax.set_ylabel ('Sensitivity, R/Q per m')
ax.set_title('Resolution map')
ax.set_xticks(np.arange(-0.02, 0.02, step=0.005))
ax.set_xticks(np.arange(-0.02, 0.02, step=0.001), minor = True)
ax.set_yticks(np.arange(1550, 1950, step=25))
ax.set_yticks(np.arange(1550, 1950, step=5), minor = True)
ax.grid(which = 'both')
ax.errorbar(data1[4, :], data1[0, :], data1[1, :], fmt='bo',capsize = 3, ecolor = 'green', label="70 x 34 cm cavity")
ax.errorbar(data1[4, :], data2[0, :], data2[1, :], fmt='bD',capsize = 3, ecolor = 'red', label="80 x 34 cm cavity")
ax.errorbar(data1[4, :], data3[0, :], data3[1, :], fmt='bs',capsize = 3, ecolor = 'black', label="90 x 34 cm cavity") 		
ax.legend( loc='center left', borderaxespad=0.,   prop={'size': 10}, bbox_to_anchor=(0.65, 0.64))
plt.tight_layout()
plt.savefig('ResMapPlots.pdf', bbox_inches='tight')	
plt.show()
#ax.errorbar(Mydata.ycoord, a, aerr, fmt='o', capsize = 5, ecolor = 'green') 		
#ax.plot(x, circavRQ[10,:], label="Cylindrical cavity") 
#ax.plot(x, elcavRQ[10,:], label="Elliptical cavity")
#ax.legend( loc=5, borderaxespad=0.,   prop={'size': 12})
