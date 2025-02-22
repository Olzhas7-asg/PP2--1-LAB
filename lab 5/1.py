import re
txt = input()
x = re.search('a.*b', txt)
print(x)