import re

txt="hello planet"

#search for a sequence that starts with he, followed by 0 or more characters , and an "0""

x=re.findall("he.+o",txt)
print(x)