#Q.3 N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in
#the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads
#he numbers N and K. it should print the two answers for the questions above.

N=int(input("enter the number of students:"))
A=int(input("enter the number of apples:"))
D=(N/A)
R=(N//A)

print(f"The no of apples single students got,{D}")
print(f"The number of apples remain in the basket, {R} ")
#abc