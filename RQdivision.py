#No idea what this code is doing))
import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib
import math

#quality factors of cavities
elcavQ = 18334.797 
circavQ = 19278.36
#every datafile after division shows the shunt impedance of the cavity. Reshaping is done for the map
elcavRQ = np.divide(np.genfromtxt( sys.argv[1], skip_header = 15)[:, 1].reshape(21, 21), elcavQ)
circavRQ = np.divide(np.genfromtxt( sys.argv[2], skip_header = 15)[:, 1].reshape(21, 21), circavQ)
datafile = np.divide(circavRQ, elcavRQ)
np.savetxt("ratiofile.txt", datafile)

#coordinate net
x=np.arange(-5, 5.5, 0.5)
y=np.arange(-1.5, 1.65, 0.15)
#square root from the ratio of shunt impedances give me ratio of voltages between cavities.
#this string will be used for the signal ratio in GNU radio
print("X coordinate: ", x[10])
print("Voltage ratio for all the points: ", np.sqrt(datafile[10 ,:]) )

#nice plot of R/Q map
matplotlib.rcParams.update({'font.size': 12})
'''
plt.xlabel('X-position, cm')
plt.ylabel('Y-position, cm')
plt.title('Shunt impedances ratio map')
plot=plt.contourf(x, y, datafile, 100)
for p in plot.collections:#to avoid contor polygons lines for pdf quality pictures
    p.set_edgecolor("face")#make edge lines the same colour as area under the colour
plt.colorbar()
plt.tight_layout()
plt.savefig('RshuntMap.pdf', bbox_inches='tight')	
'''
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel ('X-position, cm')
ax.set_ylabel ('Shunt impedance, Ohm')
ax.set_title('Shunt impedance - position dependency')
ax.set_xticks(np.arange(-5, 5.5	, step=1))
ax.set_xticks(np.arange(-5, 5.5	, step=0.25), minor = True)
ax.set_yticks(np.arange(0, 0.008, step=0.001))
ax.set_yticks(np.arange(0, 0.008, step=0.00025), minor = True)
ax.grid(which = 'both')

ax.plot(x, circavRQ[10,:], label="Cylindrical cavity") 
ax.plot(x, elcavRQ[10,:], label="Elliptical cavity")
ax.legend( loc=5, borderaxespad=0.,   prop={'size': 12})
plt.tight_layout()
plt.savefig('Shunt-position.pdf', bbox_inches='tight')	

#'''

plt.show()

