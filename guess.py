# This is a guess the number game.


import random


print('Hello inbred. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

# print('DEBUG: Secret number is ' + str(secretNumber))

for guessesTaken in range(1, 7):
    print('Take a guess, bitch.')
    guess = int(input())

    if guess < secretNumber:
        print('You stupid. Your guess is too low.')
    elif guess > secretNumber:
        print('You are as high as a motherfucking kite.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + name + '! You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('HAH! The number I was thinking of was ' + str(secretNumber))
