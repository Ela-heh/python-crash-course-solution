from random import choices
l = []
my_list = [1,2,8,5,55,24,4,0,8,6421,21,34,'a','f','e','h','v']
for i in range (1,4):
    l.append(choices(my_list))
print("The Lottory winners are : \t")
for i in l:
    print(f"-{i}")
