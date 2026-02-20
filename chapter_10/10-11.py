from pathlib import Path
import json
fav = []
def check(path):
    if path.exists():
        contest = path.read_text()
        fav = json.loads(contest)
        return fav
    else:
        return None

def get(path):
    while True:
        number = input("Give your favorite numbers(Press 'q' to quit):  ")
        if number.lower() == 'q':
            break    
        fav.append(int(number))
    contest = json.dumps(fav)
    path.write_text(contest)
    return fav

def show():
    path= Path('fav.json')
    fav = check(path)
    if fav :
        print(f"I know your favorite number! It's {fav}")

    else:
        fav = get(path)

show()

