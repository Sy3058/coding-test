import sys
input = sys.stdin.readline

n, b = map(int, input().split())
A = [list(map(int, input().split())) for _ in range (n)]

# 행렬곱
def multi(li1, li2):
  X = [[0] * n for _ in range (n)]
  for i in range (n):
    for k in range (n):
      for j in range (n):
        X[i][k] += (li1[i][j] * li2[j][k]) % 1000
  return X

# X**5 = X**2 * X**2 * X 로 분할할 수 있음
def square(X, n): # X: 행렬 n: 제곱할 횟수
  if n == 1:
    return X
  temp = square(X, n//2)
  if n%2 == 0:
    return multi(temp, temp)
  else:
    return multi(multi(temp, temp), X)

result = square(A, b)
for i in range (n):
  for j in range (n):
    result[i][j] = result[i][j] % 1000

for row in result:
  print(*row)