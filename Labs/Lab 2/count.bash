
words=0
lines=0

for f in `ls`; do
  words=`wc -w $f | cut -f1 -d' '`
	lines=`wc -l $f | cut -f1 -d' '`
  echo "$f $lines $words"
done
