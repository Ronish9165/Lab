#If name is less than 3 characters long- name must be at least 3 characters otherwise if it's more than 50 characters
# -name must be maximum of 50 characters  otherwise - name looks good!.

name=input("Enter the name:")
length=len(name)

if length<=3:
    print("Name must be at least 3 characters long")
elif length>=50:
    print("Name must be maximum of 50 characters.")
else:
    print("Name looks good")