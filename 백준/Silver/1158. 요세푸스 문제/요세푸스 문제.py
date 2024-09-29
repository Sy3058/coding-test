import sys

N, K = map(int, sys.stdin.readline().split())

arr = [i+1 for i in range (N)]
temp = 0
print("<", end="")

for i in range (N):
  temp = (temp+K-1)%len(arr)
  answer = arr.pop(temp)
  if i == N-1:
    print(answer, end=">")
  else:
    print(answer, end=", ")