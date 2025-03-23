#no users
name = []
if name :
    for name in name :
        if name == 'admin':
            print ('hello admin , would u like to see a status report?')
        else :
            print (f"hello {name},thanks for logging again")
else :
    print("we need some users!")