#Write a Python program to convert seconds to day,hour,mintes and second.

second=int(input("Enter the value for second:"))

day=(((second//60)//60)//24)
print(f'Total day given seconds:{day}')

hour=((second//60)//60)
print(f'Total hours for given seconds:{hour}')

minute=(second//60)
print(f"Total minute for given seconds:{minute}")