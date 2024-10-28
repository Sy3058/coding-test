import sys
from collections import deque

text = sys.stdin.readline().strip()

# 전체 a의 개수 - window에 있는 a의 개수 = 교환해야하는 횟수
a = text.count('a') # 전체 a의 개수
window = deque(text[-a:]) # 탐색할 부분 (회전 가능하므로 오른쪽 끝을 window로 둠)
wa = window.count('a') # 탐색할 부분에 있는 a의 개수
maxa = wa # 탐색할 부분에 있는 a의 최대개수

for i in range (0, len(text)-1):
  # window 갱신
  left = window.popleft()
  right = text[i]
  window.append(right)

  # wa 갱신
  if left == 'a':
    wa -= 1
  if right == 'a':
    wa += 1
  
  if wa > maxa:
    maxa = wa
    
  if maxa == a:
    break

print(a - maxa)
