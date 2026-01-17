#2
name = input("Enter your name: ")
print("Hello, " + name + "!")




#3
import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius

print("The circumference of the circle is:", circumference)




#4
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print("The perimeter of the rectangle is:", perimeter)
print("The area of the rectangle is:", area)






#5
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

sum_numbers = a + b + c
product = a * b * c
average = sum_numbers / 3

print("Sum:", sum_numbers)
print("Product:", product)
print("Average:", average)





#6
talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

# Conversions
grams_per_lot = 13.3
lots_per_pound = 32
pounds_per_talent = 20

# Total weight in grams
total_grams = (
    talents * pounds_per_talent * lots_per_pound * grams_per_lot +
    pounds * lots_per_pound * grams_per_lot +
    lots * grams_per_lot
)

# Convert to kilograms and grams
kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")





#7
import random

# 3-digit code (numbers between 0 and 9)
code_3 = [random.randint(0, 9) for _ in range(3)]

# 4-digit code (numbers between 1 and 6)
code_4 = [random.randint(1, 6) for _ in range(4)]

print("3-digit code:", "".join(map(str, code_3)))
print("4-digit code:", "".join(map(str, code_4)))
