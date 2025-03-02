''' 
from functools import reduce 
def multiply_list(numbers):
    return reduce (lambda x,y: x*y, numbers)

numbers = [2, 3, 4, 5]
print (multiply_list(numbers))
'''
'''
def count_letters(string):
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    return upper_count, lower_count

string = "Hello world!"
upper_count, lower_count = count_letters(string)
print (upper_count)
print (lower_count)
'''
'''
def ispalindrome(string):   
    return string == string[::-1]
    
string = "kazak"
print (ispalindrome(string))
string = "radio"
print (ispalindrome(string))
'''
'''
import time
import math
def delayed_square_root(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

number = 25100
delay = 2123
result = delayed_square_root(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")
'''
'''
def all_element_true(t):
    return all(t)

t=(True, True, True)
print (all_element_true(t))
t=(False, True, False)
print (all_element_true(t))
'''