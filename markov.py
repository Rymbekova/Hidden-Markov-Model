#/usr/bin/python
import sys, random
import numpy as np


def get_alphabet(seq):
	alpha = []
	for a in seq:
		if a not in alpha: alpha.append(a)
	alpha.sort()
	return ''.join(alpha)


def get_matrix(seq, alpha): 
	n = len(alpha)
	tm = np.zeros((n,n))
	l = len(seq) #transition from element 0 to element l-1
	for i in range(l-1):
		p1 = alpha.find(seq[i]) #assign to each transition a position in a matrix
		p2 = alpha.find(seq[i+1]) 
		if p1 > -1 and p2 > -1: tm[p1][p2]+=1
	print tm
	for i in range(n):
		tm[i,:] = tm[i,:]/np.sum(tm[i,:]) #to get probs we need to sum the row and divide by each number
	return tm #so in the end all probs are normalised and sum is 1


def get_prob(seq, tm, alpha):
	p = 1.0
	l = len(seq)
	for i in range (l-1):
		p1 = alpha.find(seq[i])
		p2 = alpha.find(seq[i+1]) 
		if p1 > -1 and p2 > -1: p = p*tm[p1][p2]
	return p #probability or - log

def get_shuffle(seq):
	l = [i for i in seq]
	random.shuffle(l)
	return ''.join(l)



if __name__ == '__main__':
	seq = sys.argv[1] #first input - a string or a file with seq
	#tseq = sys.argv[2] #test
	alpha = get_alphabet(seq)
	#print alpha
	#print seq
	tm = get_matrix(seq, alpha)
	print tm
	p = get_prob(seq, tm, alpha)
	#tp = get_prob(tseq, tm, alpha)
	print seq
	print -np.log10(p)
	for i in range(100):
		nseq = get_shuffle(seq)
		npr = get_prob(nseq, tm, alpha)
		print nseq, -np.log10(npr)
	#print tseq
	#if tp > 0:
		#print -np.log10(tp)
	#else:
		#print np.inf #infinite