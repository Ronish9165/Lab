'''Given a positive real number, print its fractional part.'''
import math
num=float(input("Enter the number:"))
print(math.modf(num))