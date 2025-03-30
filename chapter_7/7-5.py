while True:
    age = input("Input your age (or type 'exit' to quit):\n")

    if age.lower() == "exit":
        print("Exiting program.")
        break

    try:
        age = int(age)
        if age < 3:
            print("The ticket is free")
        elif 3 <= age < 12:
            print("The ticket is $10")
        else:
            print("The ticket is $15")
    except ValueError:
        print("Invalid input. Please enter a number or type 'exit' to quit.")