import re

txt="Hello this is my first search word"

#this is to find first search word

x=re.findall("^Hello",txt)
if(x):
	print("match")
else:
	print("not found")