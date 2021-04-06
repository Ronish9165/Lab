#Function having no parameter & no return type. (ADD)

def add():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=a+b
    print(f'The sum of {a} and {b} is {a+b}')

add()


#Function having parameter & no return type. (Subtract)
def sub(a,b):
    sub=a-b
    print(f'The subtraction of {a} and {b} is {a-b}')

sub(4,2)
print(sub)

#Functions having no parameter and with return type. (Multiply)

def mul():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = a*b
    return a*b
c=mul()
print(c)

#Functions having parameter and return type. (Divide)
def div(a,b):
    return a/b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

c=div(a,b)
print(C)