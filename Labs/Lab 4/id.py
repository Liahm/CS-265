import sys
import collections


if len( sys.argv ) < 2 :  # no file name
	print 'ERROR:'
	sys.exit()
else :
	fName = "ids" 

f = open(fName, "r") #Open the file
d = {}

l = f.readline() #Read the first line of the file
while l :
	l =l.strip(" \t\n") #Remove the whitespaces
	s = l.split(" ", 1) 
	d[int(s[0])] = s[1] #Add the record to the dictionary
	l = f.readline()

for key in sorted(d):
	print "%d %s" % (key, d[key])

    
