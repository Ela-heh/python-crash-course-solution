#checking usernames
current_users = ['mmd','eli','Admin','the guy','hacker','zahra']
new_users = ['Ali','eli','admin','Zahra','pwj']
copy_current_users = [current_users.lower() for current_users in current_users]
copy_new_users = [new_users.lower() for new_users in new_users]
print(copy_new_users)
print(copy_current_users)
for copy_new_users in copy_new_users:
    if copy_new_users in copy_current_users:
        print (f'{copy_new_users} ; the username is taken')
    else :
        print (f'{copy_new_users} ; the username is available')