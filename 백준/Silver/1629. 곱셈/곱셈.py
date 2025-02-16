import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def multi (a, n):
  if n == 1:
    return a%c
  tmp = multi(a, n//2)
  if n%2 == 0: # 나머지 분배 법칙
    return (tmp * tmp) % c
  else:
    return (tmp * tmp * a) % c

print(multi(a, b))