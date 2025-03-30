#Deli
sandwich_orders = ['chicken' , 'cheese' , 'taco' , 'falafel']
finished_sandwiches =  []
for sandwich in sandwich_orders:
    print (f"I made your {sandwich} sandwich order")
while sandwich_orders :
    finished = sandwich_orders.pop()
    finished_sandwiches.append(finished)
for finished in finished_sandwiches:
    print (f"these sandwiches are ready : {finished}")