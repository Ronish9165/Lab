#Write a program to check a number given by the user is armstrong or not.

num=int(input("Enter the number:"))
sum=0
while num>0:
    rem=num%10
    c=rem**3
    sum=c+ num
    num=num//10
print(sum)
