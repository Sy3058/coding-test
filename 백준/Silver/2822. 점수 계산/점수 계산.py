import sys
input = sys.stdin.readline
score = [(int(input()), i+1) for i in range (8)]

score.sort(key = lambda x:x[0], reverse = True) # 점수 높은 순으로 정렬
score = score[:5]
score.sort(key = lambda x:x[1]) # 문제 번호 순으로 정렬

hap = 0
pn = [] # 문제 번호
for i in range (5):
  hap += score[i][0]
  pn.append(score[i][1])

print(hap)
print(' '.join(map(str, pn)))