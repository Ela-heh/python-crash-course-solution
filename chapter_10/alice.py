from pathlib import Path
def count_words(filename):
    try:
        contest = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print (f"Check the file's existance first in {path}!!")
        #pass
    else:
        words = contest.split()
        nwords = len(words)
        print(f"The file {path} has about {nwords} words")
filename = ['alice.txt','uknown.txt','pi_digits.txt']
for i in filename:
    path = Path(i)
    count_words(path)


