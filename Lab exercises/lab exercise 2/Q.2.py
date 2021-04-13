'''
write a program which accepts marks of four subjects and disp[aly total marks, percentage and grade.
Hint: More than 70% =Distinction, More than 60% =First, More than 40% =Pass, Less than 40% = Fail.
'''

first_subject=float(input("Enter the marks of first subject:"))
second_subject=float(input("Enter the marks of second subject:"))
third_subject=float(input("Enter the marks of third subject:"))
fourth_subject=float(input("Enter the marks of fourth subject:"))

total_marks=first_subject+second_subject+third_subject+fourth_subject
total_percentage=(total_marks/400)*100
print(f"The total marks is {total_marks} and percentage is {total_percentage}%")

if total_percentage>70:
    print("Distinciton!")
    print("Your grade is A")
elif total_percentage>60:
    print("First Division")
    print("Your grade is B")
elif total_percentage>40:
    print("Pass")
    print("Your grade is C")
else:
    print("You are fail.")