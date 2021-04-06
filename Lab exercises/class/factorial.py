# num=int(input('Enter the value :'))
# for i in range(1,11):
#     product= num * i
#     print(f"{num} * {i} = {product}")

#Write a program of factorial of number by using function.


def factorial(a):
    product = 1
    for i in range(1,a+1):
        product = product * i
    return product

prashant= int(input("Enter a number: "))
print(factorial(prashant))