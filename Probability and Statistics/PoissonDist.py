# Probability Fun: Project 4 - Poisson Distribution.
# Daniel Neamati
# 28 December 2018

import matplotlib.pyplot as plt 
import numpy as np 
import random
import sys
import mpmath # gamma function (generalized factorial)

from FreqVsProb import randomPick


def possionDist(numTrials, numTosses, mu):
	'''We want to model a poisson distribution from a symmetric binomial 
	distribution. We want to show that for large number of trials, the 
	binomial histogram converges to the poisson distribution. 

	We do this with a (fair) coin toss.'''

	results = []

	# For tracking progress
	verboseThres = int(numTrials/10)

	for i in range(numTrials):
		trial = []
		for j in range(numTosses):
			# Flip a fair coin. Did it flip heads?
			trial.append(randomPick(1, int(numTosses / mu)))
		# Append the average number that flipped heads.
		results.append(np.sum(trial))

		if (i + 1) % verboseThres == 0:
			print("At iteration ", i + 1)

	print("Select results:", results[:20])

	return results


def main(numTrials, numTosses, mu):

	results = possionDist(numTrials, numTosses, mu)
	
	# Plot the binomial distibution of results
	numBins = int(max(results) - min(results))
	n, bins, patches = plt.hist(np.array(results), numBins, density = 1)
	print("Values in bins:", n)
	print("Sum of these values:", sum(n))

	# Now we plot poisson distribution
	# sigma = np.std(results)
	mu = np.average(results)
	xpts = np.linspace(- 0.5, max(results))
	# xpts = list(range(max(results)))
	# print(xpts)
	# zVals = (xpts - 0.5 - mu) / sigma

	# y = np.exp(- mu) * ((mu ** xpts)/ [np.math.factorial(x) for x in xpts])
	y = np.exp(- mu) * ((mu ** (xpts)) / \
				[mpmath.gamma(k) if k != 0 else 1 for k in xpts + 1])
	yfunc = lambda k : np.exp(- mu) * ((mu ** k)/ mpmath.gamma(k + 1))
	# print("Possion Distribution Probability:", y[:20])
	print("Factor:", max(n) / max(y))

	plt.plot(xpts + 0.5, y) #* max(n) / max(y))

	# We now do the rest of the plotting.
	plt.title("Poisson Distribution of" + \
		" {} Trials \n and {} Tosses per trial".\
					format(numTrials, numTosses))
	plt.xlabel("Number of Trials to Success")
	plt.ylabel("Probability Density")
	plt.xlim(0)

	print("Mean prob", yfunc(mu))

	_, max_ = plt.ylim()
	plt.axvline(x = mu, ymax = yfunc(mu - 0.5) / max_, color = 'black')
	# plt.axvline(x = mu + sigma, ymax = yfunc(mu + sigma) / max_,\
	# 				color = 'black', linestyle = '--')
	# plt.axvline(x = mu - sigma, ymax = yfunc(mu - sigma) / max_,\
	# 				color = 'black', linestyle = '--')

	plt.show()


if __name__ == '__main__':
	print(len(sys.argv))
	if len(sys.argv) == 1:
		print('''
	Usage: {} numTrials nWant nTot
	
	numTrials    the number of iterations to run
	nWant        the number of the deisred quantity (e.g. 10 red balls))
	nTot         the total number of quatities (e.g. 100 balls total)

	Performed with replacement.\n'''.format(sys.argv[0]))
	
	numTrials = 10000
	if len(sys.argv) > 1:
		numTrials = int(sys.argv[1])
	print("Number of Trials set to ", numTrials)

	numTosses = 100
	if len(sys.argv) == 3:
		numTosses = int(sys.argv[2])
	print("numTosses set to ", numTosses)

	mu = 2
	if len(sys.argv) == 4:
		mu = int(sys.argv[3])
	print("mu (lambda) set to ", mu)

	main(numTrials, numTosses, mu)