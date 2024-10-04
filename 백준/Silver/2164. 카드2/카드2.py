import sys

n = int(sys.stdin.readline()) # num of card

cards = [i+1 for i in range (n)] # cards list

while len(cards) != 1:
  if len(cards)%2 == 0:
    cards = cards[1::2] # 하나는 버리고 하나는 아래로 넘기므로 짝수 인덱스만 남기는 것과 동일한 결과
  else:
    cards.pop(0)
    temp = cards.pop(0)
    cards.append(temp)

print(cards[0])