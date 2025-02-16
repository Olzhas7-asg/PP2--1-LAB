#task1
'''
import math
degree = float(input("Input degree: "))
radian = math.radians(degree)
print("Output radian:", radian)
'''
#task2
'''
height = float(input("Enter the height of the trapezoid: "))
base1 = float(input("Enter the first base of the trapezoid: "))
base2 = float(input("Enter the second base of the trapezoid: "))
area = 0.5 * height * (base1 + base2)
print(f"The area of the trapezoid is: {area}")
'''
#task3
'''
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

if n == 4:  
    area = s ** 2
else:
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print(f"The area of the polygon is: {area}")
'''kk
#task4

base = float(input ("Enter base: "))
length = float(input ("Enter length of side: "))
area = base * length
print (f"Area of the parrallelogram: {area}")



