# Viswa Virinchi
# 130070038
# Assignment 2

import sys
from operator import add, mul

def transpose(alist):
	return map(list, zip(*alist))

mdp_file_name = sys.argv[1]
# mdp_file_name = '../data/MDP-2_5.txt'
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
V =[0]*S
Q = [[]]*S
pi =[-1]*S
e = 0.000000001
i = 0
converge = False
while not converge:
	i+=1
	converge = True
	for s in xrange(S):	
		Vprev = V[s]
		Q[s] = [sum(map(mul,map(add,[g*v for v in V],r),T[s][a])) for a,r in enumerate(R[s])]
		V[s] = max(Q[s])
		converge = converge and (abs(V[s]-Vprev)<e)
	
for s in xrange(S):
	pi[s] = [i for i,j in enumerate(Q[s]) if j==V[s]][0]
	print str(V[s])+'\t'+str(pi[s]) 