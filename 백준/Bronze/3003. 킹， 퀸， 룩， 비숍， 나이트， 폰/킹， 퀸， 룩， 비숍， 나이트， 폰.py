import sys

need = [1, 1, 2, 2, 2, 8]
have = list(map(int, sys.stdin.readline().split()))

for i in range (len(need)):
  print(need[i] - have[i], end = ' ')