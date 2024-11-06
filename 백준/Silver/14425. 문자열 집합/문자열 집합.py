import sys

N, M = map(int, sys.stdin.readline().split())
S = []
cnt = 0

for _ in range (N):
  word = sys.stdin.readline().strip()
  S.append(word)

S = set(S) # 시간 복잡도를 줄이기 위함

for _ in range (M):
  tmp = sys.stdin.readline().strip()
  if tmp in S:
    cnt += 1

print(cnt)