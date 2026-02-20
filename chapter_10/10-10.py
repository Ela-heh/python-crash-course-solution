from pathlib import Path

path = Path("alice.txt")

text = path.read_text(encoding="utf-8").lower()   # lowercase the whole text
words = text.split()              # split into words

print(words.count("the"))