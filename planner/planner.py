# Viswa Virinchi
# 130070038
# Assignment 2

import sys
from operator import add, mul
from random import randint
import numpy as np

mdp_file_name = sys.argv[1]
mdp_file = open(mdp_file_name, 'r')
S = int(mdp_file.readline())
A = int(mdp_file.readline())
R =[]
T =[]
for s in xrange(S):
	R.append([])
	for a in xrange(A):
		R[s].append(map(float,mdp_file.readline().strip().split('\t')))

for s in xrange(S):
	T.append([])
	for a in xrange(A):
		T[s].append(map(float,mdp_file.readline().strip().split('\t')))

g = float(mdp_file.readline())
pi = [randint(0,A-1) for a in xrange(S)]
converge = False
i =0
while not converge:
	converge = True
	b = [sum(map(mul,T[s][pi[s]],R[s][pi[s]]))  for s in xrange(S)]
	a =[]
	for s in xrange(S):
		temp =[]
		for sPrime in xrange(S):
			if sPrime == s:
				temp.append(1.0-g*T[s][pi[s]][sPrime])
			else:
				temp.append(-g*T[s][pi[s]][sPrime])
		a.append(temp)
	a = np.array(a)
	b = np.array(b)
	V = np.linalg.solve(a, b)
	for s in xrange(S):
		Q = [sum(map(mul,map(add,[g*v for v in V],r),T[s][a])) for a,r in enumerate(R[s])]
		Qbest =max(Q)
		# Find optimal action
		a = [i for i,j in enumerate(Q) if j==Qbest][0]
		if(Qbest>V[s]):
			converge = converge and pi[s]==a
			pi[s] =a
			
for s in xrange(S):
	print str(V[s])+'\t'+str(pi[s]) 