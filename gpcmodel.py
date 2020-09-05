import sys 
import numpy as np
import cPickle


def get_seq(seqfile):
	seq=''
	for line in open (seqfile):
		if line[0] != '>': seq = seq + line.rstrip()
	return seq
	#seq=''.join([line.rstrip() for line in open(seqfile) if line[0] != '>'])

def get_ranges(bedfile):
	l=[]
	for line in open(bedfile):
		v = line.split()
		l.append([v[1], int(v[2]), int(v[3])])
	return l

def match_seq(bed, seq): #seq nongpc and gpc
	s=''
	n = len(bed)
	p0=0
	for i in range(n): 
		s = s + (bed[i][1]-p0-1)*'N' #final position of nongpci
		s = s + (bed[i][2]-bed[i][1])*'Y'
		p0 = bed[i][2]
	#print len(s)
	s = s+(len(seq)-bed[i][2])*'N' #length of all Ys
	return s #range on the seq: gpc, nongpc

#whatever is N also N nucleotides are begin and end
#count transitions and inition
#a matrix 2x2
def count(seq, cpg, nuc='ACGT', state='NY'):
	t = np.zeros((len(state), len(state)))
	e = np.zeros((len(state), len(nuc)))
	n = len(seq)
	for i in range (1, n):
		ps = state.find(cpg[i])
		pn = nuc.find(seq[i])
		#pf = state.find(cpg[i+1])
		if ps > -1 and pn > -1: e[ps][pn] += 1
		#if ps > -1 and pn > -1: t[ps][pf] += 1
	e[0] = e[0]/np.sum(e[0])
	e[1] = e[1]/np.sum(e[1]) #emission two states four letters
	t[0] = t[0]/np.sum(t[0])
	t[1] = t[1]/np.sum(t[1]) #transition
	return e, t








if __name__ == '__main__':
	hmm = {}
	bedfile=sys.argv[1]
	seqfile=sys.argv[2]
	seq = get_seq(seqfile)
	bed = get_ranges(bedfile)
	cpg = match_seq(bed, seq) #gpc no N yes Y
	seq = seq.upper() #nucleotides
	e, t = count(seq,cpg)
	hmm['T'] = t
	hmm['E'] = e
	cPickle.dump(hmm, open('hmm.cpk', 'w'))
	
