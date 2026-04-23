import re

with open('data.txt', 'r', encoding='utf-8') as f:
    s = f.read().strip()
    parts = re.split(r'Q{3,}', s)
    print(parts)