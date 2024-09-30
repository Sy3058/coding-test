n, m = map(int, input().split())

if n >= m:
  ans = (m-1) + (n-1)*m
elif n < m:
  ans = (n-1) + (m-1)*n

print(ans)