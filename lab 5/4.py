import re
text=input()
x = re.search("[A-Z]+([a-z]+)",text)
print (x)
