
import numpy as np
import math
from numpy import matrix
from numpy import linalg as LA


#inputs need to be 1-D vectors of n components

A = matrix ([[1.],
	[2.],
	[0.],
	[2.], 
	[2.]])

B = matrix ([[1.],
	[2.],
	[1.],
	[2.], 
	[3.]])

C = matrix ([[4.],
	[5.],
	[8.],
	[2.], 
	[3.]])

D = matrix ([[20.],
	[5.],
	[8.],
	[2.], 
	[3.]])

#function to get magnititude 
#alt, just use "LA.norm(array)"
mag = lambda x : math.sqrt(sum(i**2 for i in x))

def meano(array1):
	return np.sum(array1, axis=0)*1/len(array1)

def cosim(a, b): 
	return np.dot(a.T, b)/(mag(a)*mag(b))

def angles(array1):
	anglebox = []
	mean = meano(array1)
	for x in array1:
		anglebox.append(float(cosim(x, mean)))
	return anglebox

#print angles([A,B,C,D])
