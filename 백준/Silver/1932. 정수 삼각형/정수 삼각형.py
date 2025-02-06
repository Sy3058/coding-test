import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range (n):
  row = list(map(int, input().split()))
  arr.append(row)

for i in range (n-1):
  for j in range (len(arr[i+1])):
    if j == 0:
      arr[i+1][j] += arr[i][j]
    elif j == len(arr[i+1]) - 1:
      arr[i+1][j] += arr[i][j-1]
    else:
      arr[i+1][j] = max(arr[i+1][j] + arr[i][j], arr[i+1][j] + arr[i][j-1])

print(max(arr[-1]))