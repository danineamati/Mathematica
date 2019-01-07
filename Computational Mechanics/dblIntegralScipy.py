# Test the double integral in scipy
# Daniel Neamati
# 6 January 2018

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


testFunc = lambda x: 2 * x

xpts = np.linspace(-10, 10, 1000)
ypts = []
yIntpts = []
yDblIntpts = []

for x in xpts:
	ypts.append(testFunc(x))
	yIntpts.append(integrate.quad(lambda s: testFunc(s), 0, x)[0])

	# Syntax for double integral is 
	# I = int_{0}^{inf} int_{1}^{inf} \frac{e^{-xt}}{t^n} dt dx
	# is written as
	# integrate.dblquad(lambda t, x: np.exp(-x*t)/t**n, 0, np.inf,\
	#			 lambda x: 1, lambda x = np.inf)
	# THE ORDER OF:
			# first lambda matters (corresponds to bounds)
	# THE NAME OF:
			# variables in the bounds does not matter.
	# 
	# Or more generally,
	# I = int_{y=0}^{y=0.5} int _{x=0}^{x=1-2y} x * y dx dy
	# is written as
	# I = integrate.nquad(f, [bounds_x, bounds_y])
	# where
	# def f(x, y): return x * y
	# def bounds_y(): return [0, 0.5]
	# def bounds_x(y): return [0, 1-2*y]

	yDblIntpts.append(integrate.dblquad(\
		lambda s, s2 : testFunc(s), 0, x, lambda s2: 0, lambda s2: s2)[0])

	# In the above example, we want to integrate
	# I = int_{0}^{x} int_{0}^{s2} f(s) ds ds2

plt.plot(xpts, ypts)
plt.plot(xpts, yIntpts)
plt.plot(xpts, yDblIntpts)

plt.axhline(y = 0, color = 'k', linewidth = 0.5)
plt.axhline(y = 333, color = 'k', linewidth = 0.5)
plt.axvline(x = 0, color = 'k', linewidth = 0.5)
plt.axvline(x = 10, color = 'k', linewidth = 0.5)

plt.show()