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

	return -rrefA[0][0,2], -rrefA[0][1,2]

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
		outDF.loc[outDF.shape[0]] = [qi[0], area, centroid]
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

def getForceDist(forceDistDF, xpts):
	'''Returns an array for the total shear force.'''
	qDist = lambda x : sum(getSimpleForceDist(qi[1], qi[2], qi[3], qi[4])(x)\
								 for qi in forceDistDF.values)
	return [qDist(x) for x in xpts]

def getReactionPlot(forceListDF, xpts):
	'''Returns an array for the total shear force.'''
	reactShear = lambda x :	sum(getReactionForceFunction(ri[1], ri[2])(x) \
								 for ri in forceListDF.values[:2])
	return [reactShear(x) for x in xpts]

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

	# qDist = lambda x : sum(getSimpleForceDist(qi[1], qi[2], qi[3], qi[4])(x)\
	# 							 for qi in forceDistDF.values)
	# reactShear = lambda x :	sum(getReactionForceFunction(ri[1], ri[2])(x) \
	# 							 for ri in forceListDF.values[:2])

	initial = xpts[0]
	print("initial pt: ", initial)

	for index, x_curr in enumerate(xpts):
		for indQ, qi in enumerate(forceDistDF.values):
			if x_curr >= qi[1] and x_curr <= qi[2]:
				# In the middle of the force distribution.
				# print("Within the", qi[0], "force distribution")
				lower_bound = qi[1]
				newShear = integrate.quad(lambda s : \
					getSimpleForceDist(qi[1], qi[2], qi[3], qi[4])(s), \
					lower_bound, x_curr)[0]
				shearAtXval[index] += newShear

				newBMoment = integrate.dblquad(lambda s2, s : \
					getSimpleForceDist(qi[1], qi[2], qi[3], qi[4])(s), \
					lower_bound, x_curr, \
					lambda s2: lower_bound, lambda s2: s2)[0]

				bmomentAtXval[index] += newBMoment

			elif x_curr > qi[2]:
				# You want to include the previous contribution of that 
				# force distribution. This is just the force from that value.
				# print("Need to include magnitude of ", qi[0], "which is ", \
				# 	forceListDF.loc[indQ + 2, "Magnitude"])
				shearAtXval[index] += forceListDF.loc[indQ + 2, "Magnitude"]

				lower_bound = qi[1]
				upper_bound = qi[2]
				newBMoment = integrate.dblquad(lambda s2, s : \
					getSimpleForceDist(qi[1], qi[2], qi[3], qi[4])(s), \
					lower_bound, upper_bound, \
					lambda s2: lower_bound, lambda s2: s2)[0]

				bmomentAtXval[index] += newBMoment

		for indReact, ri in enumerate(forceListDF.values[:2]):
			if x_curr >= ri[2]:
				# Past the reaction so we need to include it.
				shearAtXval[index] += ri[1]
				bmomentAtXval[index] += (x_curr - ri[2]) * ri[1]
				
		if (index + 1) % 100 == 0:
			print("At index ", index + 1, " with x val ", x_curr)

	return shearAtXval, bmomentAtXval

def main(forceListDF, forceDistDF):
	print()
	print(forceListDF)
	print()
	print(forceDistDF)
	print()
	print("Solving for Shear Force and Bending Moment \n")

	xpts = np.linspace(0,10,400)
	fig, axes = plt.subplots(2, 2)
	fig.tight_layout()

	qDist = getForceDist(forceDistDF, xpts)
	rReact = getReactionPlot(forceListDF, xpts)

	# The first argument is shear and the second is bending moment
	shearBendVals = solveShearAndBendingMoment(forceDistDF, forceListDF, xpts)

	print("Beginning Plotting...\n")
	axes[0,1].plot(xpts, qDist, color = 'blue')
	axes[1,1].plot(xpts, rReact, color = 'blue')
	axes[0,0].plot(xpts[:-1], shearBendVals[0][:-1], color = 'green')
	axes[1,0].plot(xpts[:-1], shearBendVals[1][:-1], color = 'orange')

	axes[0,1].set_title("Force Distribution on the Beam")
	axes[1,1].set_title("Reaction Distribution on the Beam")
	axes[0,0].set_title("Shear Force in the Beam")
	axes[1,0].set_title("Bending Moment in the Beam")

	for ax in axes.flatten():
		ax.axhline(y = 0, color = 'k', linewidth = 0.5)

		for qi in forceDistDF.values:
			ax.axvline(x = qi[1], color = 'k', linewidth = 0.5)
			ax.axvline(x = qi[2], color = 'k', linewidth = 0.5)

		ax.set_xlim(forceDistDF.values[0][1],\
			forceDistDF.values[len(forceDistDF.values) - 1][2])

		# ax.grid(True, which='both')

	plt.show()


if __name__ == '__main__':
	# The distributed force has to be of the form
	# [["Force Name", magnitude, [direction vec], [centroid vec], 
	#	true if Distribution, function for distribution]]
	forceDistDF = pd.read_csv('distBeam.csv')
	forceListDF = pd.read_csv('dataBeam.csv')

	genCSVforDistForce(forceDistDF, 'dataBeam.csv', forceListDF)

	forceListDF.loc[0,'Magnitude'], forceListDF.loc[1,'Magnitude'] =\
			solveReactions(forceListDF)

	main(forceListDF, forceDistDF)

	