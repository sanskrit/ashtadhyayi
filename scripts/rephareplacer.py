# This Python file uses the following encoding: utf-8
import re,codecs,sys
def rephareplacer(inputfile):
	fin = codecs.open(inputfile,'r','utf-8')
	data = fin.readlines()
	fin.close()
	for datum in data:
		if datum[0] in [u';',u'’',u'?']:
			pass
		else:
			split = datum.split(':')
			changefile = str(split[2]).strip()
			print changefile
			existing = split[0]
			replacement = split[1]
			fchange = codecs.open(changefile,'r','utf-8')
			inputdata = fchange.read()
			fchange.close()
			outputdata = inputdata.replace(existing,replacement)
			fchange1 = codecs.open(changefile,'w','utf-8')
			fchange1.write(outputdata)
			fchange1.close()
rephareplacer('rephalistforchecking.txt')
			