from pathlib import Path
path = Path('pi_digits.txt')
for line in path.read_text().strip().splitlines():
    print(line)