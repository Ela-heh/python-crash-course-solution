from pathlib import Path
import json
path = Path('numbers.json')
contest = path.read_text()
numbers = json.loads(contest)
print(numbers)