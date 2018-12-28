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
	randomPick(3, 5)

	results = []
	avgResult = []
	xpts = []

	verboseThres = int(numTrials/10)

	for i in range(numTrials):
		results.append(randomPick(nWant, nTot))
		avgResult.append(np.average(results))
		xpts.append(i + 1)

		if (i + 1) % verboseThres == 0:
			print("At iteration ", i + 1)


	fig, axes = plt.subplots(2, 1)
	fig.tight_layout()
	#fig.suptitle("Frequency versus Probability")

	axes[0].plot(xpts, avgResult)
	axes[0].axhline(y = 0.5, color = 'k', linewidth = 0.5)
	axes[0].axhline(y = 0.475, color = 'k', linewidth = 0.5, linestyle = '--')
	axes[0].axhline(y = 0.525, color = 'k', linewidth = 0.5, linestyle = '--')
	axes[0].set_title("{} Random Trials with probability {}".format(numTrials,\
													(nWant/nTot)))
	axes[0].set_ylabel("Relative Frequency of Desired Value")
	
	lower_bound = int(len(avgResult)/2)
	axes[1].plot(xpts[lower_bound:], avgResult[lower_bound:])
	axes[1].axhline(y = 0.5, color = 'k', linewidth = 0.75)
	axes[1].axhline(y = 0.495, color = 'k', linewidth = 0.5, linestyle = '--')
	axes[1].axhline(y = 0.505, color = 'k', linewidth = 0.5, linestyle = '--')
	axes[1].set_title("Zoom in on points {} through {}".format(lower_bound,\
															numTrials))
	axes[1].set_ylabel("Relative Frequency of Desired Value")

	plt.show()


if __name__ == '__main__':
	
	numTrials = 25
	if len(sys.argv) > 1:
		numTrials = int(sys.argv[1])

	main(numTrials, 1, 2)