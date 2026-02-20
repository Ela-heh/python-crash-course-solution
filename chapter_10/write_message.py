from pathlib import Path
path = Path('programming.txt')
contents = "I Love programming \n"
contents += "I love creating new games"
path.write_text(contents)