n = int(input())

def fib(n):
  global c1
  if n == 1 or n == 2:
    return 1
  
  c1 += 1
  return fib(n-1) + fib(n-2)

def fibonacci(n):
  global c2
  f[1], f[2] = 1, 1
  for i in range (3, n+1):
    f[i] = f[i-1] + f[i-2]
    c2 += 1
  
  return f[n]

c1, c2 = 1, 0
f = [0] * 41
fib(n)
fibonacci(n)

print(c1, c2)