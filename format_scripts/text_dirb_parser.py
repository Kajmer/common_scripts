#!/usr/bin/python
#text_dirb_parser
#parses dirb output into to files: directories and files
#Files contains "+" at the beginning of the row
#Directory contains "==> "
# Everything else is trash and should be ignored?
# Also we can ignore custom 404 answer if we gonna look at the size 
'''
sample input:
---- Scanning URL: http://192.168.31.150/ ----
==> DIRECTORY: http://192.168.31.150/bitrix/
==> DIRECTORY: http://192.168.31.150/company/
==> DIRECTORY: http://192.168.31.150/contacts/
==> DIRECTORY: http://192.168.31.150/images/
==> DIRECTORY: http://192.168.31.150/include/
==> DIRECTORY: http://192.168.31.150/login/
==> DIRECTORY: http://192.168.31.150/news/
==> DIRECTORY: http://192.168.31.150/products/
==> DIRECTORY: http://192.168.31.150/search/
==> DIRECTORY: http://192.168.31.150/services/
==> DIRECTORY: http://192.168.31.150/upload/
+ http://192.168.31.150/web.config (CODE:200|SIZE:691)

---- Entering directory: http://192.168.31.150/bitrix/ ----
==> DIRECTORY: http://192.168.31.150/bitrix/activities/
==> DIRECTORY: http://192.168.31.150/bitrix/admin/
==> DIRECTORY: http://192.168.31.150/bitrix/components/
==> DIRECTORY: http://192.168.31.150/bitrix/css/
==> DIRECTORY: http://192.168.31.150/bitrix/fonts/
==> DIRECTORY: http://192.168.31.150/bitrix/gadgets/
==> DIRECTORY: http://192.168.31.150/bitrix/images/
+ http://192.168.31.150/bitrix/index.php (CODE:200|SIZE:83)
==> DIRECTORY: http://192.168.31.150/bitrix/js/
==> DIRECTORY: http://192.168.31.150/bitrix/panel/
==> DIRECTORY: http://192.168.31.150/bitrix/services/
==> DIRECTORY: http://192.168.31.150/bitrix/sounds/
+ http://192.168.31.150/bitrix/sub (CODE:400|SIZE:0)
+ http://192.168.31.150/bitrix/subdomains (CODE:400|SIZE:0)
+ http://192.168.31.150/bitrix/subject (CODE:400|SIZE:0)
+ http://192.168.31.150/bitrix/sub-login (CODE:400|SIZE:0)
+ http://192.168.31.150/bitrix/submenus (CODE:400|SIZE:0)
+ http://192.168.31.150/bitrix/submissions (CODE:400|SIZE:0)
+ http://192.168.31.150/bitrix/submit (CODE:400|SIZE:0)

'''
def parseme(inputFileAddr, outputFileAddr):
	inputFile = open(inputFileAddr)
	outputFile = open(outputFileAddr, 'w')
	dirs = ""
	files = ""
	for line in inputFile:
		# Debug:
		# print ("line[0:13]: \"{}\" line[0:2]: \"{}\". RESULT: line[0:13] == \"==> DIRECTORY\" is {} and \"line[0:2] == \"+ \" is {}".format(line[0:13], line[0:2], line[0:13] == "==> DIRECTORY", line[0:2] == "+ "))
		if line[0:13] == "==> DIRECTORY":
			dirs = dirs + line[15:] # every else after "==> DIRECTORY: "(link)+\r\n
		elif line[0:2] == "+ ":
			files = files + line[2:] # including CODE and SIZE

	#output
	outputFile.write("DIRECTORIES:\r\n{}\r\nFILES:\r\n{}\r\n".format(dirs, files))


import argparse

parser = argparse.ArgumentParser(description="Removes uppercase duplicates, transform all text to lowercase")
parser.add_argument("-i", "--input", type=str, help="Input file to correct")
parser.add_argument("-o", "--output", type=str, help="Write to file (if empty - write to console")


args = parser.parse_args()
parseme(args.input, args.output)
