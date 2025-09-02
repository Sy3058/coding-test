def get_profit(w): # 일꾼이 채취한 벌통
  max_profit = 0
  for bit in range (1, 2**m):
    ta = 0 # total amount
    tp = 0 # total profit
    for i in range (m):
      if (bit >> i) & 1: # 해당 벌통을 사용한 것
        ta += w[i]
        tp += w[i] ** 2
        if ta > c: break # 꿀은 c까지만 채취 가능
    # 현재 조건에서 얻은 이익과 최대 이익을 비교해서 갱신
    if ta > c: continue
    max_profit = max(max_profit, tp)
  return max_profit

for tc in range (1, int(input()) + 1):
  n, m, c = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range (n)]
  ans = 0 # 일꾼 1과 일꾼 2가 채취한 꿀의 최대 이익

  for i1 in range (n):
    for j1 in range (n-m+1): # 한줄에 m개씩 선택가능하므로
      w1 = [arr[i1][j1 + dm] for dm in range (m)] # 첫번째 일꾼이 일해서 얻을 수 있는 꿀의 양
      mpw1 = get_profit(w1)
      for i2 in range (i1, n):
        if i2 == i1: # 한 줄에 두개 선택하는 경우
          for j2 in range (j1+m, n-m+1):
            w2 = [arr[i2][j2 + dm] for dm in range (m)] # 두번째 일꾼이 일해서 얻을 수 있는 꿀의 양
            mpw2 = get_profit(w2)
            ans = max(ans, mpw1 + mpw2)
        
        else:
          for j2 in range (n-m+1):
            w2 = w2 = [arr[i2][j2 + dm] for dm in range (m)] # 두번째 일꾼이 일해서 얻을 수 있는 꿀의 양
            mpw2 = get_profit(w2)
            ans = max(ans, mpw1 + mpw2)
  print(f"#{tc} {ans}")