import sys
input = sys.stdin.readline

target = list(input().strip())
origin = list(input().strip())

# 만약 t[0] == 'B' 이고 t[1] == 'A': 분기점이 생김
n = len(origin)-1

def check (s, e):
  if s < e: # 뒤집히지 않은 상태
    if origin[s:e+1] == target:
      return 1
    if e - s < len(target):
      return 0
    
    if origin[s] == 'B' and origin[e] == 'A':
      if check (e, s+1):
        return 1
      else:
        return check (s, e-1)
    
    elif origin[s] == 'B':
      return check (e, s+1)
    
    elif origin[e] == 'A':
      return check (s, e-1)
    
    else:
      if origin[s:e+1] == target:
        return 1
      else:
        return 0
    
  else:
    if origin[e:s+1][::-1] == target:
      return 1
    if s - e < len(target):
      return 0
    
    if origin[s] == 'B' and origin[e] == 'A':
      if check (e, s-1):
        return 1
      else:
        return check (s, e+1)
    
    elif origin[s] == 'B':
      return check (e, s-1)
    
    elif origin[e] == 'A':
      return check (s, e+1)
    
    else:
      if origin[e:s+1][::-1] == target:
        return 1
      else:
        return 0

print(check(0, n))