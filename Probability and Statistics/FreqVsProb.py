# Probability Fun: Project 1 - frequency versus probability.
# Daniel Neamati
# 27 December 2018

import random
import matplotlib.pyplot as plt 
import sys
import numpy as np

def randomPick(nWant, nTot):
	'''This function does the equivalent of picking a red ball from a bag
	where there are (nWant) red balls and (nTot) balls total.
	
	It returns true if it picked the red ball (nWant)

	Assertion Error if nWant > nTot.'''
	
	assert (nWant <= nTot), "Number of desired objects is larger than " + \
		"number of total objects. Please check that arguments are "+\
		"randomPick(nWant, nTot)."

	chosen = random.randint(1, nTot)

	if chosen <= nWant:
		return True
	return False

def main(numTrials, nWant, nTot):
	'''We want to compare the frequency of random events to the actual
	probability that they occur. Basically we want to check that at the 
	number of trials becomes large, does the frequency converge to the 
	expected probability.'''

	# We canculate the expected probability
	prob = nWant / nTot

	# Initialized list.
	results = [] # Results of true (picked the desired ball) and false
	avgResult = [] # Average number of true values thus far.
	xpts = [] # Enumerating the i-th trial

	verboseThres = int(numTrials/10)

	for i in range(numTrials):
		results.append(randomPick(nWant, nTot))
		avgResult.append(np.average(results))
		xpts.append(i + 1)

		if (i + 1) % verboseThres == 0:
			print("At iteration ", i + 1)


	# Now we just plot the results.

	fig, axes = plt.subplots(2, 1)
	fig.tight_layout()
	#fig.suptitle("Frequency versus Probability")

	axes[0].plot(xpts, avgResult)
	axes[0].axhline(y = prob, color = 'k', linewidth = 0.5)
	axes[0].axhline(y = prob - 0.025, color = 'k', linewidth = 0.5,\
							linestyle = '--')
	axes[0].axhline(y = prob + 0.025, color = 'k', linewidth = 0.5,\
							linestyle = '--')
	axes[0].set_title("{} Random Trials with probability {}".format(numTrials,\
													prob))
	axes[0].set_ylabel("Relative Frequency of Desired Value")
	
	lower_bound = int(len(avgResult)/2)
	axes[1].plot(xpts[lower_bound:], avgResult[lower_bound:])
	axes[1].axhline(y = prob, color = 'k', linewidth = 0.75)
	axes[1].axhline(y = prob - 0.005, color = 'k', linewidth = 0.5,\
							linestyle = '--')
	axes[1].axhline(y = prob + 0.005, color = 'k', linewidth = 0.5,\
							linestyle = '--')
	axes[1].set_title("Zoom in on points {} through {}".format(lower_bound,\
															numTrials))
	axes[1].set_ylabel("Relative Frequency of Desired Value")

	plt.show()


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print('''
	Usage: {} numTrials nWant nTot
	
	numTrials    the number of iterations to run
	nWant        the number of the deisred quantity (e.g. 10 red balls))
	nTot         the total number of quatities (e.g. 100 balls total)

	Performed with replacement.\n'''.format(sys.argv[0]))
	
	numTrials = 100
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