print("Give me two numbers, i'll devide them\nEnter 'q' to quit .")
while True:
    first = input("\nFirst number : ")
    if first == 'q':
        break

    second = input("second number : ")
    if second =='q':
        break


    try:
        ans = int(first)/int(second)
    except ZeroDivisionError:
        print('U cant devide by zero !')
    else:
        print(ans)
