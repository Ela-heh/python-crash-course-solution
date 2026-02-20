from pathlib import Path
path = Path("guest.txt")
contents = input("Please Enter Your Name : ")
path.write_text(contents)