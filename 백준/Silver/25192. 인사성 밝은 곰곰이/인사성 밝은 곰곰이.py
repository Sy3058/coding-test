import sys
input = sys.stdin.readline

n = int(input())
p = set()
ans = 0
for _ in range (n):
  chat = input().strip()
  if chat == 'ENTER':
    ans += len(p)
    p = set()
  else:
    p.add(chat)

ans += len(p)

print(ans)