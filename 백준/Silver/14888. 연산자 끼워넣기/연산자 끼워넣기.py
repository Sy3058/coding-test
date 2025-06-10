import sys
input = sys.stdin.readline

n = int(input())
arr = list(input().split())
c = list(map(int, input().split()))
visited = [False] * (n-1)
op = ('+', '-', '*', '/')
maxv, minv = -1e10, 1e10
calculated = set()

def calculate(n1, n2, oper):
  n1, n2 = int(n1), int(n2)
  if oper == '+':
    return n1 + n2
  elif oper == '-':
    return n1 - n2
  elif oper == '*':
    return n1 * n2
  else:
    if n1 >= 0:
      return n1 // n2
    else:
      return -(-n1 // n2)

def sol(idx, cur_v, ops_used):
  global maxv, minv

  if idx == n:
    maxv = max(maxv, cur_v)
    minv = min(minv, cur_v)
    return
  
  for i in range (4):
    if ops_used[i] > 0:
      nv = calculate(cur_v, arr[idx], op[i])
      ops_used[i] -= 1
      sol(idx + 1, nv, ops_used)
      ops_used[i] += 1
    
sol(1, int(arr[0]), c)
print(maxv)
print(minv)