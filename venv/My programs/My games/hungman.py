#The word to guess is represented by a row of dashes. If the player guess a letter which exists in the word,
#the script writes it in all its correct positions.  The player has 10 turns to guess the word.

word="secret"
print("..Hungman Game....")
no_turns =5
i=0
while no_turns >= 1:
    guess=input("Guess a letter")
    if guess == word[i]:
        print(guess)
    else:
        print("-")
    i +=1
    no_turns -=1
