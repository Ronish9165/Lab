#A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in
#each class, print the smallest possible number of desks that can be purchased.
#The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
#in the first test there are three groups. the first group has 20 students and thus needs 10 desks. The second group has
#21 students, so they can get by with no fewer than 11 desks, 11 desks are also enough for the third group of 22 students
#so, we need 32 desks in total.

a=int(input("Enter the number of students in class A:"))
b=int(input("Enter the number of students in class B:"))
c=int(input("Enter the number of students in class c:"))

desk_class1=(a//2)
print(f"The number of desk required for class A is {desk_class1}")
desk_class2=(b//2)
print(f"The number of desk required for class B is {desk_class2}")
desk_class3=(c//2)
print(f"The number of desk required for class C is {desk_class3}")

remain_class1= (a % 2)
print(f"Remaining desk for first class is {remain_class1}")
remain_class2= (b % 2)
print(f"Remaining desk for second class is {remain_class2}")
remain_class3= (c % 2)
print(f"Remainig desk for third class is 20{remain_class3}")
total_desk= desk_class1 + desk_class2 + desk_class3 + remain_class1 + remain_class2 + remain_class3
print(f"Total number of desks that can be prchased is {total_desk}")