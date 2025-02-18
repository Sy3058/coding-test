import sys
input = sys.stdin.readline

n, c = map(int, input().split())
ma = list(map(int, input().split())) # message array
md = {} # message dictionary
mn = list(set(ma)) # message number
md = {num:[0, 0] for num in mn}
for i in range (n):
  md[ma[i]][0] += 1 # 개수 확인
  if md[ma[i]][1] == 0: # 첫 등장 확인
    md[ma[i]][1] = i
md[ma[0]][1] = 0 # 첫 등장한 숫자의 경우 두번째로 등장했을 때로 순서가 바뀌므로 따로 지정해주어야 함

al = [] # answer list
for key, value in md.items():
  al.append((key, value[0], value[1])) # (숫자, 빈도수, 첫 등장) 순서로 저장

al.sort(key = lambda x:x[2]) # 등장한 순서대로 먼저 정렬
al.sort(key = lambda x:x[1], reverse = True) # 그 후 빈도가 큰 순서대로 정렬

answer = []
for i in range (len(al)):
  for j in range (al[i][1]):
    answer.append(al[i][0])

print(*answer)