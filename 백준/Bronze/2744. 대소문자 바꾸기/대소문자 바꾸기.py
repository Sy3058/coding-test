import sys
input = sys.stdin.readline

word = list(input().strip())
lower = {chr(i):chr(i+32) for i in range (65, 91)}
upper = {chr(i):chr(i-32) for i in range (97, 123)}
switch = dict(lower, **upper)
for i in range (len(word)):
  word[i] = switch[word[i]]
print(''.join(word))