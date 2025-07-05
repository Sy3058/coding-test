s, m = map(int, input().split())

ari = 1023
cha = s & ~ari # 현재 가격에서 아리가 가지고 있는 동전들을 제외한 값
if cha == 0: # 만약 0이라면 아리가 지불할 수 있음
  print("No thanks")

else:
  s -= ari # 1023원 이하는 모두 지불 가능하므로 불가능할 경우 항상 s가 아리가 가진 돈보다 큼
  if s & ~m: # 남은 금액에서 쿠기가 가지고 있는 동전들을 제외한 값이 0이 아닌 경우
    print("Impossible")
  
  else: # 남은 금액을 쿠기가 가진 돈으로 지불 가능한 경우
    print("Thanks")