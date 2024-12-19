import sys

n, m = map(int, sys.stdin.readline().split())
mk = set([sys.stdin.readline().strip() for _ in range (n)]) # 메모장에 적은 키워드

for _ in range (m):
  words = set(sys.stdin.readline().strip().split(','))
  mk -= words
  print(len(mk))