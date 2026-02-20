from pathlib import Path
path = Path('cats.txt')
path1 = Path('dogs.txt')
file = [path,path1]
for f in file:
    try:
        text = f.read_text()
    except FileNotFoundError:
        print(f"File {f} doesn't exist")
    else:
        print(f"\nThe {f} file exists")
        print(f"The {f} file's content is:\n{text}")
