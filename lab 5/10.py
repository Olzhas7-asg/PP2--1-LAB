text =input()
n=0
result=""
while i<len(a):
    if (a[n].isupper()):
        result+="_"
        result+=a[n].lower()
    else:
        result+=a[n]
    n+=1
print(result)
