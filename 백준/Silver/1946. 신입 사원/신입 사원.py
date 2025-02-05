import sys
input = sys.stdin.readline

t = int(input())
for _ in range (t):
  n = int(input())
  p = []
  for i in range (n):
    paper, interview = map(int, input().split()) # 서류, 면접 순위
    p.append((paper, interview))
  
  p.sort(key = lambda x:x[0]) # 서류 순위로 정렬
  mv = p[0][1] # 서류 1등의 면접 순위

  cnt = 1 # 뽑힌 신입사원의 수
  for i in range (1, n):
    if p[i][1] < mv: # 서류 순위가 더 낮으므로 면접 순위가 더 높아야 합격 가능
      mv = p[i][1] # 면접 순위 갱신
      cnt += 1
  print(cnt)