#Dream vacation
response = {}
number = int(input("how many people want to take this poll?"))
count = 1
while count <= number:
    name = input ("what's your name ?")
    answer = input ("if u could visit one place ,where would that be ?")
    response[name] = answer
    count += 1
for name , answer in response.items() :
    print (f"{name.title()}'s dream place is {answer.title()}")