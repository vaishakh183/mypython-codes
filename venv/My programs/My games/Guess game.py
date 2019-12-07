#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
#then tell them whether they guessed too low, too high, or exactly right.

import random
ran_num=random.randint(1,9)
print(ran_num)
guess=input("Guess a number between 1-9")

if int(guess) == ran_num:
    print("Awesome..Your Guess is Correct")
else:
    print("Failed")