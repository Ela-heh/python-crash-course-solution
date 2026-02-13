from pathlib import Path
path = Path('pi_digits.txt')
contests = path.read_text().rstrip()
lines = contests.splitlines()
for line in lines:
    print(line)