## Daniel Neamati
## 22 May 2018
## Ge 1 Set 4

import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
from scipy import stats

verbose = False

if verbose:
    print("Import Complete")

## Data
# increment by 0.5 from 2.75 to 7.25 (30) or 5.25 (22)
magRange = np.array([x/4 for x in range(11, 30, 2)])
countM = np.array([5901, 2070, 684, 222, 59, 18, 3, 0, 0, 1])

cumulM = np.array([8958, 3057, 987, 303, 81, 22, 4, 1, 1, 1])
log10cumul = np.log10(cumulM)

magRangeAdj = [x/4 for x in range(11, 24, 2)]
magRangeAdj.append(7.75)
magRangeAdj = np.array(magRangeAdj)
countMAdj = np.array([5901, 2070, 684, 222, 59, 18, 3, 1])

if verbose:
    print("magRange:", len(magRange), magRange)
    print("countM:", len(countM), countM)
    print("cumulM:", len(cumulM), cumulM)
    print("log10cumul:", len(log10cumul), log10cumul)
    print()
    print("magRangeAdj:", len(magRangeAdj), magRangeAdj)
    print("countMAdj:", len(countMAdj), countMAdj)
    print()

## Energy Calc
def Energy(magRange, countM):
    '''Determines the energy released in each magnitude bin.'''
    energy = []
    mag = 2.75
    print()
    for binM in range(len(magRange)):
        EperEarthquake = 10**(1.5 * magRange[binM] + 4.8)
        energy.append(EperEarthquake * countM[binM])
        print(mag, ":", Decimal(str(EperEarthquake * countM[binM])))
        mag += 0.5
    print()
    if energy == [] and verbose:
        print('No values added.')
        print()
    elif verbose:
        print()
        print(len(energy), 'Total Energies (J)', energy)
        print()
    return np.array(energy)

## Make plots
def EarthquakeNumPlot(X, Y, logY):
    '''Makes the graph of earthquake number on log scale.'''
    fig = plt.figure()
    ax = fig.add_subplot(111)

##    for (index, num) in enumerate(Y):
##        print(index, num)
##        if num == 0:
##            X.pop(index)
##            Y.pop(index)
##            print("Pop")

    rawplot = plt.scatter(X, Y, color = 'black', \
                label = 'Cumulative Total of Earthquakes')
    plt.xlabel('Magnitude Range')
    plt.ylabel('Cumulative Total above lower bound of the Magnitude Range')
    plt.title('Log-Linear Plot of Earthquake Numbers in \n Southern California, 2007 through 2016')

    #fit = np.polyfit(X, logY, deg = 1)
    #fitline = 10**(fit[0] * X + fit[1])
    #print('The line has a slope of', fit[0], 'and a y-int of', fit[1])
    #print(fit)
    
    slope, yint, r_val, p_val, std_err = stats.linregress(X[:6], logY)
    fitline = 10**(slope * X[:6] + yint)
    print('The line has a slope of', slope, 'and a y-int of', yint)
    print('r =', r_val, 'r^2 =', r_val**2)
    
    if verbose:
        print(X, logY)
        print(fitline)
        print()

    TWOPLACES = Decimal(10) ** -2
    THREEPLACES = Decimal(10) ** -3
    lbl = 'Best Fit Line \nlog10(y) = {0} x + {1} \nr^2 = {2}'.format(\
        Decimal(slope).quantize(TWOPLACES), Decimal(yint).quantize(TWOPLACES),\
        Decimal(r_val**2).quantize(THREEPLACES))
    fitplot = plt.plot(X[:6], fitline, label = lbl)

    ax.set_yscale('log')
    #ax.set_ylim(0, 10**4)
    ax.set_xlim(2.5, 7.5)

    plt.legend()
    
    plt.show()

def EnergyPlot(X, Y, XAdj, YAdj):
    '''Makes the graph of energy dissipated in each bin.'''
    #print(YAdj)
    fig = plt.figure()
    ax = fig.add_subplot(111)

    rawplot = plt.scatter(X, Y, color = 'black', \
                label = 'Total Energy of Earthquakes in bin')
    plt.xlabel('Magnitude Range')
    plt.ylabel('Total Energy of Eartquakes in Magnitude Range (J)')
    plt.title('Log-Linear Plot Earthquake Energy in \n Southern California, 2007 through 2016')

    ## Include last point
    '''fit = np.polyfit(XAdj, np.log10(YAdj), deg = 1)
    fitline = 10**(fit[0] * XAdj + fit[1])
    print('The line has a slope of', fit[0], 'and a y-int of', fit[1])
    
    if verbose:
        print()
        print(XAdj, YAdj, fit)
        print(fitline)
        
    fitplot = plt.plot(XAdj, fitline, label = 'Best Fit Line')'''

    '''slope, yint, r_val, p_val, std_err = stats.linregress(\
        XAdj, np.log10(YAdj))
    fitline = 10**(slope * XAdj + yint)
    print('The line has a slope of', slope, 'and a y-int of', yint)
    print('r =', r_val, 'r^2 =', r_val**2)
    
    if verbose:
        print(XAdj, np.log10(YAdj))
        print(fitline)
        print()

    TWOPLACES = Decimal(10) ** -2
    lbl = 'Best Fit Line \nlog10(y) = {0} x + {1} \nr^2 = {2}'.format(\
        Decimal(slope).quantize(TWOPLACES), Decimal(yint).quantize(TWOPLACES),\
        Decimal(r_val**2).quantize(TWOPLACES))
    fitplot = plt.plot(XAdj, fitline, label = lbl)'''

    ## Ignore last point
    stopPt = 6
    '''fit2 = np.polyfit(X[:stopPt], np.log10(Y[:stopPt]), deg = 1)
    fitline2 = 10**(fit2[0] * X[:stopPt] + fit2[1])
    print()
    print('The line has a slope of', fit2[0], 'and a y-int of', fit2[1])
    
    if verbose:
        print()
        print(X[:stopPt], Y[:stopPt], fit2)
        print(fitline2)
        
    fitplot = plt.plot(X[:stopPt], fitline2, label = 'Best Fit Line')'''

    '''slope, yint, r_val, p_val, std_err = stats.linregress(\
        X[:stopPt], np.log10(Y[:stopPt]))
    fitline = 10**(slope * X[:stopPt] + yint)
    print('The line has a slope of', slope, 'and a y-int of', yint)
    print('r =', r_val, 'r^2 =', r_val**2)
    
    if verbose:
        print(X, logY)
        print(fitline)
        print()

    TWOPLACES = Decimal(10) ** -2
    lbl = 'Best Fit Line \nlog10(y) = {0} x + {1} \nr^2 = {2}'.format(\
        Decimal(slope).quantize(TWOPLACES), Decimal(yint).quantize(TWOPLACES),\
        Decimal(r_val**2).quantize(TWOPLACES))
    fitplot = plt.plot(X[:stopPt], fitline, label = lbl)'''
    
    ax.set_yscale('log')
    ax.set_ylim(10**12, 10**17)
    #ax.set_xlim(2.5, 7.5)

    plt.legend(loc = 'lower right')
    
    plt.show()

## Run Code
EarthquakeNumPlot(magRange, cumulM, log10cumul[:6])
EnergyPlot(magRange, Energy(magRange, countM),\
           magRangeAdj, Energy(magRangeAdj, countMAdj))
