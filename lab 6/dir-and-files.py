'''
import os
all = list(os.listdir())
print(all)
'''
'''
import os

def checkAccess(s : str):
    if os.path.exists(s):
        print("path exists")
        if os.access(s , os.R_OK):
            print("readable")
        else:
            print("not readable")
        if os.access(s , os.W_OK):
            print("writable")
        else:
            print("not writable")
        if os.access(s , os.W_OK):
            print("executable")
        else:
            print("not executable")
    else:
        print("path does not exists")
    return 0
'''
'''
import os

def check(s : str):
    if os.path.exists(s):
        print("path exists")
        print(os.path.basename(s))
        print(os.path.dirname(s))
    else:
        print("path does not exists")
    return 0
s = 'c:/Users/nndan/OneDrive/Рабочий стол/pp2/lab 5/8.py'
check(s)
'''
'''
s = "C:/Users/nndan/OneDrive/Рабочий стол/pp2/lab 6/file2.txt"
def countLines(s : str):
    with open(s) as f:
        x = 0
        for i in f:
            x += 1
    return x
print(countLines(s))


'''

'''
a = ["result" , "is" , ":" , "text"]
b = "C:/Users/nndan/OneDrive/Рабочий стол/pp2/lab 6/file.txt"
def listToFile(a : list , b : str):
    with open(b , "w") as f:
        for i in a:
            f.write(i)

'''
'''
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt")

generate_text_files()
'''
'''
first = "C:/Users/nndan/OneDrive/Рабочий стол/pp2/lab 6/file.txt"
second = "C:/Users/nndan/OneDrive/Рабочий стол/pp2/lab 6/file2.txt"
def copyOneToAnother(s1 : str , s2 : str):
    a = open(s1 , 'r')
    b = open(s2 , 'w')
    x = a.read()
    b.write(x)
    a.close()
    b.close()
    return 0
copyOneToAnother(first , second)
'''

'''
import os

def deleteFile(s : str):
    if os.path.exists(s):
        os.remove(s)
    else:
        print("No such file or directory exists")
s = "C:/Users/nndan/OneDrive/Рабочий стол/pp2/lab 6/file3.txt"
deleteFile(s)
'''




