'''
Functions having no parametrer and no return type.
'''

def add():
    print('Function start')
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a+b
    print(c)
    print("Function end")

print("Main start")
print("Function is calling")
add()
print("Program end")

# Functions having parameter and no return type
# def sum(a,b):
#     print(f'the sum of {a} and {b} is {a+b}')
#
# sum(4,5)

#Functions having no parameter and with return type.
# def sum():
#     a = int(input("Enter the first number:"))
#     b = int(input("Enter the second number:"))
#     return a+b
# c=sum()
# print(c)


# Functions having parameter and with return type.
# def sum(x,y):
#     return x+y
# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c=sum(2,3)
# print(C)