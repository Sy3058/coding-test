import sys
input = sys.stdin.readline

s = input().strip() # s <= 200,000
q = int(input())
alpha = {}

for _ in range (q):
  target, l, r = input().split()
  l, r = int(l), int(r)
  if target not in alpha:
    alpha[target] = [0] * (len(s) + 1)
    
    if s[0] == target:
      alpha[target][0] = 1

    for i in range (1, len(s)):
      if target == s[i]:
        alpha[target][i] = alpha[target][i-1] + 1
      else:
        alpha[target][i] = alpha[target][i-1]
  
  if l == 0:
    print(alpha[target][r])
  
  else:
    print(alpha[target][r] - alpha[target][l-1])