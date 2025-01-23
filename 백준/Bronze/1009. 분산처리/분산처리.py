import sys
input = sys.stdin.readline

rem = {0:[10], 1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5], 6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}

t = int(input())
for _ in range (t):
  a, b = map(int, input().split())
  a %= 10
  pos = rem[a]
  b %= len(pos)
  print(pos[b-1])