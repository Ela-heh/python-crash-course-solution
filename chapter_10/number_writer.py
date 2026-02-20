from pathlib import Path
import json
numbers = [3,7,1,29,0]
path = Path('numbers.json')
contest = json.dumps(numbers)
path.write_text(contest)