#Write a program to print a multiplication table of a given number by using a functions.
def mul(num):
    product = 1
    for i in range(1,11):
        product=num*i
        print(f"{num}*{i}={product}")

num=int(input("Enter a number for multiplication:"))
mul(num)