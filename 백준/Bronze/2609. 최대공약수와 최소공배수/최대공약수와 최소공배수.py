a, b = map(int, input().split())
n = max(a, b)
m = min(a, b)

def gcd(n, m):
  while m != 0:
    tmp = n % m
    n, m = m, tmp
  return n

ans = gcd(n, m)
print(ans)
print(int(n*m//ans))