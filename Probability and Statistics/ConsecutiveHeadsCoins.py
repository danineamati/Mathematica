# Daniel Neamati
# 
# Consider the experiment of tossing a coin
# until you get two consecutive heads. What is the probability 
# distribution of the number # of tosses?
# (Just to be clear, the sequence HH requires two tosses and 
# HTTHH requires five tosses.)

import numpy as np 
import matplotlib.pyplot as plt 
import random

def tossUntilTwoHeads(verbose = False):
	'''Run coins until two consecutive heads and then return 
	number of tosses.'''
	previous = ''
	counter = 0

	while True:
		counter += 1
		current = random.choice(['T', 'H'])
		if verbose:
			print(counter, previous, current)
		if current == 'H' and previous == 'H':
			return counter
		previous = current

def main():
	scores = []
	for i in range(10000):
		scores.append(tossUntilTwoHeads())

	xpts = np.linspace(min(scores), max(scores))
	ypts = 0.25 * np.exp(-0.25 * (xpts - 2))

	plt.hist(scores, bins=range(0, max(scores) + 1, 1), density = 1)
	plt.plot(xpts, ypts, 'k')
	# plt.xlim(2, max(scores))
	plt.xlabel("Number of tosses")
	plt.ylabel("Probability")
	plt.show()

if __name__ == '__main__':
	main()