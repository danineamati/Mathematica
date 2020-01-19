# APMonitor GEKKO Python Tutorial
# https://apmonitor.com/wiki/index.php/Main/GekkoPythonOptimization

from gekko import GEKKO
import numpy as np
import matplotlib.pyplot as plt  

m = GEKKO(remote=True)
m.time = np.linspace(0,20,41) # how far and frequently to look into the future

# Parameters
mass = 500
b = m.Param(value=50)
K = m.Param(value=0.8)

# Manipulated variable
# Denote lower bound and upper bound on the maniputated variable
# In this case the gas pedal can go between 0 and 100.
# We set the initial condition as 0
p = m.MV(value=0, lb=0, ub=100) 
p.STATUS = 1  # allow optimizer to change
p.DCOST = 0.1 # smooth out gas pedal movement, Non-zero cost on change of gas
p.DMAX = 20   # slow down change of gas pedal, Maximum on the derivative

# Controlled Variable
# We set the initial condition as 0
v = m.CV(value=0)
v.STATUS = 1  # add the SP to the objective
m.options.CV_TYPE = 2 # squared error
v.SP = 40     # set point
v.TR_INIT = 1 # set point trajectory
v.TAU = 5     # time constant of trajectory

# Process model
# m v' = - b * v + K*b*p
# p is the gas pedal
# b is the ??
# K is the ??
m.Equation(mass*v.dt() == -v*b + K*b*p)

m.options.IMODE = 6 # control
m.solve(disp=True)

# get additional solution information
import json
with open(m.path+'//results.json') as f:
    results = json.load(f)

plt.figure()
plt.subplot(2,1,1)
plt.plot(m.time,p.value,'b-',label='MV Optimized')
plt.title("MPC Example with Car Speeding up during HWY Onramp")
plt.legend()
plt.ylabel('Input (Gas Pedal)')
plt.subplot(2,1,2)
plt.plot(m.time,results['v1.tr'],'k-',label='Reference Trajectory')
plt.plot(m.time,v.value,'r--',label='CV Response')
plt.ylabel('Output (Velocity)')
plt.xlabel('Time')
plt.legend(loc='best')
plt.show()