#trying the conditional test in while statement
age = ""
while age != 'exit':
    age = input("Input your age (or type 'exit' to quit):\n")
    if age != 'exit' :
        age = int(age)

        if age < 3:
            print("The ticket is free")
        elif 3 <= age < 12:
            print("The ticket is $10")
        else:
            print("The ticket is $15")