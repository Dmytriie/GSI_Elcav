#!/usr/bin/python3
#This program was created to build 1D plot of the R/Q  Resolution values from data given  by CST2019.
#IMagine that you have R/Q data inside the rectangular pipe. Data was taken as:
#	R/Q(X1,Y1) R/Q(X2,Y1) ... R/Q(Xn,Y1)
#	R/Q(X1,Y2) R/Q(X2,Y2) ... R/Q(Xn,Y2)
#           ...
#	R/Q(X1,Yn) R/Q(X2,Yn) ... R/Q(Xn,Yn)
#program will take all points along the bottom horizontal line and fit them. Then give you slope and error of the slope
#slope is a resolution of a given cavity whereas slope error is the resolution error. We demand resolution/resolution error to be the smallest possible
#As a result user will have  resolution map. It will be saved as .pdf
from PlotCST import * #importing all methods from class PlotCST written for the data processing
import numpy as np
import sys
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.optimize import curve_fit

#several parameters could be adjusted in matplotlib. Basically - everything
#wherever we want to have a resolution map - we have to have array of resolutions for every y coordinate and binded errors
matplotlib.rcParams.update({'font.size': 12})
#matplotlib.rcParams['axes.edgecolor'] = 'limegreen'
#matplotlib.rcParams['axes.facecolor'] = 'black'
#matplotlib.rcParams['axes.labelcolor'] = 'limegreen'
#matplotlib.rcParams['xtick.color'] = 'limegreen'
#matplotlib.rcParams['ytick.color'] = 'limegreen'
#matplotlib.rcParams['text.color'] = 'limegreen'
#matplotlib.rcParams['figure.facecolor'] = 'black'		
matplotlib.rcParams['figure.figsize'] = (8, 3)	
def resolutionmap():
	a=[]
	aerr=[]
	b=[]
	berr=[]
	dataarray1=[]
	RQ=[]
	Mydata = PlotCST() #read all parameters from terminal
	mesharray = Mydata.get_CST_data() #get mesh coordinates and R/Q
	Z = mesharray[2]
	print (Mydata.direction)
		#in case of vertical linearity measurements - uncomment this		
	if Mydata.direction != 'h':
		for xline in Mydata.xcoord:
			x, z, fit, popt, perr = Mydata.linear_fit(Z, xline) # get array of x-coordinate, R/Q according to Y line and X point and A and B from fit F=A*x+B
			a.append(popt[1]*-1)
			aerr.append(perr[1])
			b.append (popt[0])
			berr.append(perr[0])		
		#print("a = ", a, " b = ", b, "as = ", aerr, "bs = ", berr)
		#in case you need to save your data about fitting parameters - uncomment folliwing lines
		#dataarray1 = np.concatenate((a, aerr, b, berr, Mydata.xcoord), axis=0)
		#dataarray1 = dataarray1.reshape (5,21)
		#np.savetxt(sys.argv[1] + 'Vdata' + '.txt', dataarray1.T, header="A                         Aerr                         B                         Berr                         X  ", comments='Y = A*x + B'+ '\n')
		print("A = ", round(sum(np.abs(a)), 0), "Aerr = ", round(sum(np.abs(aerr)), 0)*2, "A/Aerr = ", round(sum(np.abs(a))/(2*sum(np.abs(aerr))), 2) )
		Y, X = np.meshgrid(mesharray[1], mesharray[0])
		plt.xlabel('X-position, m')
		plt.ylabel('Sensitivity, R/Q per m')
		plt.errorbar(Mydata.xcoord, a, aerr, fmt='o', capsize = 5, ecolor = 'green')
		plt.title('Resolution map')
		#plt.savefig(sys.argv[1] +'V.png', bbox_inches='tight')
		#plt.savefig(sys.argv[1] +'V.eps', bbox_inches='tight')
		plt.savefig(sys.argv[1] +'V.pdf', bbox_inches='tight')
		plt.show()
	
	if Mydata.direction == 'h':
		for yline in Mydata.ycoord:
			x, z, fit, popt, perr = Mydata.linear_fit(Z, yline) # get array of x-coordinate, R/Q according to Y line and X point and A and B from fit F=A*x+B
			a.append(popt[0]*-1)
			aerr.append(perr[0])
			b.append (popt[1])
			berr.append(perr[1])
		#print("a = ", a, " b = ", b, "as = ", aerr, "bs = ", berr)
		#in case you need to save your data about fitting parameters - uncomment folliwing lines
		#dataarray1 = np.concatenate((a, aerr, b, berr, Mydata.ycoord), axis=0)
		#dataarray1 = dataarray1.reshape (5,21)
		#np.savetxt(sys.argv[1] + 'Hdata' + '.txt', dataarray1, header="A                         Aerr                         B                         Berr                             X", comments='Y = A*x + B'+ '\n')
		#print ( np.sum(a)/np.sum(aerr), np.sum(berr) )
		print("A = ", round( np.abs(a)[len(a)//2], 2), "Aerr = ", round(aerr[len(a)//2], 2)*2, "A/Aerr = ", round(np.abs(a)[len(a)//2]/(2*aerr[len(a)//2]), 2),  )
		'''
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)
		ax.set_xlabel ('X-position, cm')
		ax.set_ylabel ('Sensitivity, R/Q per m')
		ax.set_title('Resolution map')
		#ax.set_xticks(np.arange(Mydata.xstart, Mydata.stop+	, step=0.02))
		#ax.set_xticks(np.arange(-5, 5.5	, step=0.25), minor = True)
		ax.set_yticks(np.arange(1600, 1800, step=50))
		ax.set_yticks(np.arange(1600, 1800, step=10), minor = True)
		ax.grid(which = 'both')
		ax.errorbar(Mydata.ycoord, a, aerr, fmt='o', capsize = 5, ecolor = 'green') 
		'''
		#'''
		#save_path = '/home/skye/Documents/_My_Science/GSIReport2.05.2019R3DALINAC/images/'
		Y, X = np.meshgrid(mesharray[1], mesharray[0])
		plt.xlabel('Y-position, m')
		plt.ylabel('Sensitivity, R/Q per m')
		plt.errorbar(Mydata.ycoord, np.abs(a), aerr, fmt='o', capsize = 5, ecolor = 'green')
		plt.title('Resolution map')
		#plt.savefig(sys.argv[1] +'H.png', bbox_inches='tight')
		#plt.savefig(sys.argv[1] +'H.eps', bbox_inches='tight')
		plt.savefig('ResmapDael80.pdf', bbox_inches='tight')
		#'''
		plt.show()

if __name__ == '__main__':

	resolutionmap()

	
