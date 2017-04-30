import sys


if len( sys.argv ) < 2 :  # no file name
	print 'ERROR:'
	sys.exit()
else :
	fName = "students.csv"
 
f = open( fName, "r" )  # open file for reading (default)

l = f.readline()
while l :
	l = l.strip( ' \t\n' ) # get rid of whitespace
	s = l.split(",") #Split the string into individual components and add a
comma
	length = len(s[1:])
	i = 1 
	total = 0
	while i<=length :
		total += float(s[i])
		i += 1
	
	total = int(round(total/length))
	print '{0} {1}'.format(s[0], total)

	l = f.readline()	

    
