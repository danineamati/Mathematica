# Test of 2D Random Walk
# Daniel Neamati
# 18 February 2019

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

import sys
import numpy as np
import random

def walkOnce(loc):
	'''Moves one step.'''
	row, col = loc
	stepRow = random.choice([-1, 1])
	stepCol = random.choice([-1, 1])
	return (row + stepRow, col + stepCol)

def randomWalk(numsteps):
	'''Random walk (2D) with n steps. Returns the steps'''
	
	currentLoc = (0,0)
	steps = [currentLoc]

	for i in range(numsteps):
		currentLoc = walkOnce(currentLoc)
		steps.append(currentLoc)

	return steps


def main(numsteps, numTrails, gradient = False):

	allSteps = []
	for i in range(numTrails):
		steps = randomWalk(numsteps)
		xPts, yPts = zip(*steps)
		xPts = np.array(xPts)
		yPts = np.array(yPts)
		allSteps.append([xPts,yPts])

	fig, axes = plt.subplots(1, 1)

	# plt.plot(xPts,yPts)
	plt.axhline(y = 0, color = 'k')
	plt.axvline(x = 0, color = 'k')
	plt.axhline(y = numsteps ** (1/2), color = 'k', linestyle = '--')
	plt.axvline(x = numsteps ** (1/2), color = 'k', linestyle = '--')
	plt.axhline(y = -numsteps ** (1/2), color = 'k', linestyle = '--')
	plt.axvline(x = -numsteps ** (1/2), color = 'k', linestyle = '--')

	minX, maxX, minY, maxY = 0, 0, 0, 0

	for i, step in enumerate(allSteps):
		x, y = step
		if min(x) < minX:
			minX = min(x)
		if max(x) > maxX:
			maxX = max(x)
		if min(y) < minY:
			minY = min(y)
		if max(y) > maxY:
			maxY = max(y)

		if gradient:
			count = np.array(list(zip(*list(enumerate(x))))[0])

			points = np.array([x, y]).T.reshape(-1, 1, 2)
			segments = np.concatenate([points[:-1], points[1:]], axis=1)
			norm = plt.Normalize(0, max(count))
			lc = LineCollection(segments, cmap='hsv', norm=norm)
			# Set the values used for colormapping
			lc.set_array(count)
			lc.set_linewidth(2)
			line = axes.add_collection(lc)

			if i == 0:
				fig.colorbar(line, ax=axes)
		else:
			plt.plot(x,y, label="Path {}".format(i))
			plt.legend()

	axes.set_xlim(min(minX, -numsteps/2), max(maxX, numsteps/2))
	axes.set_ylim(min(minY, -numsteps/2), max(maxY, numsteps/2))
	plt.show()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(int(sys.argv[1]), 4)
	else:
		main(10, 4)