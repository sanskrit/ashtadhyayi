#!/bin/bash

# This script was used to process the historical ashtadhyayi bodhaka sqlite3 database
# and convert it ito the files for this repo. It should not be required again.
vrittiname="balamanorama"

rm -rf $vrittiname
rm -rf "${vrittiname}_itx"

mkdir $vrittiname
mkdir "${vrittiname}_itx"

cat ${vrittiname}.out | while read line
do
  if [[ $line =~ (.*):::(.*):::(.*):::(.*) ]]; then
      laghuindex=${BASH_REMATCH[1]}
      index=${BASH_REMATCH[2]}
      mulam=${BASH_REMATCH[3]}
      vrittitext=${BASH_REMATCH[4]}
  fi
  # echo laghuindex is $laghuindex
  # echo index is $index
  # echo mulam is $mulam
  # echo vritti is $vrittitext

  filename=${vrittiname}_itx/$index.txt
  echo "---" > $filename
  echo "##index:## " $index >> $filename
  echo "##vrittiindex:## " $laghuindex >> $filename
  echo "##sutra:## "  $mulam >> $filename
  echo "##vritti: " $vrittiname "##" >> $filename
  echo "---" >> $filename
  echo "" >> $filename
  echo $vrittitext >> $filename
  echo "" >> $filename
done

ls ${vrittiname}_itx | xargs -I{} sh -c "cat ${vrittiname}_itx/{} | ./itrans2unicode.pl > $vrittiname/{}"
rename "s/.txt/.md/" $vrittiname/*
find . -name "$vrittiname/*.md" -print | xargs gsed -i 's/\*/\#/g'

for i in {1..8}
do
  for j in {1..4}
  do
    mkdir ${vrittiname}/pada-${i}.${j}
    mv ${vrittiname}/${i}.${j}.*.md ${vrittiname}/pada-${i}.${j}
  done
done

rm -rf ${vrittiname}_itx
