''' Write a function called fizz_buzz that takes a number .'''

def fizzbuzz(num):
    if num%3==0 and num%5==0:
        return "fizzBuzz"

    elif num%5==0:
        return "Buzz"

    elif num%3==0:
        return "fizz"

    else:
        print(num)

d=int(input("Enter the number:"))
c=fizzbuzz(d)
print(c)
print('end of process')
