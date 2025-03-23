import sys
input = sys.stdin.readline

def gcd(a, b):
  while b != 0:
    r = a%b
    a, b = b, r
  return a

t = int(input())

for _ in range (t):
  m, n, x, y = map(int, input().split())

  lcm = m*n // gcd(m,n) # least common multiple
  i = 0
  flag = False

  if x > y:
    while n*i + y <= lcm:
      if (n*i) % m == x-y:
        print(n*i + y)
        flag = True
        break
      i += 1
  
  elif x < y:
    while m*i + x <= lcm:
      if (m*i) % n == y-x:
        print(m*i + x)
        flag = True
        break
      i += 1
  
  else:
    while (m*i) + x <= lcm:
      if (m*i) % n == 0:
        print(m*i + x)
        flag = True
        break
      i += 1
  
  if not flag:
    print(-1)