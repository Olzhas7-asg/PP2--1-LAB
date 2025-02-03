#1
'''
class MyClass:
    def __init__(self): #constructor
        pass

    def getString(self):
        string = input()
        return string

    def printString(self):
        print (self.getString().upper())

opt = MyClass()

opt.printString()
 '''

#2

'''
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2


shape = Shape()
square = Square(10)

print("Shape area:", shape.area())  
print("Square area:", square.area()) '''


'''# Getting input from me
length = int(input("Enter the length of the square: "))
square = Square(length)
square.area()'''


#3
'''
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width


length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print("Rectangle area:", rectangle.area())
'''

#4
'''import math

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


length = int(input("Enter the length of the square: "))
square = Square(length)
print("Square area:", square.area())

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print("Rectangle area:", rectangle.area())
'''

#5

'''class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


account = Account("Alice", 200)
account.deposit(100)
account.withdraw(50)
account.withdraw(300) 
'''

#6

'''import math

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


account = Account("Alice", 200)
account.deposit(100)
account.withdraw(50)
account.withdraw(300)   


is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

numbers = [2, 3, 4, 5, 10, 13, 17, 20, 23, 29, 30]
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers:", prime_numbers)'''