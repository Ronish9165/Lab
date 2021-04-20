'''Check whether the given year is leap or not. If year is leap print 'Leap year' esle print 'Common year'.
Hint: a year is leap if its number is exactly divisible by 4 and is no exactly divisible by 100 a year is always a leap
     year if its number is divisible by 400. '''

year=int(input("Enter a year:"))
if year%4==0 and year%100 !=0 or year%400==0:
    print(f"Leap year")
else:
    print('Common year')