import random
number=random.randint(1,10)

#while number != guess:
 #   guess=int(input('uffs !! try again: guess again'))
#else:
 #   print('congratulations!! u are right')
while True:
     guess= int(input('please enter the number:'))
     if guess==number:
         print("congratulation")
         break
     print('wrong!')