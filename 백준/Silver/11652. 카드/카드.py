import sys
input = sys.stdin.readline

n = int(input())
card = {}

for _ in range (n):
  c = int(input())
  card[c] = card.get(c, 0) + 1 # c가 없으면 기본값을 0으로 하고 1을 더함

cl = list(card.items()) # card list
cl.sort(key = lambda x:x[0]) # 카드의 숫자가 작은 순으로 정렬
cl.sort(key = lambda x:x[1], reverse = True) # 카드가 많은 순으로 정렬

print(cl[0][0])