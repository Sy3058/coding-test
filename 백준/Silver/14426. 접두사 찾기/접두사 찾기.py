import sys
input = sys.stdin.readline

n, m = map(int, input().split())

prefix = set()

for _ in range (n):
  string = input().strip()
  for i in range (1, len(string)+1):
    prefix.add(string[:i])

cnt = 0

for _ in range (m):
  # 검사해야하는 문자열
  target = input().strip()
  if target in prefix:
    cnt += 1

print(cnt)