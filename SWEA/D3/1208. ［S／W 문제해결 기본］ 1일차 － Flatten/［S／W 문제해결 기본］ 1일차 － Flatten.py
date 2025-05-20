for tc in range (1, 11):
  dump = int(input())
  arr = list(map(int, input().split()))
  height = [0] * 101
  
  for h in arr: # 높이를 인덱스로 개수를 셈
    height[h] += 1
  
  for _ in range (dump):
    for i in range (101): # 가장 낮은 높이를 찾은 다음 개수를 하나 줄이고 그 다음 높이에 개수 추가
      if height[i] > 0:
        height[i] -= 1
        height[i+1] += 1
        break
    
    for j in range (100, -1, -1): # 가장 높은 높이를 찾은 다음 개수를 하나 줄이고 그 전 높이에 개수 추가
      if height[j] > 0:
        height[j] -= 1
        height[j-1] += 1
        break
    
    if i + 1 == j: # 만약 최저 높이와 최고 높이의 차가 1이면 멈춰도 됨
      break

  for i in range (101):
    if height[i] > 0:
      minh = i
      break
  
  for j in range (100, -1, -1):
    if height[j] > 0:
      maxh = j
      break
  
  print("#%d %d"%(tc, maxh - minh))