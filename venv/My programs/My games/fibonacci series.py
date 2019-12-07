#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Hint: The Fibonnaci seqence is a sequence of numbers where
#the next number in the sequence is the sum of the previous two numbers in the sequence.
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonnaci(limit):
    l1=[]
    i=1
    print("limit is "+ limit)
    if int(limit) ==1:
        l1.append(1)
        print(l1)
    while i < int(limit):
        




limit =input("How many Fibonnaci numbers ? ")
fibonnaci(limit)