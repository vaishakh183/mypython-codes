#Guess a word game.

word = "Madapeedika"
guess= ""
i=0
while guess != word and i <=2:

    guess=input("Guess the Word")
    if word.lower() == guess.lower():
        print("You guessed the word " + guess + ". It is correct. You win!!")
        exit()
    if i<2:
        print("Worng Guess.Try again")
    i +=1
if i != 3:
    print("You guessed the word "+guess+". It is correct. You Win!!")
else:
    print("You failed!!")
