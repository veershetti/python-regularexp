import re
txt="cureent year 2023 I was born in 2020 train"
#Find all digit characters
x=re.findall("train\Z",txt)
print(x)