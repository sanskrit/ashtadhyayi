# -*- coding: utf-8 -*-
"""
ngram.py
To generate words having unique ngrams.   
"""
import sys, re
import codecs,glob
import transcoder
from lxml import etree

class sn():
	def __init__(self,line):
		[self.num,self.text,self.scrap1,self.scrap2] = line.split(u'|')

def fname(inputfilename):
	x = inputfilename.replace('../../../SanskritVerb/Data/allsutrani\\','')
	outfilename = re.sub('([1-8])[.]([1-4])[.]([0-9]+)[.]htm','../../nyasa/pada-\g<1>.\g<2>/\g<1>.\g<2>.\g<3>.md',x)
	return outfilename

def postprocess(line):
	x = line.replace('&quot;','`')
	m = re.search('<div>([^<]*) <span class="sUtramIndex">, ([^<]*)</span> </div><p>',x)
	if m:
		rep = '---\nindex:  '+transcoder.transcoder_processString(m.group(2),'deva','slp1')+'\nsutra:  '+m.group(1)+'\nvritti:  nyasa\n---\n\n'
		x = re.sub('<div>([^<]*) <span class="sUtramIndex">, ([^<]*)</span> </div><p>',rep,x)
	x = re.sub('<span class="sUtramIndex"><a href="([0-9.]+)[.]htm">([^<]*)</a></span>','(\g<1>)',x)
	x = x.replace('<span class="prashna">','')
	x = x.replace('<span class="vArtikA">','')
	x = re.sub('[<][^>]*[>]','',x)
	x = x.strip()
	x += '\n'
	return x
	
if __name__=="__main__":
	inputfiles = glob.glob('../../../SanskritVerb/Data/allsutrani/*.htm')
	flog = codecs.open('nyasa_log.txt','w','utf-8')
	for inputfile in inputfiles:
		fin = codecs.open(inputfile,'r','utf-8')
		data = fin.read()
		fin.close()
		outfile = fname(inputfile)
		print outfile
		fout = codecs.open(outfile,'w','utf-8')
		splits = data.split(u'<div class="heading">न्यासः</div>')
		if len(splits) == 2:
			splits2 = splits[1].split(u'<div class="heading">बाल-मनोरमा</div>')
			if len(splits2) == 2:
				nyasadata = splits2[0]
			else:
				splits2 = splits[1].split(u'<div class="heading">तत्त्व-बोधिनी</div>')
				if len(splits2) != 2:
					if len(splits2) == 1:
						splits2 = splits[1].split(u'</body></html>')
						nyasadata = splits2[0]
					else:
						flog.write(inputfile+'\n'+str(len(splits2))+' next item issue\n')
						nyasadata = ''
				else:
					nyasadata = splits2[0]
		else:
			nyasadata = ''
			flog.write(inputfile+'\n'+str(len(splits))+' nyasa issue\n')
		nyasadata = postprocess(nyasadata)
		fout.write(nyasadata)
	flog.close()
	