n, m = map(int, input().split())

# nCm = n! / m! * (n-m)!
def fac(x):
  s = 1
  for i in range (1, x+1):
    s*=i
  
  return s

print(fac(n)//(fac(m) * (fac(n-m))))