#No Pastrami
sandwich_orders = ['chicken' , 'cheese' , 'taco' , 'falafel','pastrami','pastrami','pastrami']
print ("Deli has run out of pastrami")
while 'pastrami' in sandwich_orders : 
    sandwich_orders.remove('pastrami')
print ("available orders :\n")
for sandwich in sandwich_orders:
    print (sandwich.title())