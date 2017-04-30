
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
