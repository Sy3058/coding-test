cards = [i for i in range (1, 21)]

def change(a, b, cards):
  change_list = []
  change_list = cards[a:b]
  change_list.reverse()
  j = 0
  for i in range (a, b):
    cards[i] = change_list[j]
    j += 1
  return cards

for _ in range (10):
  a, b = map(int, input().split())
  a -= 1 # 인덱스이므로 -1
  cards = change(a, b, cards)

print(' '.join(map(str, cards)))