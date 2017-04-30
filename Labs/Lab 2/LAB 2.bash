
#count.bash
#Variables count starting at 0
words=0
lines=0

#for files f in the command ls (use ``, which is the tilde) do
for f in `ls`; do
    #Variables are given their value.
    #words = wc(count words/lines/characters) -w(only words) of that file we add a pipe to use the ouput
    #of the previous section. Cut is used for text processing, so it extract those portions. 
    #-f1 specifies which field it extracts. -d specifies what is the field delimiter. In this case space 
  words=`wc -w $f | cut -f1 -d' '` 
    #same as words, but instead of -w is -l for lines
	lines=`wc -l $f | cut -f1 -d' '`
  echo "$f $lines $words"
done



#reextend thing
if [ $# -ne 2 ]; then
#if the number is not equal to 2
	echo "Please enter two parameters."
    #print enter 2 parameters
	exit 1
    #return value
fi
#finish if statement

for i in *$1; do
#for files i in the first directory
  mv "$i" "${i/%$1/$2}"
  #move files from i to i/first parameters/second parameters 
	if [ $? -ne 0 ]; then
    #if the last line executed and is not equal to 0
	  echo "Operation failed for file $i." 
      #print failure of the file
	fi
    #finish if statement
done
#end


#Organise Music thing
for i in *.mp3; do
	#Extract relevant names for Artist and Song and remove any leading and trailing whitespace
	artistName="$(echo -e "${i}" | cut -d'-' -f 1 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
    #file name of (print if file in i exist, with that cut the file name that is separated by -)
    #with that we replace the text that exist from - to /
	songName="$(echo -e "${i}" | cut -d'-' -f 2 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"

	mkdir -p "$artistName" #Create the directory only if it does not already exist
  mv "$i" "$artistName//$songName" #Move the files into the directory
done
