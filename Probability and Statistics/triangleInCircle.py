# Daniel Neamati
# 4 February 2019
# Probability that a triangle inscribed in a circle contains the center

import numpy as np
import matplotlib.pyplot as plt
import random
import sys

def randpoint():
	'''Needs to return a random point on a unit circle.'''
	theta = random.random() * 2 * np.pi
	return (np.cos(theta), np.sin(theta))

def makePairs(ptList):
	'''Given a list of points, it makes tuples of the points in order.
	It also loops.'''
	ptTuples = []
	for i, pt in enumerate(ptList):
		if i < len(ptList) - 1:
			ptTuples.append((pt, ptList[i + 1]))
		else:
			ptTuples.append((pt, ptList[0]))
	return ptTuples

def yInt(coordTuple):
	'''Returns the y - int of the line.'''
	# m = (y2 - y1) / (x2 - x1)
	slope = (coordTuple[1][1] - coordTuple[0][1]) / \
						(coordTuple[1][0] - coordTuple[0][0])
	# yint = m (-x1) + y1
	return slope * (- coordTuple[0][0]) + coordTuple[0][1]

def checkContainsCenter(ptTuples, verbose = False):
	'''Given a list of points checks if the lists surround (0,0).
	Basically via intermediate value theorem.'''
	yPos = 0
	yNeg = 0

	for pair in ptTuples:
		y = yInt(pair)
		if y > 0 and y < 1:
			yPos += 1
		elif y < 0 and y > -1:
			yNeg += 1

	if verbose:
		print(yPos, yNeg)

	if yPos == 1 and yNeg == 1:
		return True
	return False

	# Naive and also wrong...
	# xPos = False
	# xNeg = False
	# yPos = False
	# yNeg = False

	# for pt in ptList:
	# 	x, y = pt
	# 	if x > 0:
	# 		xPos = True
	# 	elif x < 0:
	# 		xNeg = True
	# 	if y > 0:
	# 		yPos = True
	# 	elif y < 0:
	# 		yNeg = True

	# return xPos and xNeg and yPos and yNeg

def runTest(verbose = False):
	'''Selects three random points and checks if the triangle contains the
	center.'''
	ptList = []
	for pt in range(3):
		ptList.append(randpoint())

	tuppairs = makePairs(ptList)

	if verbose:
		print(ptList)
		print(checkContainsCenter(tuppairs))

	return checkContainsCenter(tuppairs)

def largeNTest(numTrials, calcmean = True):
	'''Runs the Test n times and reports the results.'''
	results = []
	currMean = []
	for test in range(numTrials):
		res = runTest()
		results.append(res)

		if calcmean:
			currMean.append(np.mean(results))

	return results, currMean


if __name__ == '__main__':

	if '-v' in sys.argv:
		ptList = []
		for pt in range(3):
			ptList.append(randpoint())
		tuppairs = makePairs(ptList)
		for pair in tuppairs:
			print(pair)
			print(yInt(pair))

		print(checkContainsCenter(tuppairs))

		x, y = zip(*ptList)
		x = list(x)
		y = list(y)
		x.append(ptList[0][0])
		y.append(ptList[0][1])
		
		plt.plot(x, y, 'bo-')
		 
		ax = plt.gca()
		ax.set_xlim((-1,1))
		ax.set_ylim((-1,1))
		ax.axhline(y = 0, color = 'k')
		ax.axvline(x = 0, color = 'k')
		unitcirc = plt.Circle((0,0),1, color = 'g', fill = False)
		ax.add_artist(unitcirc)
		# plt.axis('equal')
		plt.show()


	numTrials = 1000
	if len(sys.argv) < 2:
		numTrials = int(sys.argv[1])

	results, currMean = largeNTest(numTrials)
	print(np.mean(np.array(results)))
	plt.plot(currMean)
	plt.axhline(np.mean(np.array(results)), color = 'black')
	plt.show()

	aggResults = []
	for i in range(numTrials):
		results, currMean = largeNTest(numTrials, False)
		aggResults.append(np.mean(np.array(results)))

	print(np.mean(aggResults))
	plt.plot(aggResults)
	plt.show()
