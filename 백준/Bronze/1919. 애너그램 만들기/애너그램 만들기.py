a = input()
b = input()
cnt = 0

for i in set(a):
  if i in set(b):
    cnt += abs(a.count(i) - b.count(i)) # 만약 b에도 해당하는 알파벳이 있다면 둘의 개수 차이만큼 삭제해야함
  else: # i가 b에 없다면 a에 있는 i 개수만큼 추가
    cnt += a.count(i)
for i in set(b):
  if i not in set(a): # 겹치는 것은 위에서 검사했으므로 겹치지 않는 것만 추가
    cnt += b.count(i)

print(cnt)