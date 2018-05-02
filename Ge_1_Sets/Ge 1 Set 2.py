## Daniel Neamati
## 23 April 2018
## Ge 1 Set 2

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib

from mpl_toolkits.mplot3d import Axes3D

print("Complete!")

## Constants
sigma = 5.67e-8  #The Stefan-Boltzmann constant
Cp = 1000
P = 10**5
g = 10 
C = Cp * P / g
print(C)

## Setting
iceOn = True
waterOn = False


## Making plot
matplotlib.rc('xtick',labelsize = 18)
matplotlib.rc('ytick',labelsize = 18)
matplotlib.rc('axes',linewidth = 2)


def feedbackEarth(X, Y, dTsdt, lines, Tmin, Tmax,\
                  surface = False, refline = False, labels = True):
    '''Makes the actual graph of feedback in the Earth CO2 cycle.'''
    fig = plt.figure()
    if surface:
        ax = fig.add_subplot(111, projection='3d')

    p1 = plt.contour(X, Y, dTsdt, lines, color = 'k')

    if not labels:
        plt.clabel(p1,inline=1,fontsize=10,fmt='%4.2f')
    else:
        plt.clabel(p1,inline=1,fontsize=10,fmt='%4.2f K/day')
        
    plt.xlabel('$T_0 \quad (K)$', fontsize = 15)
    plt.ylabel('$T_S \quad (K)$', fontsize = 15)
    plt.title('Surface Energy Balance \n' +\
              'Contour Plot of Change in Surface Temperature ' +\
              'with Respect to Time' )

    if refline:
        plt.plot([220,320],[288,288],'r',linewidth=2) #TS = 288 K
        plt.plot([276.56,276.56],[Tmin,Tmax],'r',linewidth=2) # plug in for T0

    if surface:
        ax.plot_surface(X, Y, dTsdt, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

    plt.show()

def makeGraph(iceOn, lines, surface = False, refline = False, labels = True):
    '''Makes specific of the two plots.'''
    if iceOn:
        ########## Problem 1 ##############
        print("########## Problem 1 ##############")
        x = 5
        Tmin, Tmax = 220, 320
        ## Albedo at a given temperature
        AofTs = lambda Ts: 0.45 - 0.25 * np.tanh((Ts - 272)/23)
        ## Constant Opacity (Tau)
        tau = 0.68
        
    else:
        ########## Problem 3 ##############
        print("########## Problem 3 ##############")
        x = 0
        Tmin, Tmax = 260, 360
        ## Assume constant albedo
        A0 = 0.3 
        ## Opacity at given temperature (Tau)
        Tau = lambda Ts: 0.55 + 0.07 * np.exp(5413*((1/288) - (1/(Ts))))
        

    T0 = np.arange(220, 320, 0.1)
    Ts = np.arange(Tmin, Tmax, 0.1)

    X, Y = np.meshgrid(T0, Ts)

    if iceOn:
        ## Feedback function
        dTsdt = (1/C)*(sigma*(X**4)*(1 - AofTs(Y))-(1/(1+tau))*sigma*(Y**4))\
                * (60 * 60 * 24)
    else:
        ## Feedback function
        dTsdt = (1/C)*(sigma*(X**4)*(1 - A0)- (1/(1 + Tau(Y)))*sigma*(Y**4))\
                * (60 * 60 * 24)

    feedbackEarth(X, Y, dTsdt, lines, Tmin, Tmax, surface, refline, labels)

    
#makeGraph(True, 15)
makeGraph(True, 15, refline = True)
#makeGraph(False, 15)
#makeGraph(False, 15, refline = True)



    
