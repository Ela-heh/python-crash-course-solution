from pathlib import Path
path = Path("guest_book.txt")
print("Enter q to quit")
content = []
while True:
    contents = input("Enter your name : \n")
    if contents.lower() == 'q':
        break
    content.append(contents)

all = ''   
for i in content:
    all += i +", "
path.write_text(all)