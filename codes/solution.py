import numpy as np
import matplotlib.pyplot as plt

def line_intersect(n1,n2,p1,p2):
	N = np.vstack((n1,n2))
	p = np.zeros(2)
	p[0] = p1
	p[1] = p2
	return np.matmul(np.linalg.inv(N),p)

def opposite_vertex(O,A):
	return (2*O - A)

dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

#Equation of line AB

n_AB = np.array([1,-1])
n_AD = np.array([7,-1])
p_AB = -1
p_AD = 5

A = line_intersect(n_AB,n_AD,p_AB,p_AD) #intersection of given two lines 

O = np.array([-1,-2])

C = opposite_vertex(O,A)

#Normal vector of diagonal BD is directional vector of AC
n_BD = A-C
p_BD = np.matmul(n_BD.T,O)

B = line_intersect(n_AB,n_BD,p_AB,p_BD)
D = line_intersect(n_AD,n_BD,p_AD,p_BD)

print (A,B,C,D)



