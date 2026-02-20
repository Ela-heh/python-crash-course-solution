from pathlib import Path
path = Path('pi_digits.txt')
contest = path.read_text()

lines = contest.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip().rstrip()

#print(float(pi_string)+1)
#print(f"{pi_string[:30]}...")
#print(len(pi_string))
while True:
    birthday = input ("Give me your birth year : \n")
    if birthday in pi_string:
        print("u are part of pi HAHA!")
    else:
        print("Nope ! U are not special :>")