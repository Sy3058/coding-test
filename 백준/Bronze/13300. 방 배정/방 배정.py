import math

n, k = map(int, input().split()) # 수학여행에 참가하는 학생 수, 한 방에 배정할 수 있는 최대 인원 수
girls = [0 for _ in range (6)] # 여학생 리스트
boys = [0 for _ in range (6)] # 남학생 리스트

for _ in range (n):
  s, y = map(int, input().split()) # s: 여학생 0, 남학생 1, y: 학년
  if s == 0: # 여학생인 경우
    girls[y-1] += 1 # 인덱스이므로 학년 -1
  else:
    boys[y-1] += 1

for i in range (6):
  girls[i] = math.ceil(girls[i]/k) # 한 명만 있어도 방을 배정해야 하므로 올림
  boys[i] = math.ceil(boys[i]/k)

print(sum(girls)+sum(boys))