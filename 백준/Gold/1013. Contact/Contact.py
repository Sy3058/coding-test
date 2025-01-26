import sys
import re

def check_pattern(s):
    pattern = re.compile(r'^((100+1+)|(01))+$')
    return bool(pattern.match(s))

t = int(input())
for _ in range(t):
    s = input().strip()
    print('YES' if check_pattern(s) else 'NO')