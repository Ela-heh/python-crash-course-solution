from pathlib import Path
import json
path = Path('username.json')
contest = path.read_text()
username = json.loads(contest)
print(f"Welcom back,{username}")
