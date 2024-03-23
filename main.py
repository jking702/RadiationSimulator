import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import imshow, show, get_cmap
# using the 
# set the x and z space for the gaussian beam
xmax = 0.000025
imax = 1999
x = np.linspace(-xmax, xmax, num=imax)
zmax = 2e-3 
jmax = 100
z = np.linspace(0, zmax,jmax)
lambd = 1e-6
k0 = 2*np.pi/lambd

# set the initial conditions for the gaussian input

a = 10e-6
x0 = 25e-6
theta = 45
thetarad = theta*np.pi/180
E0 = np.multiply(np.exp(np.divide(np.square(-(np.add(x,x0))),a**2)),np.exp(complex(0,1)*k0*x*np.cos(thetarad)))
present = np.abs(E0)
print(len(present))
# imshow(present, cmap=get_cmap("Spectral"), interpolation='nearest')
# show()