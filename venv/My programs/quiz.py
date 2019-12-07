from question import Question
question_prmpt = [
    "What color are apples? = \n (a) Red \n (b) Orange \n (c) Yellow",
    "What color are bananas? \n (a) Red \n (b) Yellow \n (c) Orange",
    "What color are strawberries ? \n (a) Yellow \n (b) Blue \n (c) Red"
]

questions = [
    Question(question_prmpt[0],"a"),
    Question(question_prmpt[1],"b"),
    Question(question_prmpt[2],"c")
]

def run_test(questions):
    scrore=0
    for question in questions:
        answer= input(question.prompt)
        if answer == question.answer:
            scrore +=1
    print("Your score is" + str(scrore))

run_test(questions)
#passing questions list to run_test function