from pathlib import Path
path =Path('learning_python.txt')
contest = path.read_text().strip()
line = contest.splitlines()
l =[]

for i in line :
    finall =i.replace('python','snake')#just a dumb example haha
    l.append(finall)

for i in l:
    print(i)