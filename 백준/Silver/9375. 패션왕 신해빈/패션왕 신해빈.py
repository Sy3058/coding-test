import sys
input = sys.stdin.readline

for _ in range (int(input())):
  n = int(input())
  sorts = {}
  for i in range (n):
    nm, srt = input().split()
    sorts[srt] = sorts.get(srt, 0) + 1
  
  cnt = 1
  for val in sorts.values():
    cnt *= (val + 1)
  
  print(cnt - 1)