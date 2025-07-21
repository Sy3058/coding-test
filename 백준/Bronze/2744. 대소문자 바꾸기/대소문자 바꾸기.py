import sys
input = sys.stdin.readline

word = input().strip()
lower = {chr(i):chr(i+32) for i in range (65, 91)}
upper = {chr(i):chr(i-32) for i in range (97, 123)}
switch = dict(lower, **upper)
for w in word:
  print(switch[w], end='')