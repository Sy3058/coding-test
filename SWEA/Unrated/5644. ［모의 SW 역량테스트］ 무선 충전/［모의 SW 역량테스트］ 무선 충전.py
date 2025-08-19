def bc_range(x, y, idx):
  for i in range (x-c, x+c+1):
    for j in range (y-c, y+c+1):
      d = abs(x - i) + abs(y - j)
      if d <= c:
        bc_dict[idx].add((i, j))

def movement(s, op): # 시작 좌표, 이동방향
  x, y = s
  # (x, y) 는 board[y][x]
  if op == 0: # 이동하지 않음
    return (x, y)
  
  elif op == 1: # 상
    return (x, y-1)
  
  elif op == 2: # 우
    return (x+1, y)
  
  elif op == 3: # 하
    return (x, y+1)

  else: # 좌
    return (x-1, y)

for tc in range (1, int(input()) + 1):
  m, a = map(int, input().split())
  move_a = list(map(int, input().split()))
  move_b = list(map(int, input().split()))
  bc_dict = {i:set() for i in range (1, a + 1)}
  powers = [0] * (a + 1)
  ans = 0 # 총합
  for i in range (1, a+1):
    x, y, c, p = map(int, input().split())
    bc_range(x, y, i)
    powers[i] = p
  
  # 0초일 때 위치
  pos_a = (1, 1)
  pos_b = (10, 10)

  for time in range (-1, m):
    if time == -1:
      pass
    else:
      pos_a = movement(pos_a, move_a[time])
      pos_b = movement(pos_b, move_b[time])

    temp_a = []
    temp_b = []
    for i in range (1, a+1):
      if pos_a in bc_dict[i]:
        temp_a.append((powers[i], i))
      
      if pos_b in bc_dict[i]:
        temp_b.append((powers[i], i))
    
    temp_a.sort(key = lambda x:x[0], reverse = True) # 충전량 많은 순으로 정렬
    temp_b.sort(key = lambda x:x[0], reverse = True)

    if not temp_a and not temp_b:
      # 둘 다 해당하는 bc가 없는 경우
      continue

    elif not temp_a:
      ans += temp_b[0][0]
    
    elif not temp_b:
      ans += temp_a[0][0]
    
    else:
      # A와 B가 고를 수 있는 충전기 쌍 모두 탐색
      best = 0
      for pa, ia in temp_a:
        for pb, ib in temp_b:
          if ia == ib: # 같은 충전기인 경우 (나눠씀)
            best = max(best, pa)
          
          else:
            best = max(best, pa + pb)
      ans += best
  
  print(f"#{tc} {ans}")


