LIST1=(balamanorama kashika laghu nyasa samhita tattvabodhini)
LIST2=(pada-1.1 pada-1.2 pada-1.3 pada-1.4 pada-2.1 pada-2.2 pada-2.3 pada-2.4 pada-3.1 pada-3.2 pada-3.3 pada-3.4 pada-4.1 pada-4.2 pada-4.3 pada-4.4 pada-5.1 pada-5.2 pada-5.3 pada-5.4 pada-6.1 pada-6.2 pada-6.3 pada-6.4 pada-7.1 pada-7.2 pada-7.3 pada-7.4 pada-8.1 pada-8.2 pada-8.3 pada-8.4)

"""
rm -f suspecthr.txt
cd ..
for BOOK in "${LIST1[@]}"
do
	echo $BOOK
	cd $BOOK
	for PADA in "${LIST2[@]}"
	do
		cd $PADA
		echo $PADA
		shopt -s nullglob
		array=(*.md)
		for FILENAME in "${array[@]}"
		do
			# hr-hy corrections
			python ../../scripts/corrections.py $FILENAME
		done
		cd ..
	done
	cd ..
done
"""

"""
# rephalist scraping
rm -f rephalist.txt
cd ..
for BOOK in "${LIST1[@]}"
do
	echo $BOOK
	cd $BOOK
	for PADA in "${LIST2[@]}"
	do
		cd $PADA
		echo $PADA
		shopt -s nullglob
		array=(*.md)
		cd ../../scripts
		for FILENAME in "${array[@]}"
		do
			# rephalist creation
			php repha.php ../$BOOK/$PADA/$FILENAME
		done
		cd ../$BOOK
	done
	cd ..
done
# rephalist replacement
#python rephareplacer.py
"""

"""
# suspect bigrams and trigrams generation
rm -f ngram/checkngrams.txt
cd ..
for BOOK in "${LIST1[@]}"
do
	echo $BOOK
	cd $BOOK
	for PADA in "${LIST2[@]}"
	do
		cd $PADA
		echo $PADA
		shopt -s nullglob
		array=(*.md)
		cd ../../scripts/ngram
		for FILENAME in "${array[@]}"
		do
			# bigram creation
			#python abnormngramscraper.py ../../$BOOK/$PADA/$FILENAME 2
			# trigram creation
			python abnormngramscraper.py ../../$BOOK/$PADA/$FILENAME 3
		done
		cd ../../$BOOK
	done
	cd ..
done
"""

# Issue 10 list generation
rm -rf issues/10/issue10.txt
cd ..
for BOOK in "${LIST1[@]}"
do
	echo $BOOK
	cd $BOOK
	for PADA in "${LIST2[@]}"
	do
		cd $PADA
		echo $PADA
		shopt -s nullglob
		array=(*.md)
		cd ../../scripts/issues/10
		for FILENAME in "${array[@]}"
		do
			# Issue 10 suspect list generation
			php issue10.php ../../../$BOOK/$PADA/$FILENAME
		done
		cd ../../../$BOOK
	done
	cd ..
done
