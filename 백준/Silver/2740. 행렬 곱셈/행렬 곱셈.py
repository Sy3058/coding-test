import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 행렬 A의 원소 M개
A = [list(map(int, input().split())) for _ in range (n)]
m, k = map(int, input().split()) # 행렬 곱 계산하려면 m 크기 동일해야함
B = [list(map(int, input().split())) for _ in range (m)]

"""
행렬곱이란?
앞 행렬의 가로(행)와 뒤 행렬의 세로(열)를 곱해서 더하는 것
ex)
a11 a12   b11 b12 b13
a21 a22   b21 b22 b23
a31 a32
일 때 행렬 곱은
a11b11 + a12b21 | a11b12 + a12b22 | a11b13 + a12b23
a21b11 + a22b21 | a21b12 + a22b22 | a21b13 + a22b23
a31b11 + a32b21 | a31b12 + a32b22 | a31b13 + a32b23
"""
C = [[0] * k for _ in range (n)]

for i in range (n):
  for l in range (k):
    for j in range (m):
      C[i][l] += A[i][j] * B[j][l]

for row in C:
  print(*row)