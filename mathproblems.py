import math

# x = 9.1
# print(math.pi)
# print(math.e)
# print(math.sqrt(x))
# print(math.ceil(x))
# print(math.floor(x))

# 1. Finding circumference

# C = 2 pi r
radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference,2)}cm")

# 2. Finding Area of a circle

# A = pi r square
radius = float(input("Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is : {round(area, 2)}cm^2")

# 3. Hypotenuse of right angle triangle

# c = square root of (a square + b square)
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C = {c}")



