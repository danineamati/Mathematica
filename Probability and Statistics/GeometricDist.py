# Probability Fun: Project 2 - Geometric Distribution.
# Daniel Neamati
# 27 December 2018

import random
import matplotlib.pyplot as plt
import sys
import numpy as np

from FreqVsProb import randomPick

def main(numTrials, nWant, nTot):
	'''We want to model a geometric distribution. To do this we "pick" a ball
	from a bag and keep "picking" until we we get the correct ball. '''

	# Expected probability of success
	prob = nWant/nTot

	# Initialize to the first pick
	results = np.ones(numTrials)

	for i in range(numTrials):
		# Keep picking until we get the correct ball
		while(not randomPick(nWant, nTot)):
			# print("Fail")
			results[i] += 1

		# print("Success")
		# print(results[i])
		# print()

	# We want to make sure that we bin at the integer
	numBins = int(max(results))
	print(set(results))
	print("Number of Bins:", numBins)
	n, bins, patches = plt.hist(results, numBins, color = 'green')

	# We model the ideal geometric distribution
	y = numTrials * ((1 - prob) ** (bins - 1)) * prob
	# plt.plot(bins + 0.5, y, '--')
	plt.scatter((bins + 0.5), y, color = 'black')


	# We now do the rest of the plotting.

	plt.title("Geometric Distribution of" + \
		" {} Trials \n and Probability of Success {}".\
					format(numTrials, round(prob, 3)))
	plt.xlabel("Number of Trials to Success")
	plt.ylabel("Frequency")

	plt.ylim(0)
	plt.xlim(1)

	avg = np.average(results) 

	_, max_ = plt.ylim()

	plt.axvline(x = 1/prob, color = 'black')
	plt.axvline(x = avg, color = 'black', linestyle = 'dashed')
	plt.text(max(avg + avg/10, (1/prob) + (1/prob)/10), 
         max_ - max_/10, 
         'Mean: {:.2f} vs {:.2f}'.format(avg, 1/prob))

	plt.show()


if __name__ == '__main__':
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

	nWant = 1
	nTot = 2
	if len(sys.argv) == 4:
		nWant = int(sys.argv[2])
		nTot = int(sys.argv[3])
	print("nWant set to {} and nTot set to {}".format(nWant, nTot))

	main(numTrials, nWant, nTot)