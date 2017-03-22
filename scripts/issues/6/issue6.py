# This Python file uses the following encoding: utf-8
import re,codecs,sys,glob
"""
Usage: python issue6.py
"""
if __name__=="__main__":
	booklist=['balamanorama','kashika','laghu','nyasa','samhita','tattvabodhini']
	padalist=['pada-1.1','pada-1.2','pada-1.3','pada-1.4','pada-2.1','pada-2.2','pada-2.3','pada-2.4','pada-3.1','pada-3.2','pada-3.3','pada-3.4','pada-4.1','pada-4.2','pada-4.3','pada-4.4','pada-5.1','pada-5.2','pada-5.3','pada-5.4','pada-6.1','pada-6.2','pada-6.3','pada-6.4','pada-7.1','pada-7.2','pada-7.3','pada-7.4','pada-8.1','pada-8.2','pada-8.3','pada-8.4']
	for book in booklist:
		for pada in padalist:
			inputdir = '../../../'+book+'/'+pada
			inputfiles = glob.glob(inputdir+'/*.*')
			for inputfile in inputfiles:
				print inputfile
				fin = codecs.open(inputfile,'r','utf-8')
				lines = fin.readlines()
				fin.close()
				fout = codecs.open(inputfile,'w','utf-8')
				for line in lines:
					if re.search(u"([`][^']*')",line):
						#fout.write(inputfile+'\n')
						m = re.findall(u"[`]([^']*['])",line)
						for match in m:
							rep = match.rstrip("'")+"`"
							line = line.replace(match,rep)
						fout.write(line)
					else:
						fout.write(line)
				fout.close()