import sys
input = sys.stdin.readline

def dfs(cf, num): # calculation formula, number
  if num > n:
    if eval(cf.replace(" ", "")) == 0: # replace " " to calculate string
      print(cf)
  
  else:
    # in ASCII code order
    dfs(f"{cf} {num}", num + 1)
    dfs(f"{cf}+{num}", num + 1)
    dfs(f"{cf}-{num}", num + 1)

t = int(input())
for _ in range (t):
  n = int(input())
  dfs("1", 2)
  print()