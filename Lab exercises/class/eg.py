#User le input gareko number ko reminder,division ra sum..
num=int(input("Enter any number:"))
sum=0
while num>0:
    rem=num%10
    print(rem)
    sum=sum+rem
    num = num // 10
print(sum)