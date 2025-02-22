import re
a=input()
x = re.findall(r'[a-z]+|[A-Z][a-z]*', a)
print(x)