from random import randint
my_ticket  = 2
award = []
while True:
    number =  randint(1,10)
    award.append(number)
    if number == my_ticket:
        break

print (award)
print(f"U won after {len(award)-1} people!")
