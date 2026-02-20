from pathlib import Path
path = Path('learning_python.txt')
contests = path.read_text().strip()
lines = contests.splitlines()
print(contests)
string = ''
for line in lines:
    string += line
print(string)