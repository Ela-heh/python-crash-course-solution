favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
people = ['jen' , 'sarah' , 'edward' , 'ali' , 'jasmin']
for people in people:
    if people in favorite_languages.keys() :
        print (f"thanks for your response {people}")
    else :
        print (f"pls take the poll {people}")
