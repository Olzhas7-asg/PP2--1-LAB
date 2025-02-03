#1
'''
def grams_to_ounces(grams):
    return 28.3495231 * grams

gram = int (input())
print (grams_to_ounces(gram))'''

#2
'''
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

f_value = float(input("Enter Fahrenheit temperature to convert to Celsius: "))
print(f"{f_value}°F is {fahrenheit_to_celsius(f_value):.2f}°C")'''

#3
'''
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return "No solution"

heads = int(input("Enter the number of heads:"))
legs = int (input ("Enter the number of legs:"))
chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
'''

#4
'''
import math 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))


num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
prime_numbers = filter_prime(num_list)
print("Prime numbers:", prime_numbers)
'''
#5
'''
from itertools import permutations

def print_permutations(string):
    perm_list = [''.join(p) for p in permutations(string)]
    print("Permutations:", perm_list)

user_string = input("Enter a string to get its permutations: ")
print_permutations(user_string)
'''

#6
'''
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

user_sentence = input("Enter a sentence to reverse words: ")
print("Reversed sentence:", reverse_words(user_sentence))
'''

#7

'''
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = list(map(int, input("Enter a list of numbers:  ").split()))
print("Contains consecutive 3s:", has_33(nums))

'''
#8

'''def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


spy_nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Contains 007 in order:", spy_game(spy_nums))
'''
#9

'''import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

radius = float(input("Enter the radius of the sphere: "))
print("Volume of the sphere:", sphere_volume(radius))
'''
#10
'''
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


user_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("List with unique elements:", unique_elements(user_list))
'''

#11
'''
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


user_input = input("Enter a word or phrase to check if it's a palindrome: ")
if is_palindrome(user_input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
'''
#12
'''
def histogram(lst):
    for num in lst:
        print('*' * num)

user_input = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
histogram(user_input)
'''

#13
'''
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

guess_the_number()
'''
#14
import random
import math



def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for num in lst:
        print('*' * num)

def main():
    print("Testing functions:\n")
    
    # Test reverse_words
    sentence = "We are ready"
    print("Reversed words:", reverse_words(sentence))
    
    # Test has_33
    num_list = [1, 3, 3]
    print("Contains consecutive 3s:", has_33(num_list))
    
    # Test spy_game
    spy_list = [1, 2, 4, 0, 0, 7, 5]
    print("Contains 007 in order:", spy_game(spy_list))
    
    # Test sphere_volume
    radius = 3
    print("Volume of sphere:", sphere_volume(radius))
    
    # Test is_palindrome
    word = "madam"
    print("Is palindrome:", is_palindrome(word))
    
    # Test histogram
    hist_values = [4, 9, 7]
    print("Histogram:")
    histogram(hist_values)

if __name__ == "__main__":
    main() 

 




    