import sys
import math

if len( sys.argv ) < 2 :  # no file name
	print 'ERROR:'
	sys.exit()
else :
	fName = "students" 

f = open (fName, "r") #open file for reading

l = f.readline()

while l :
   l = l.strip (' \t\n' ) #Remove whitespaces
   s = l.split() #split strings into "chars"
   length = len(s[1:])
   i = 1
   total = 0 #Value of student scores
   while i<length :
      total += float(s[i]) #+1 total
      i += 1
   total = int(round(total/length))#Average
   print '{0}{1}'.format(s[0], total) #Prints formatted output

   l = f.readline() #Next line
