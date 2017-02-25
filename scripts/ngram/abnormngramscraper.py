# -*- coding: utf-8 -*-
"""
ngram.py
To generate words having unique ngrams.   
"""
import sys, re
import codecs,glob
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
	output = set()
	if n >= len(input): # Removing whole word entries.
		pass
	else:
		for i in range(len(input)-n+1):
			output.add(input[i:i+n])
	return output

def getngrams(line,nth):
	words = re.split(u' ',line)
	ngr = set()
	for word in words:
		ngr = ngr.union(ngrams(word,nth))
	return ngr

def getbasengrams(forThisBook,nth):
	booklist=['balamanorama','kashika','laghu','nyasa','samhita','tattvabodhini']
	padalist=['pada-1.1','pada-1.2','pada-1.3','pada-1.4','pada-2.1','pada-2.2','pada-2.3','pada-2.4','pada-3.1','pada-3.2','pada-3.3','pada-3.4','pada-4.1','pada-4.2','pada-4.3','pada-4.4','pada-5.1','pada-5.2','pada-5.3','pada-5.4','pada-6.1','pada-6.2','pada-6.3','pada-6.4','pada-7.1','pada-7.2','pada-7.3','pada-7.4','pada-8.1','pada-8.2','pada-8.3','pada-8.4']
	result = set()
	for book in booklist:
		print book
		if book == forThisBook:
			pass
		else:
			for pada in padalist:
				inputdir = '../../'+book+'/'+pada
				inputfiles = glob.glob(inputdir+'/*.*')
				print inputdir
				for inputfile in inputfiles:
					fin = codecs.open(inputfile,'r','utf-8')
					data = fin.read()
					text = data.split('---')[2].strip()
					text = transcoder.transcoder_processString(text,'deva','slp1')
					text = re.sub('[^a-zA-Z ]+','',text)
					result = result.union(getngrams(text.encode('utf-8'),nth))
					fin.close()
				print len(result), nth, 'gram'
	#print result
	return result	
def gettestngrams(forThisBook,nth):
	result = set()
	padalist=['pada-1.1','pada-1.2','pada-1.3','pada-1.4','pada-2.1','pada-2.2','pada-2.3','pada-2.4','pada-3.1','pada-3.2','pada-3.3','pada-3.4','pada-4.1','pada-4.2','pada-4.3','pada-4.4','pada-5.1','pada-5.2','pada-5.3','pada-5.4','pada-6.1','pada-6.2','pada-6.3','pada-6.4','pada-7.1','pada-7.2','pada-7.3','pada-7.4','pada-8.1','pada-8.2','pada-8.3','pada-8.4']
	for pada in padalist:
		inputdir = '../../'+forThisBook+'/'+pada
		inputfiles = glob.glob(inputdir+'/*.*')
		print inputdir
		for inputfile in inputfiles:
			fin = codecs.open(inputfile,'r','utf-8')
			data = fin.read()
			text = data.split('---')[2].strip()
			text = transcoder.transcoder_processString(text,'deva','slp1')
			text = re.sub('[^a-zA-Z ]+','',text)
			result = result.union(getngrams(text.encode('utf-8'),nth))
			fin.close()
		print len(result), nth, 'gram'
	return result	

if __name__=="__main__":
	filein = sys.argv[1]
	nth = sys.argv[2]
	nth = int(nth)
	basengrams = getbasengrams(filein,nth)
	#testngrams = gettestngrams(filein,2)

	print len(basengrams), 'total base ngrams'
	
	padalist=['pada-1.1','pada-1.2','pada-1.3','pada-1.4','pada-2.1','pada-2.2','pada-2.3','pada-2.4','pada-3.1','pada-3.2','pada-3.3','pada-3.4','pada-4.1','pada-4.2','pada-4.3','pada-4.4','pada-5.1','pada-5.2','pada-5.3','pada-5.4','pada-6.1','pada-6.2','pada-6.3','pada-6.4','pada-7.1','pada-7.2','pada-7.3','pada-7.4','pada-8.1','pada-8.2','pada-8.3','pada-8.4']
	logfile = codecs.open(filein+'_'+str(nth)+'gram_suspect.txt','w','utf-8')
	for pada in padalist:
		inputdir = '../../'+filein+'/'+pada
		inputfiles = glob.glob(inputdir+'/*.*')
		print inputdir
		for inputfile in inputfiles:
			fin = codecs.open(inputfile,'r','utf-8')
			data = fin.read()
			fin.close()
			text = data.split('---')[2].strip()
			text = transcoder.transcoder_processString(text,'deva','slp1')
			text = re.sub('[^a-zA-Z ]+','',text)
			words = text.split(' ')
			for word in words:
				testngrams = ngrams(word.encode('utf-8'),nth)
				if not testngrams < basengrams:
					missing = list(testngrams - basengrams)
					devaword = transcoder.transcoder_processString(word,'slp1','deva')
					logfile.write(inputfile+'\n'+devaword+':'+devaword+':'+filein+":"+transcoder.transcoder_processString(','.join(missing),'slp1','deva')+"\n")
		
	"""
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
	"""