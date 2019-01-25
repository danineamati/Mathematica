# Daniel Neamati
# Balls in Bins
# 19 January 2019

import random
import matplotlib.pyplot as plt 
import numpy as np 
import sys
import mpmath # gamma function (generalized factorial)
from scipy.special import comb

def drawBalls(n, verbose = False):
	'''We have n balls and n bins. We want to place balls in bins at random.'''
	bins = [-1] * n
	balls = list(range(n))

	while len(balls) > 0:
		binNum = random.choice(list(enumerate(bins)))
		if binNum[1] == -1:
			# The bin is empty and the ball can be placed
			
			bins[binNum[0]] = balls.pop(0)

			if verbose:
				print(binNum[0])
				print(bins)
				print(balls)
				print()
		# Otherwise we just try another bin.

	return bins

def evaluateBins(bins):
	'''Checks how many balls landed in the correct bin. '''
	numCorrect = 0

	for slotNum, ball in enumerate(bins):
		if slotNum == ball:
			numCorrect += 1

	return numCorrect

def main(n, numTrails):
	'''Runs the matching test for n balls/bins and specific number of 
	trials.'''

	results = []
	currAvg = []
	for trial in range(numTrails):
		results.append(evaluateBins(drawBalls(n)))
		currAvg.append(np.mean(results))

	print("Average: ", np.mean(results))

	fig, axes = plt.subplots(2, 1)

	axes[0].plot(currAvg)

	numBins = int(max(results))
	print(set(results))
	print("Number of Bins:", numBins)
	print(np.arange(min(results), max(results) + 1, 1))
	nTot, bins, patches = axes[1].hist(results,  \
		bins = np.arange(min(results), max(results) + 1, 1), \
		color = 'green', density = True)

	mu = np.average(results)
	xpts = np.linspace(- 0.5, max(results))
	y = np.exp(- mu) * ((mu ** (xpts)) / \
				[mpmath.gamma(k) if k != 0 else 1 for k in xpts + 1])
	yfunc = lambda k : np.exp(- mu) * ((mu ** k)/ mpmath.gamma(k + 1))
	# print("Possion Distribution Probability:", y[:20])
	print("Factor:", max(nTot) / max(y))

	axes[1].plot(xpts + 0.5, y, color = "black")

	xpts2 = [i for i in range(numBins + 1) ]
	y2 = np.array([yfunc(k) for k in xpts2])
	# yBinomial = np.array([comb(n, k) * ((1 / n) ** k) * \
	# 							(1 - (1/n)) ** (n - k) for k in xpts2])
	yBinomial = np.array([comb(n, k) / (n **2) for k in xpts2])
	axes[1].scatter(np.array(xpts2) + 0.5, y2, color = "black", zorder = 9)
	axes[1].scatter(np.array(xpts2) + 0.5, yBinomial, color = "red", zorder = 10)

	plt.show()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		n = int(sys.argv[1])
	else:
		n = 10

	if len(sys.argv) > 2:
		numTrails = int(sys.argv[2])
	else:
		numTrails = 30
	
	main(n, numTrails)

