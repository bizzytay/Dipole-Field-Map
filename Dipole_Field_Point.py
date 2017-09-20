import math
import pprint
import numpy as np
from numpy import corrcoef, sum, log, arange
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import cm

# magnetic moment of the magnetic particle
#theta = math.pi/2
theta = 90*math.pi/180
phi = 75*math.pi/180
Ms = 10000/(4*math.pi)
mRadius = 500e-7
mV = (4/3)*(math.pi)*(mRadius**3)
mp = Ms*mV
print "mp=", mp
mx = mp * math.sin(theta) * math.cos(phi)
my = mp * math.sin(theta) * math.sin(phi)
mz = mp * math.cos(theta)

# Make space
x_length = 4e-6 * 100
y_length =  4e-6 * 100
d = 300e-9 * 100 + mRadius
z_length = 0e-9 * 100

#Class to make B Fields
class B_Field:
    def Point(self,xp,yp,zp,mx,my,mz):
        dist = math.sqrt(xp**2 + yp**2 + zp**2)
        Bx = ((2*xp**2-yp**2-zp**2)*mx + 3*xp*yp*my + 3*xp*zp*mz)/(dist**5)
        By = (3*xp*yp*mx + (2*yp**2-xp**2-zp**2)*my + 3*yp*zp*mz)/(dist**5)
        Bz = (3*xp*zp*mx + 3*yp*zp*my + (2*zp**2-xp**2-yp**2)*mz)/(dist**5)
        return Bx, By, Bz

    def Map(self, xnum,ynum,znum,xrel,yrel,zrel):
        Bxmap = [[[0 for k in xrange(znum)] for j in xrange(ynum)] for i in xrange(xnum)]
        Bymap = [[[0 for k in xrange(znum)] for j in xrange(ynum)] for i in xrange(xnum)]
        Bzmap = [[[0 for k in xrange(znum)] for j in xrange(ynum)] for i in xrange(xnum)]

        for i in range(xnum):
            for j in range(ynum):
                for k in range(znum):
                    xrelc = xrel[i]
                    yrelc = yrel[j]
                    zrelc = zrel[k]
                    dist = math.sqrt(xrelc**2 + yrelc**2 + zrelc**2)

                    Bxmap[i][j][k] = ((2*xrelc**2-yrelc**2-zrelc**2)*mx + 3*xrelc*yrelc*my + 3*xrelc*zrelc*mz)/(dist**5)
                    Bymap[i][j][k] = (3*xrelc*yrelc*mx + (2*yrelc**2-xrelc**2-zrelc**2)*my + 3*yrelc*zrelc*mz)/(dist**5)
                    Bzmap[i][j][k] = (3*xrelc*zrelc*mx + 3*yrelc*zrelc*my + (2*zrelc**2-xrelc**2-yrelc**2)*mz)/(dist**5)

        return Bxmap,Bymap,Bzmap
