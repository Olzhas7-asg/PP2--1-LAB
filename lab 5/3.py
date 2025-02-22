import re
text=input()
x =  re.search("[a-z]+(_[a-z]+)",text)
print (x)