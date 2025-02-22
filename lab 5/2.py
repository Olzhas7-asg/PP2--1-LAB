import re
text=input()
x = re.search("a+b{2,3}$",text)
print (x)