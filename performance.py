#!/usr/bin/python #generate a confusion matrix
import sys
import math


def get_blast(filename): #a dict of all ID and then append all scores
	flist = []
	d = {}
	f = open(filename)
	for line in f: 
		v = line.rstrip().split()
		d[v[0]] = d.get(v[0], [])
		d[v[0]].append([float(v[1]), int(v[2])]) #append for each ID
	for v in d.values():
		v.sort()
		flist.append(v[0]) #lowest evalue
	return flist



def get_data(filename):
	ldata = []
	f = open(filename)
	for line in f:
		v = line.rstrip().split()
		ldata.append([float(v[1]), int(v[2])])
	return ldata




def get_cm(data,th):
	#cm = [[TP, FP], [FN, TN]]
	#0 negatives, 1 positives
	cm = [[0.0, 0.0], [0.0, 0.0]]
	for i in data:
		if i[0]<th and i[1] == 1:
			cm[0][0] = cm[0][0]+1
		if i[0]>=th and i[1] == 1:
			cm[1][0] = cm[1][0]+1
		if i[0]<th and i[1] == 0:
			cm[0][1] = cm[0][1]+1
		if i[0]>th and i[1] == 0:
			cm[1][1] = cm[1][1]+1
	return cm




def get_acc(cm):
	return float(cm[0][0]+cm[1][1])/(sum(cm[0])+ sum(cm[1]))

def mcc(m): #matthew correlation
  	d=(m[0][0]+m[1][0])*(m[0][0]+m[0][1])*(m[1][1]+m[1][0])*(m[1][1]+m[0][1]) #sum of all pos and neg
  	return (m[0][0]*m[1][1]-m[0][1]*m[1][0])/math.sqrt(d)

def FPR(cm):
	return (float(cm[0][1]/(cm[0][1]+cm[1][1])))*100


def TPR(cm):
	return (float(cm[0][0]/(cm[1][0]+cm[0][0])))

if __name__ == "__main__":
	filename=sys.argv[1]
	data = get_blast(filename)
	#FPR = []
	#TPR = []
	for i in range(20):
		th = 10**-i
		cm = get_cm(data,th)
		acc = get_acc(cm)
		print 'TH:', th,'ACC:', get_acc(cm), 'MCC:', mcc(cm), cm, FPR(cm), TPR(cm)
	
	
