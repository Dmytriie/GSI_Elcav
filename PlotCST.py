#!/usr/bin/python3
#This program was created to build 2D plots of the R/Q values which were prepared by CST2018. Also one will have linearity checking plot for 0.0 horizontal line
#Input - .txt file with strings with one number. Output - 2Dplot
#Idea of the input file structure is given by CST modelling. Here - we have loop over all y for each x

#"All X for every Y data" means next data structure:
#	R/Q(X1,Y1) R/Q(X2,Y1) ... R/Q(Xn,Y1)
#	R/Q(X1,Y2) R/Q(X2,Y2) ... R/Q(Xn,Y2)
#           ...
#	R/Q(X1,Yn) R/Q(X2,Yn) ... R/Q(Xn,Yn)

#"All Y for every X data" means next data structure:
#	R/Q(X1,Y1) R/Q(X1,Y2) ... R/Q(X1,Yn)
#	R/Q(X2,Y1) R/Q(X2,Y2) ... R/Q(X2,Yn)
#           ...
#	R/Q(Xn,Y1) R/Q(Xn,Y2) ... R/Q(Xn,Yn)
#	difference one can see when "meshgrid" will be applied

import fileinput
import numpy as np
import sys
from math import sqrt
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
matplotlib.rcParams.update({'font.size': 15})
import os.path

def fit_function(x, a, b):
	"""
	Line 
	"""
	x = np.asarray(x)
	return b + a *x 
	
class PlotCST:
	def __init__(self):
		self.datafile = sys.argv[1]
		self.direction = sys.argv[2]
		self.line = float(sys.argv[3])				
		self.xstart = float(sys.argv[4])
		self.xstop = float(sys.argv[5])
		self.xsteps = int(sys.argv[6])
		self.ystart = float(sys.argv[7])
		self.ystop = float(sys.argv[8])
		self.ysteps = int(sys.argv[9])
		self.xcoord = []
		self.ycoord = []
		self.new_file = self.datafile.replace(".txt", "dot.txt")
		self.old_symbol = ','
		self.new_symbol = '.'

	def symbol_change(self):
		with open(self.new_file, "w", encoding = 'utf-8') as f:
			for line in fileinput.input([self.datafile], inplace = False):
				f.write(line.replace(self.old_symbol, self.new_symbol))
		self.datafile = self.new_file

	def get_CST_data(self): #this function returns XY coordinates for mesh and reshaped R/Q data
		self.dataset = np.genfromtxt( self.datafile, skip_header = 15)#skip internal file description + first point created by first calculation of the field
		self.dataset = self.dataset.reshape(len(self.dataset), 2) #for dividing the string number and data

		for x in range(self.xsteps):
			self.xcoord.append(round ( self.xstart + (self.xstop - self.xstart) / (self.xsteps - 1) * x ,4))
		for y in range(self.ysteps):
			self.ycoord.append(round ( self.ystart + (self.ystop - self.ystart) / (self.ysteps - 1) * y ,4))

		dataset=self.dataset[:, 1].reshape(len(self.ycoord), len(self.xcoord))  #for all Y for every X data
		dataset=np.transpose(dataset) #Uncomment if you work with  "All X for every Y data"

		return self.xcoord, self.ycoord, dataset

	def linear_fit(self, dataset, line): # do linear fit and get errors of parameters
		linecounter = 0
		dataarray = []
		if self.direction == 'h': #when we check linearity along horizontal axis
			x = self.xcoord # already pick an array of all X coordinates
			for coordinate in self.ycoord: #for every position of horizontal fitting
				if coordinate == float(line): #when we found our line
					RQ = dataset [linecounter,:] # to use RQ data from all Y for certain line	
					break
				else:
					linecounter += 1 #our data is deeper in array

		if self.direction == 'v': #when we check linearity along vertical axis
			x = self.ycoord # already pick an array of all Y coordinates
			for coordinate in self.xcoord: #for every position of vertical fitting
				if coordinate == float(line): #when we found our line
					RQ = dataset [:, linecounter] # to use RQ data from all X for certain line
					break
				else:
					linecounter += 1 #our data is deeper in array
		#print (RQ)
		#print (x)
		perr=[]
		#linfunc = lambda a,b,x: a*x+b
		#popt, pcov = curve_fit(linfunc, x, RQ) #popt - optimal Hi-square min values for the fit parameters in this point
			
		slope = 34
		b = -190
		p = (b, slope)
		#popt, pcov = curve_fit(fit_function, x, RQ)
		popt, pcov = curve_fit(fit_function, x, RQ, p0=p)	
		fit = [popt[1]*X + popt[0] for X in x] # for every x coordinate fit function = a*x+b
		perr = np.sqrt(np.diag(pcov))
		'''
		for i in range(len(x)):
			perr.append(np.sqrt( (RQ[i] - (popt[1]*x[i] + popt[0]) )**2 )) #RMS formula
		print(perr)
		'''
		return x, RQ, fit, popt, perr
		
	def rqmap_fitplot(self): #function to check if everything works as it has to. Change it on your own.
		Mydata = PlotCST() #read all parameters from terminal
		mesharray = Mydata.get_CST_data() #get mesh coordinates and R/Q
		X = mesharray[0]
		Y = mesharray[1]
		Z = mesharray[2]
		x, z, fit, popt, perr = Mydata.linear_fit(mesharray[2], Mydata.line) # get array of x-coordinate, R/Q according to Y line and X point and A and B from fit F=A*x+B
		#print("a = ", popt[1], " b = ", popt[0])
		#print("as = ", perr[1], "bs = ", perr[0])
		
		matplotlib.rcParams.update({'font.size': 12})
		#matplotlib.rcParams['axes.edgecolor'] = 'limegreen'
		#matplotlib.rcParams['axes.facecolor'] = 'black'
		#matplotlib.rcParams['axes.labelcolor'] = 'limegreen'
		#matplotlib.rcParams['xtick.color'] = 'limegreen'
		#matplotlib.rcParams['ytick.color'] = 'limegreen'
		#matplotlib.rcParams['text.color'] = 'limegreen'
		#matplotlib.rcParams['figure.facecolor'] = 'black'
		matplotlib.rcParams['figure.figsize'] = (8, 3)
		#save_path = '/home/skye/Documents/_My_Science/GSIReport2.05.2019R3DALINAC/images/'
		'''
		plt.xlabel('X-position, m')
		plt.ylabel('Y-position, m')
		plt.title('RQ map')
		plt.contourf(X, Y, Z, 100)
		plt.colorbar()
		plt.tight_layout()
		plt.savefig('2pipeR3Elbigcf.pdf')
		plt.show()
		'''
		plt.xlabel('X-position, m')
		plt.ylabel('Y-position, m')
		plt.title('RQ map')
		plt.contour(X, Y, Z, 100)
		plt.colorbar()
		plt.tight_layout()
		plt.savefig('Dael80.pdf')
		plt.show()
		
		plt.xlabel('X-position, m')
		plt.ylabel('R/Q along center left to the right')
		plt.plot(x, z, 'r-')
		plt.plot(x, fit_function(x, popt[0], popt[1]), 'g--')
		plt.tight_layout()
		plt.title('Resolution map')
		plt.savefig('Dael80Lin.pdf') #, bbox_inches='tight'			
		plt.show()
		
if __name__ == '__main__':
	M=PlotCST()	
	M.rqmap_fitplot()
