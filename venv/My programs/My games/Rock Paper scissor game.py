#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
#and ask if the players want to start a new game)
#Remember the rules:
#    Rock beats scissors
#    Scissors beats paper
#    Paper beats rock

user1=input("Enter Name")
user2=input("Enter Name")
user1_input=input("Hi "+ user1 + "\n  Select one 1.Rock -2.Paper - 3.Scissors")
user2_input=input("Hi "+ user2 + "\n  Select one 1.Rock -2.Paper - 3.Scissors")

def game(first,second):
    if first == second:
        print("Its a Tie..!!")
    elif first ==1 and second ==3:
        print("Rock beats scissors "+user1 + " won")
    elif first==1 and second==2:
        print("Paper beats rock " + user2 + " won")

game(user1_input,user2_input)