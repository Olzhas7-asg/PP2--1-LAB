import re
text=input()
x = re.search('a.*b$', text)
print(x)