import sys

s = sys.stdin.readline()
sub= set()

for i in range (len(s)):
  for j in range (1, len(s) - i):
    if i+j < len(s):
      sub.add(s[i:i+j]) # set을 사용하기 위해 list가 아니라 tuple을 append

print(len(sub))