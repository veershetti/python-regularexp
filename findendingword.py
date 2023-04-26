import re
txt="the last word"

x=re.findall("word$",txt)
if(x):
	print("found")
else:
	print("not found")