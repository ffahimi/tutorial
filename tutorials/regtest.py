import re

def Main():
	line = "I think I understand regular expressions"

	matchResult = re.match("think", line, re.M|re.I)
	if matchResult:
		print("Match Found: " + matchResult.group())

	else:
		print("No Match Was Found")


	searchResult = re.search("think", line, re.M|re.I)

	if searchResult:
		print("search found: ", searchResult.group())
	else:
		print("nothing found in search")

if __name__=="__main__":
	Main()