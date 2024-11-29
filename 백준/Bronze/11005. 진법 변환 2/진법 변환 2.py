import sys
import string

values = [i for i in range (0, 36)]
num_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keys = num_keys + list(string.ascii_uppercase)
base = dict(zip(values, keys))
ans = ''

N, B = map(int, sys.stdin.readline().split())

while N:
  ans += base[N%B]
  N //= B

ans = ans[::-1]

print(ans)