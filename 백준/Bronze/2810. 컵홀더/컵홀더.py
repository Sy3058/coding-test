import sys
input = sys.stdin.readline

n = int(input())
seat = input().strip()
base = n+1
couple = seat.count("L")
base -= couple//2

if base > n:
  print(n)
else:
  print(base)