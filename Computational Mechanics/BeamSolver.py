# Beam solver from Mathematica, but now in python.
# Daniel Neamati
# 24 December 2018

import numpy as np
import sympy
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import csv
import pandas as pd
import math

def solveReactions(forceListDF):
	'''Solves a system of equations based on the number of equations. '''
	# numEq = forceListDF.shape[0]
	# matA = np.ones(forceListDF.shape)
	# print(matA)
	sumForces = 0
	sumMoment = 0
	for val in forceListDF.values:
		if not math.isnan(val[1]):
			sumForces += val[1]
			sumMoment += val[2] * val[1]

	matA = [
	[1, 1, sumForces],
	[forceListDF.values[0][2], forceListDF.values[1][2], sumMoment]
	]
	rrefA = sympy.Matrix(matA).rref()

	print(matA)

	return rrefA[0][0,2], rrefA[0][1,2]

def getSimpleForceDist(distA, distB, hA, hB):
	return lambda x : ((hB - hA)/(distB - distA)) * (x - distA) + hA \
								if x > distA and x < distB else 0.0

def getReactionForceFunction(magnitude, location):
	return lambda x : magnitude if x >= location else 0.0

def genCSVforDistForce(forceDistDF, file, outDF):
	'''Takes an array of the given values and modifies the dataframe 
	in place'''

	# We only want to append the relevant about the force distributions
	for qi in forceDistDF.values:
		area, centroid = genDistForce(qi[1], qi[2], qi[3], qi[4])
		outDF.loc[outDF.shape[0] + 1] = [qi[0], area, centroid]
	print(outDF)
		
def genDistForce(distA, distB, hA, hB):
	'''
	Assumes a trapezoid
	Input: The start of the distibuted force, the height on both sides

	Returns the info about a distributed force in the form:
	"qi", area of force, centroid of force
	'''
	funct = getSimpleForceDist(distA, distB, hA, hB)
	area = integrate.quad(lambda x: funct(x), distA, distB)
	centArea = integrate.quad(lambda x: x * funct(x), distA, distB)
	centroid = centArea[0] / area[0]

	return area[0], centroid

def solveShearForce(forceDistDF, forceListDF, xpts):
	''' Use the getSimpleForceDist function and integrate with the specified
	bounds. Add these together to get the shear force function.
	Then we plot the shear force. '''

	shearAtXval = np.zeros(xpts.shape)

	qDist = lambda x : sum(getSimpleForceDist(qi[1], qi[2], qi[3], qi[4])(x)\
								 for qi in forceDistDF.values)
	reactShear = lambda x :	sum(getReactionForceFunction(ri[1], ri[2])(x) \
								 for ri in forceListDF.values[:2])

	for index, x in enumerate(xpts):
		vFunc = lambda x: integrate.quad(lambda s : qDist(s), xpts[0], x)
		shearAtXval[index] = vFunc(x)[0] - reactShear(x)

	return shearAtXval

def solveShearAndBendingMoment(forceDistDF, forceListDF, xpts): 
	''' Use the getSimpleForceDist function and integrate with the specified
	bounds. Add these together to get the shear force function.
	Then we plot the shear force. '''

	bmomentAtXval = np.zeros(xpts.shape)
	shearAtXval = np.zeros(xpts.shape)

	qDist = lambda x : sum(getSimpleForceDist(qi[1], qi[2], qi[3], qi[4])(x)\
								 for qi in forceDistDF.values)
	reactShear = lambda x :	sum(getReactionForceFunction(ri[1], ri[2])(x) \
								 for ri in forceListDF.values[:2])

	initial = xpts[0]

	for index, x in enumerate(xpts):
		# if False:
		# 	if index == 0:
		# 		pass
		# 	else:
		# 		# To avoid calculating the shear force and bending moment plots
		# 		# from the origin, we instead use the intermediate values.
		# 		vFunc = lambda x: integrate.quad(lambda s : qDist(s), \
		# 							xpts[index - 1], x)
		# 		# mFunc = lambda x: integrate.quad(lambda s : \
		# 		# 					vFunc(s)[0] - reactShear(s), \
		# 		# 					xpts[index - 1], x)

		# 		shearAtXval[index] = shearAtXval[index - 1] + \
		# 										vFunc(x)[0] - reactShear(x)
		# 		# bmomentAtXval[index] = bmomentAtXval[index - 1] + \
		# 		# 								mFunc(x)[0]
		# else:
		vFunc = lambda x: integrate.quad(lambda s : qDist(s), initial, x)
		mFunc = lambda x: integrate.dblquad(lambda s, s2 : \
							qDist(s), initial, x,\
							lambda s2: initial, lambda s2: x)[0] -\
						integrate.quad(lambda s: reactShear(s), initial, x)[0]

		shearAtXval[index] = vFunc(x)[0] - reactShear(x)
		bmomentAtXval[index] = mFunc(x)

		if index % 5 == 0:
			print("At index ", index, " with x val ", x)

	return shearAtXval, bmomentAtXval

def main(forceListDF, forceDistDF):
	print()
	print(forceListDF)

	print("Beginning Plotting...")

	xpts = np.linspace(0,10,100)
	fig, ax = plt.subplots()
	shearBendVals = solveShearAndBendingMoment(forceDistDF, forceListDF, xpts)
	ax.plot(xpts, shearBendVals[0])
	ax.plot(xpts, shearBendVals[1])

	#ax.grid(True, which = 'both')
	ax.axhline(y = 0, color = 'k', linewidth = 0.5)

	for qi in forceDistDF.values:
		ax.axvline(x = qi[1], color = 'k', linewidth = 0.5)
		ax.axvline(x = qi[2], color = 'k', linewidth = 0.5)

	plt.show()


if __name__ == '__main__':
	# The distributed force has to be of the form
	# [["Force Name", magnitude, [direction vec], [centroid vec], 
	#	true if Distribution, function for distribution]]
	forceDistDF = pd.read_csv('distBeam.csv', header = None)
	forceListDF = pd.read_csv('dataBeam.csv')
	# forceList = forceListDF.values

	genCSVforDistForce(forceDistDF, 'dataBeam.csv', forceListDF)

	forceListDF.loc[0,'Magnitude'], forceListDF.loc[1,'Magnitude'] =\
			solveReactions(forceListDF)

	main(forceListDF, forceDistDF)

	