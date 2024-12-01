import sys

n, k = map(int, sys.stdin.readline().split())

def division(n):
  result = []
  for i in range (1, int(n**0.5)+1):
    if n % i == 0:
      result.append(i)
      if n // i != i:
        result.append(n//i)
  result.sort()
  return result

result = division(n)
if len(result) < k:
  print(0)
else:
  print(result[k-1])