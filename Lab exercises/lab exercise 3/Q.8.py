'''Given a three digit number.Find the sum of its digit.'''

def sum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n= int(n/10)

    return sum

#Driver code
n=int(input("Enter a three digit number:"))
print(sum(n))