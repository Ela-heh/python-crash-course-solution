#pizza toppings
message = "enter the topping for your pizza "
message += "\n enter 'quit' to stop \n :"
pizza = ""
while pizza != 'quit' :
    pizza = input (message)
    if pizza != 'quit':
        print ("we'll add the topping to your pizza")