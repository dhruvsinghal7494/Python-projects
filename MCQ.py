from Question import Question

questions_prompt = [
    "What is the colour of Apple?\n (a)Red/Green\n (b)Orange\n (c)Grey\n",
    "What is the colour of Guava?\n (a)Magenta\n (b)Yellow\n (c)Green\n",
    "What is the colour of Banana?\n (a)Green\n (b)Blue\n (c)Yellow\n"
]

questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "c"),
]


def run_test(questions):
    score = 0
    for question in questions:
        Answer = input(question.prompt)
        
        if Answer == question.ans:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " Correct!")

run_test(questions)