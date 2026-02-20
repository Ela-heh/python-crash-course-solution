print("Give me two number , I'll add them for u")

def error ():
    while True:
        try :
            
            x = int(input("\nGive me the first number : "))

            y =int(input("Give me the second number : "))

            print(f"The sum of two numbers is : {x+y} ")

        except ValueError:
            print("we can't give any output")

error()