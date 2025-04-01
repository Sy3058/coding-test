import sys
input = sys.stdin.readline

s = input().strip()
nds = [s[0]]

for i in range (1, len(s)):
  if s[i] != s[i-1]:
    nds.append(s[i])

ans = min(nds.count('0'), nds.count('1'))
print(ans)