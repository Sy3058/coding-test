n = input() # 방 번호

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cnt = []
snset = 0 # 6과 9의 개수에 따라 필요한 세트

for num in num_list:
  cnt.append(n.count(num))

six = cnt.pop(6)
nine = cnt.pop()

if (six + nine)%2 == 1: # 6과 9의 개수 합이 홀수인 경우
  snset = (six + nine)//2 + 1
else:
  snset = (six + nine)//2

rset = max(cnt) # 최대 개수가 필요한 세트의 수
ans = max(rset, snset) # 둘 중 최대값이 필요한 세트의 수

print(ans)