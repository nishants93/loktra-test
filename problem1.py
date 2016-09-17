"""
	This code is used to reverse hash the string that is hashed by the formula h = h*37 + index(char in salt).
	To reverse hash the string just used the reverse_hash method and pass the hash to that function and a string will be returned.

	Usage : python problem1.py <hash>
"""
import sys

salt = "acdegilmnoprstuw"
def reverse_hash(h):
	main_string = ""
	while h > 7:
		i = h % 37
		h = (h-i)/37
		main_string = salt[i] + main_string
	return main_string


sys.argv.append("something")
if sys.argv[1] == "something":
	print "No Hash Given!"
	exit()
else:
	try:
		h = int(sys.argv[1])
		print "String for the given hash : " + reverse_hash(h)
	except ValueError:
		print "Please Enter an Integer!"
		exit()
	except:
		print "Something wierd happened!"
		exit()

