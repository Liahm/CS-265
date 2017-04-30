import sys
import collections
import fileinput

if len( sys.argv ) < 2 :  # no file name
	f = fileinput.input()
else :
	fName = sys.argv[1] 
	f = open(fName, "r")

d = {}

l = f.readline() #Read the first line of the file
while l :
	l =l.strip(" \t\n") #Remove leading/trailing whitespaces
	s = l.split(" ", 1) 
	d[int(s[0])] = s[1] #Add the record into the dictionary
	l = f.readline()    #Read the next line of the file

for key in sorted(d):
	print "%d %s" % (key, d[key]) #Print output
