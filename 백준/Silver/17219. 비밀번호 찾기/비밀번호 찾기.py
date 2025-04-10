import sys
input = sys.stdin.readline

n, m = map(int, input().split())
note = {}

for _ in range (n):
  site, pw = input().strip().split()
  note[site] = pw

for _ in range (m):
  s = input().strip()
  print(note[s])