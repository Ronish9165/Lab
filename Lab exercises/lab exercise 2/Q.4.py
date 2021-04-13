#If the temperature is greater than 30, it's a hot day other wise if it's less than 10; it's a cold day;, it's neither
#hot nor cold.

temperature=float(input("Enter the tempurature:"))

if temperature>=30:
    print("It's a hot day.")
elif temperature<=10:
    print("It's a cold day.")
else:
    print("It's neither hot nor cold.")