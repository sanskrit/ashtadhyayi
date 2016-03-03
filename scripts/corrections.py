# This Python file uses the following encoding: utf-8
import re,codecs,sys
changelist = [(u'ह्य',u'12345'),(u'ह्र',u'67890'),(u'12345',u'ह्र'),(u'67890',u'ह्य'),]
def changes(data,changelist):
	for (a,b) in changelist:
		data = data.replace(a,b)
	return data
		
def correction(filein):
	fin = codecs.open(filein,'r','utf-8')
	data = fin.read()
	fin.close()
	fout = codecs.open(filein,'w','utf-8')
	data = changes(data,changelist)
	fout.write(data)
if __name__=="__main__":
	filename = sys.argv[1]
	correction(filename)
