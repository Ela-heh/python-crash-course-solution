numbers = {
'Eli' : [7 ,10 ,22],
'mmd' : [6],
'eric' :[21 , 0],
'ali': [313] ,
'jakob' : [11]
}
for name , number in numbers.items() :
    print (f"{name.title()}")
    for number in number:
        print (number)
