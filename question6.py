# Solve each of the following problems using Python Scripts. Make sure you use appropriate
#variable names and comments. When there is a final answer have Python print it to the
#screen.
#A person’s body mass index (BMI) is defined as:
#BMI=mass in kg / (height in m)2

mass=float(input('Enter the mass in kg:'))
height=float(input('Enter the height in m:'))
bmi=mass/height**2
print(f'The bmi is {bmi}')