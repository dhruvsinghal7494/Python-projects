First = int(input("What is the First No.? "))
Operator = input("What is the operator(+,-,*,/,%)? ")
Second = int(input("What is the Second No.? "))

if Operator == "+":
    Result = First + Second
    print("The Solution is " + str(Result))
elif Operator == "-":
    Result = First - Second
    print("The Solution is " + str(Result))
elif Operator == "*":
    Result = First * Second
    print("The Solution is " + str(Result))
elif Operator == "/":
    Result = First / Second
    print("The Solution is " + str(Result))
elif Operator == "%":
    Result = First % Second
    print("The Solution is" + str(Result))
