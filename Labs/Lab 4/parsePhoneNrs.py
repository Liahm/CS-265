import sys
import re

DEF_A_CODE = "None"

def usage() :
	print "Usage:"
	print "\t" + sys.argv[0] + " [<file>]"

def searchFile( fileName, pattern ) :

	fh = open( fileName, "r" )
	
	for l in fh :
		l = l.strip()

			# Here's the actual search
		match = pattern.search( l )
		 
		if match :
			nr = match.groups()
				# Note, from the pattern, that 0 may be null, but 1 and 2 must
				# exist
			if not nr[0] :
				aCode =	DEF_A_CODE
			else :
				aCode = nr[0]

			if not nr[3]:
				print "area code: " + aCode + \
					", exchange: " + nr[1] + ", trunk: " + nr[2]
			else:	
				print "area code: " + aCode + \
					", exchange: " + nr[1] + ", trunk: " + nr[2] + ", extension:
" + nr[3]
		else :
			print "NO MATCH: " + l
	
	fh.close()
	

def main() :

		# stick filename
	if len( sys.argv ) < 2 :  # no file name
	   # assume telNrs.txt
		fileName = "telNrs.txt"
	else :
		fileName = sys.argv[1]


		# for legibility, Python supplies a 'verbose' pattern
		#		requires a special flag
	#patString = '(\d{3})*[ .\-)]*(\d{3})[ .\-]*(\d{4})'

	patString = r'''
								# don't match beginning of string (takes care of 1-)
		(\d{3})?		# area code (3 digits) (optional)
		[ .\-)]*		# optional separator (any # of space, dash, or dot,
								#   or closing ')' )
		(\d{3})			# exchange, 3 digits
		[ .\-]*			# optional separator (any # of space, dash, or dot)
		(\d{4})			# number, 4 digits
		[ \-x]*			# optional separator (either space or dash) followed by
the optional character x
		(\d{1,4})?  # number between 1 and 4 digits
		'''

	# Here is what the pattern would look like as a regular pattern:
	#patString = r'(\d{3})\D*(\d{3})\D*(\d{4})'


	# Instead of creating a temporary object each time, we will compile this
	#		regexp once, and store this object

	pattern = re.compile( patString, re.VERBOSE )
	searchFile( fileName, pattern )

main()
