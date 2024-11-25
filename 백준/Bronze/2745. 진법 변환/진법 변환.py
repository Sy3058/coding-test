import sys
import string

values = [i for i in range (0, 36)]
num_keys = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
keys = num_keys + list(string.ascii_uppercase)
base = dict(zip(keys, values))
ans = 0

N, B = sys.stdin.readline().split()
B = int(B)

t = len(N) - 1
for i in range (len(N)):
  num = base[N[i]] * (B ** t)
  ans += num
  t -= 1

print(ans)