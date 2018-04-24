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


print(AofTs(288))

## Setting
iceOn = True
waterOn = False


########## Problem 1 ##############
print("########## Problem 1 ##############")

## Making plot
matplotlib.rc('xtick',labelsize = 18)
matplotlib.rc('ytick',labelsize = 18)
matplotlib.rc('axes',linewidth = 2)


def feedbackEarth(dTsdt, lines, surface = False):
    
    fig = plt.figure()
    if surface:
        ax = fig.add_subplot(111, projection='3d')

    p1 = plt.contour(X, Y, dTsdt, lines, color = 'k')

    plt.clabel(p1, p1.levels)
    plt.clabel(p1,inline=1,fontsize=10,fmt='%4.6f K/day')
    plt.xlabel('$T_0 \quad (K)$', fontsize = 15)
    plt.ylabel('$T_S \quad (K)$', fontsize = 15)
    plt.title('Surface Energy Balance')

    plt.plot([220,320],[288,288],'r',linewidth=2) #TS = 288 K
    #plt.plot([T0,T0],[Tmin,Tmax],'b',linewidth=2) # plug in for T0

    if surface:
        ax.plot_surface(X, Y, dTsdt, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

    plt.show()

snowBallEarth(dTsdt1, 15)
snowBallEarth(dTsdt1, 15, surface = True)

########## Problem 3 ##############
iceOn = False
waterOn = True

T0 = np.arange(220, 320, 0.1)
Ts = np.arange(Tmin, Tmax, 0.1)

X, Y = np.meshgrid(T0, Ts)

dTsdt2 = (1/C)*(sigma*(X**4)*(1 - A0)- (1/(1 + Tau(Y)))*sigma*(Y**4))

snowBallEarth(dTsdt2, 15)

def makeGraph(iceOn, lines, surface = False):
    '''Makes specific of the two plots.'''
    if iceOn:
        x = 5
        Tmin, Tmax = 220, 320
        ## Albedo at a given temperature
        AofTs = lambda Ts: 0.45 - 0.25 * np.tanh((Ts - 272)/23)
        ## Constant Opacity (Tau)
        tau = 0.68
        dTsdt = (1/C)*(sigma*(X**4)*(1 - AofTs(Y))-(1/(1+tau))*sigma*(Y**4))
    else:
        x = 0
        Tmin, Tmax = 260, 360
        ## Assume constant albedo
        A0 = 0.3 
        ## Opacity at given temperature (Tau)
        Tau = lambda Ts: 0.55 + 0.07 * np.exp(5413*((1/288) - (1/(Ts))))

    T0 = np.arange(220, 320, 0.1)
    Ts = np.arange(Tmin, Tmax, 0.1)

    X, Y = np.meshgrid(T0, Ts)




    
