'''
Weight converter: Input the weight of a person in either kg or lbs.
if the person provides his/her weight n kg then convert it into lbs else convert it to kg.
'''

weight=float(input("Enter the weight"))
weight1=input("Is weight in lbs or in kg?")

if weight1=="lbs":
    weight=weight/2.205
    print(weight,"kg")
elif weight1=='kg':
    weight=weight*2.205
    print(weight,"lbs")
else:
    print("Weight is not correct.")

