''' Game finding a secret number within 3 attempts using while loop.'''

secret_number=9
guess_count=0
guess_limit=3

while guess_count<guess_limit:
    guess=int(input("Guess the number:"))
    guess_count += 1

    if guess == secret_number:
        print("You are right!")
        break
    print('You are wrong')
