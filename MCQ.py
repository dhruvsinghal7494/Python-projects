from Question import Question

questions = [
    "What is the colour of Apple?\n (a)Red/Green\n (b)Orange\n (c)Grey\n ",
    "What is the colour of Guava?\n (a)Magenta\n (b)Yellow\n (c)Green\n",
    "What is the colour of Banana?\n (a)Green\n (b)Blue\n (c)Yellow\n"
]

for question in questions:
    num = 0
    score = 0
    for num in questions.count():
        Question = input(question(num))

        if Question.ans() == 
