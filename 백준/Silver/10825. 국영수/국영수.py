import sys
input = sys.stdin.readline

n = int(input())

scores = []
for i in range (n):
  name, a, b, c = input().split()
  a, b, c = int(a), int(b), int(c)
  scores.append([name, a, b, c])
scores.sort(key = lambda x:x[0]) # 이름 사전 순 정렬
scores.sort(key = lambda x:x[3], reverse = True) # 수학 점수 감소순
scores.sort(key = lambda x:x[2]) # 영어 점수 증가 
scores.sort(key = lambda x:x[1], reverse = True) # 국어 점수 감소

for x in scores:
  print(x[0])