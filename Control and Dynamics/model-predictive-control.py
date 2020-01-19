
# Model Predictive Control Example
# Inspired by APMonitor tutorial

# Daniel Neamati
# 18 January 2020

# Goal: Replicate this, but for a simple spring system
# Objective: Get the mass to a certain position from equilibrium (deltaX)
# Manipulated: Manipulate the forcing frequency

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt  

m = GEKKO(remote=True)
m.time = np.linspace(0,100, 400) # how far and frequently to look into the future

# Parameters
mass = 500
k = m.Param(value=5)

# Manipulated variable
# Denote lower bound and upper bound on the maniputated variable
# In this case the forcing term can go between -100 and 400.
# We set the initial condition as 0
f = m.MV(value=0, lb= -100, ub=400) 
f.STATUS = 1  # allow optimizer to change
f.DCOST = 2 # smooth out gas pedal movement, Non-zero cost of force
f.DMAX = 10   # slow down change of gas pedal, Maximum on the derivative

# Controlled Variable
# We set the initial condition as 0
x = m.CV(value=0)
x.STATUS = 1  # add the SP to the objective
m.options.CV_TYPE = 2 # squared error
x.SP = 40     # set point
x.TR_INIT = 1 # set point trajectory
x.TAU = 10     # time constant of trajectory

# Since this is a second order ODE, we need an intial condition on 
# the velocity as well
dx = m.Var(value = 0.0)


# Process model
# m x'' = - k x + f
m.Equation([
	dx == x.dt(),
    mass * dx.dt() == - k*x + f
])


m.options.IMODE = 6 # control
m.solve(disp=True)

# get additional solution information
import json
with open(m.path+'//results.json') as file:
    results = json.load(file)

plt.figure()
plt.subplot(2,1,1)
plt.plot(m.time,f.value,'b-',label='MV Optimized')
plt.title("MPC Example with Spring and Forcing term")
plt.legend()
plt.ylabel('Input (Forcing Term)')
plt.subplot(2,1,2)
plt.plot(m.time,results['v1.tr'],'k-',label='Reference Trajectory')
plt.plot(m.time,x.value,'r--',label='CV Response (position)')
# plt.plot(m.time,dx.value,'b--',label='CV Response (velocity)')
plt.ylabel('Output (Position)')
plt.xlabel('Time')
plt.legend(loc='best')
plt.show()