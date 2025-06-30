import math

n = int(input())

def is_prime(x):
  for i in range (2, int(math.sqrt(x)) + 1):
    if x % i == 0:
      return False
  return True

def sol(ans):
  if len(ans) == n:
    print(''.join(map(str, ans)))
    return

  for i in range (10):
    ans.append(i)
    if is_prime(int(''.join(map(str, ans)))):
      sol(ans)
    ans.pop()

for x in (2, 3, 5, 7):
  sol([x])