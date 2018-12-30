# Probability Fun: Project 5 - The Birthday Problem.
# Daniel Neamati
# 29 December 2018

import matplotlib.pyplot as plt 
import numpy as np 
import sys
import random

# from FreqVsProb import randomPick


def randBirthday(numPeople, numTrials):
	''' '''
	numUntilRepeatedBirthday = []

	for i in range(numTrials):
		group = [] # Updated as we "ask" the individuals about their birthday

		for person in range(numPeople):
			# Choose a random birthday
			randBirth = random.randrange(1, 365) #ignores leap year
			# Add the birthday to the group list 
			group.append(randBirth)
			# Check if the birthday is a repeated
			# Note that sets do not include repeated elements
			if len(group) > len(set(group)):
				# print("person: {}, group: {}, set: {}".\
				# 				format(person, len(group), len(set(group))))
				# Subtraction by two takes into account the first person and
				# zero indexing
				numUntilRepeatedBirthday.append(person - 2)
				break

	# print(numUntilRepeatedBirthday)
	return np.array(numUntilRepeatedBirthday)


def listProduct(currList):
	prod = 1
	for elem in currList:
		prod *= elem
	print("Product of {} elements is {}".format(prod, len(currList)))
	return prod

def Birthday(numPeople, numTrials, probOnly = False):
	print("\nBirthday Problem: Given 'n' people in a room. What is the " + \
		"probability that they have the same birthday?")

	# We now calculate the histogram results for the birthdays
	fig, axes = plt.subplots(2, 1)
	fig.tight_layout()


	results = randBirthday(numPeople, numTrials)
	numBins = int(max(results) - min(results))
	n, bins, patches = axes[0].hist(results, bins = numBins)

	cummulative = []
	for i in range(len(n)):
		cummulative.append(sum(n[:i]))

	axes[1].plot(bins[:len(bins) - 1], np.array(cummulative) / numTrials, 'bo')


	# Now we plot the expected probabilities
	# For each person the chance that no one shares a birthday with them is
	# 1 - j / 365 since j enumerates the number of people before them
	jthProb = lambda j: 1 - (j/365)

	# We store the list of probabilities that there is no shared birthdays
	individProb = [1]
	# We convert to probability that there IS a shared birthday 
	# (rather than IS NOT a shared birthday)
	outProb = []
	diffToNext = [0]

	for i in range(1, numPeople + 2):
		# print(i)
		newProb = jthProb(i)
		
		# We apply product rule of probabilities 
		# (e.g. P(no one before j) * P(no one before j - 1, etc))
		prevProb = individProb[i - 1]
		individProb.append(newProb * prevProb)
		outProb.append(1 - individProb[i])
		# print(outProb[i - 1])
		diffToNext.append(outProb[i - 1] - outProb[i - 2])
	
	# outProb = 1 - np.array(individProb[1:])

	if probOnly:
		axes[1].plot(outProb, 'bo')
	else:
		axes[1].plot(outProb, color = 'orange')
		axes[0].plot(np.array(diffToNext[1:]) * numTrials)

	axes[1].set_ylim(0,1)
	axes[1].set_xlim(0, numPeople)
	
	# We can do the rest of the plotting

	axes[1].set_xlabel("Number of People")
	axes[0].set_ylabel("Frequency")
	axes[1].set_ylabel("Probability of at least \none repeated birthday")
	axes[1].axhline(y = 0.50, color = 'black', linestyle = '--')
	axes[1].axhline(y = 0.95, color = 'black', linestyle = '--')
	axes[1].axhline(y = 0.99, color = 'black', linestyle = '--')
	axes[1].set_title("Birthday Problem: Marked 50%, 95%, and 99% Confidence")

	plt.show()


if __name__ == '__main__':
	numTrials = 10000
	if len(sys.argv) > 1:
		numTrials = int(sys.argv[1])
	print("Number of Trials set to ", numTrials)

	numPeople = 50 # Default
	if len(sys.argv) == 3:
		numPeople = int(sys.argv[2])
	print("Number of People set to ", numPeople)

	Birthday(numPeople, numTrials)