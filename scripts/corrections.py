# This Python file uses the following encoding: utf-8
import re,codecs,sys
# This list was used for generic corrections. After this exercise, there were a few left.
#changelist = [(u'ह्य',u'12345'),(u'ह्र',u'67890'),(u'12345',u'ह्र'),(u'67890',u'ह्य'),]
# The leftover after generic corrections are being treated now.
changelist2 = [(u'प्रगृह्र',u'प्रगृह्य'),(u'ह्यस्व',u'ह्रस्व'),(u'ह्रयं',u'ह्ययं'),(u'ग्राह्र',u'ग्राह्य'),(u'बाह्र',u'बाह्य'),(u'गृह्र',u'गृह्य'),(u'ह्यिय',u'ह्रिय'),(u'नह्र',u'नह्य'),(u'ह्रव्युत्पन्नं',u'ह्यव्युत्पन्नं'),(u'ह्रेव',u'ह्येव'),(u'ह्रात्व',u'ह्यात्व'),(u'भीह्यी',u'भीह्री'),(u'ह्रयं',u'ह्ययं'),(u'मह्र',u'मह्य'),(u'नह्र',u'नह्य'),(u'ह्यीच्छ',u'ह्रीच्छ'),(u'ह्यद',u'ह्रद'),(u'ह्रुच्य',u'ह्युच्य'),(u'ह्रर्थ',u'ह्यर्थ'),(u'ह्रत्र',u'ह्यत्र'),(u'ह्यद',u'ह्रद'),(u'व्रीह्र',u'व्रीह्य'),(u'औह्रत',u'औह्यत'),(u'गूह्र',u'गूह्य'),(u'तुह्रो',u'तुह्यो'),(u'अदुह्य',u'अदुह्र'),(u'ह्रेत',u'ह्येत'),(u'ह्येप',u'ह्रेप'),(u'तर्ह्रास',u'तर्ह्यास'),(u'समुह्र',u'समुह्य'),(u'ह्रते',u'ह्यते'),(u'भ्युह्र',u'भ्युह्य'),(u'ह्रग्ने',u'ह्यग्ने'),(u'ह्यी',u'ह्री'),(u'ह्रुक्त',u'ह्युक्त'),(u'ह्रपि',u'ह्यपि'),(u'ह्रत',u'ह्यत'),(u'जिह्य',u'जिह्र'),]
def changes(data,changelist):
	for (a,b) in changelist:
		data = data.replace(a,b)
	return data
def correction(filein):
	fin = codecs.open(filein,'r','utf-8')
	data = fin.read()
	fin.close()
	fout = codecs.open(filein,'w','utf-8')
	#data = changes(data,changelist) # For generic changes. Done once. Not required to be repeated.
	data = changes(data,changelist2) # For leftovers. Use specific words and not generic ones.
	fout.write(data)
def suspecthrlist(filein):
	fin = codecs.open(filein,'r','utf-8')
	suspectlist = codecs.open('../../scripts/suspecthr.txt','a','utf-8')
	data = fin.read()
	fin.close()
	words = data.split(' ')
	for word in words:
		if u'ह्र' in word or u'ह्य' in word:
			suspectlist.write(word+":"+word+":"+filein+"\n")
	suspectlist.close()
if __name__=="__main__":
	filename = sys.argv[1]
	correction(filename)
	#suspecthrlist(filename)
	