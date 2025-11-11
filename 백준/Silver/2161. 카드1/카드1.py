from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
cards = deque([i for i in range (1, n+1)])

while cards:
  print(cards.popleft(), end = " ") # 맨 앞의 카드 뽑기
  cards.rotate(-1) # 맨 앞의 카드를 맨 뒤로 보내기