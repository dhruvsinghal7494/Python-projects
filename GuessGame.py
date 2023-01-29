Correct_word = "Notebook"
Guessed_word = ""
Guess_Limit = int(input("In how many turns you can guess? "))
Guess_Turn = 1

while Guessed_word != Correct_word:
    Guessed_word = input("Enter Guess: ")
    if Guessed_word == Correct_word:
        print("You win!")
        break
    elif Guess_Turn < Guess_Limit:
        print("You entered the wrong Word!")
        Guess_Turn += 1
    else:
        print("You lost!")
        break
    

