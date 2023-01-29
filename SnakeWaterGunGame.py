import random

def check(comp, user):
    if comp == user:
        print("Its a draw!")
    
    elif (comp == 0 and user == 1):
        print("You lose")

    elif (comp == 1 and user == 2):
        print("You lose")

    elif (comp == 2 and user == 0):
        print("You lose")

    else:
        print("You Won!")

comp = random.randint(0,2)
user = int(input("Enter 0 for snake, 1 for water, 2 for gun: "))

print("Your No.: ", user)
print("Computer No. ", comp)

score = check(comp, user)

