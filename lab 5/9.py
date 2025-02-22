import re
str = input()
x = re.sub(r"([A-Z])", r" \1", str)
print(x)