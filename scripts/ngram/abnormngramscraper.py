# -*- coding: utf-8 -*-
"""
ngram.py
To generate words having unique ngrams.   
"""
import sys, re
import codecs
import string
import datetime
from math import log
import transcoder

# Function to return timestamp
def timestamp():
	return datetime.datetime.now()

def triming(lst):
	output = []
	for member in lst:
		member = member.strip()
		output.append(member)
	return output

def ngrams(input, n):
	output = []
	if n >= len(input): # Removing whole word entries.
		pass
	else:
		for i in range(len(input)-n+1):
			output.append(input[i:i+n])
	return output

def getngrams(words,nth):
	ngr = []
	for word in words:
		ngr += ngrams(word,nth)
	ngr = list(set(ngr))
	return ngr

if __name__=="__main__":
	filein = sys.argv[1]
	nth = sys.argv[2]
	nth = int(nth)
	basengramfile = codecs.open('tilltrigrams.txt','r','utf-8')
	basengrams = basengramfile.readlines()
	basengrams = triming(basengrams)
	basengramfile.close()
	workablebasengrams = [gram for gram in basengrams if len(gram)==nth]
	workablebasengrams = set(workablebasengrams)
	fin = codecs.open(filein,'r','utf-8')
	data = fin.read()
	fin.close()
	testfile = codecs.open('checkngrams.txt','a','utf-8')
	split = data.split('---')
	commentarytext = split[2]
	commentarytext = transcoder.transcoder_processString(commentarytext,'deva','slp1')
	commentarytext = re.sub('[^a-zA-Z ]+','',commentarytext)
	words = commentarytext.split(' ')
	for word in words:
		testngrams = ngrams(word,nth)
		testngrams = set(testngrams)
		if not testngrams < workablebasengrams:
			missing = list(testngrams - workablebasengrams)
			devaword = transcoder.transcoder_processString(word,'slp1','deva')
			testfile.write(devaword+':'+devaword+':'+filein+":"+transcoder.transcoder_processString(','.join(missing),'slp1','deva')+"\n")
	testfile.close()
