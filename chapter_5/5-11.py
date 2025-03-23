#ordinal numbers
number = []
for i in range (1,10):
    number.append(i)
x = []
for number in number:
    if number == 1:
        x.append('1st')
    elif number == 2:
        x.append('2nd')
    elif number == 3:
        x.append('3rd')
    else:
        x.append(f"{number}th")
print (x)
