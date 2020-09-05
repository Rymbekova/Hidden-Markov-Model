#for i in `cat list.txt`
#> do
#> echo $i
#> done

#for i in `cat list.txt`
#> do wget https://www.uniprot.org/uniprot/$i.fasta; done

#cat *.fasta > list.fasta - so you create one file with all fastas
#cat list.fasta | grep '>'| wc -l - check if the generated file is correct
#clustalw server - upload list.fasta - you get MSA address output

#to transform MSA into a profile
#!/usr/bin/python
import sys
import numpy as np


#a function that parses the file and gets the alignment entropy exercise
def get_aln(alnfile):
	d_aln = {}
	f = open(alnfile)
	for line in f:
		if line.find ('sp') == 0: continue #if does not start with sp, go to the next line
		l = line.rstrip().split() # a vector that contains three columns
		sid = l[0] #sequence identifier
		seq = l[1] #sequence itself
		d_aln[sid] = d_aln.get(sid, '') + seq #to call a dictionary and check if the key exists, if does not return default -'' empty string
	return d_aln

def get_profile(d_aln): #a list of lists for each al a vector of 20 elements
	profile =[]
	n=len(d.aln_values()[0])
	sids = d.aln_keys() #look for each key which is AA
	for i in range (n):
		aas=[] #list of letters
		for j in sids:
				aas.append(d.aln[j][i]) #for each position show 
		vass=get_iprofile(aas)
		tot=float(vaas[:20].sum()) #to find frequencies of each aa
		print (tot)
		for j in range(20):
			vaas[j] = vaas[j]/tot
		profile.append(vaas) 
	print profile

def get_iprofile(aas, aa_list='ACDEFGHIKLMNPQRSTVWY-'): #a string because of using find
	v=np.zeros(len(aa_list))
	for aa in aas:
		pos=aa_list.find(aa) #find a position
		if pos > -1: v[pos] += 1 #if not found
	print v

def print_profile(profile, aa_list='ACDEFGHIKLMNPQRSTVWY-' ):
	n=len(profile)
	for i in range(n):
		pi = profile [i][:20]
		s=0.0
		for j in range(20):
			if pi[j] > 0: s = s - pi[j] * np.log(pi[j])
		#s = np.sum(-pi*np.log(pi))
		pm = pi.argmax
		print i+1, aa_list[pm], s, pi[pm], profile[i][20]




if __name__ == '__main__':
		alnfile = sys.argv[1] #a file contains MSA
		d_aln = get_aln(alnfile)
		print (d_aln)
		profile = get_profile(d_aln)
		print_profile(profile)
		#for sid in d_aln.keys():
			#print sid, d_aln[sid] #print a key and the value
