import sys
input = sys.stdin.readline

k, l = map(int, input().split())
waiting = {}

for i in range (l):
  sn = input().strip()
  waiting[sn] = i # 학생번호가 key일 때 value를 i로 계속 갱신해줌

wl = list(waiting.items())
wl.sort(key = lambda x:x[1]) # value를 기준으로 정렬

for j in range (k): # k번째까지 학생번호 출력
  if j >= len(wl):
    break
  print(wl[j][0])