import sys
input = sys.stdin.readline

n = int(input()) # 스위치 개수
switch = list(map(int, input().split()))
s = int(input()) # 학생 수
cs = {1:0, 0:1} # 스위치 상태 변환

for _ in range (s):
  g, num = map(int, input().split()) # 성별, 받은 수
  num -= 1 # 인덱스이므로 1 빼줘야함

  if g == 1: # 남학생
    for i in range (num, n, num+1):
      switch[i] = cs[switch[i]]

  else: # 여학생
    j = 1
    switch[num] = cs[switch[num]]
    while num - j >= 0 and num + j < n:
      if switch[num+j] == switch[num-j]:
        switch[num+j] = cs[switch[num+j]]
        switch[num-j] = cs[switch[num-j]]
        j += 1
      else:
        break

for i in range (n//20 + 1):
  if i == n//20:
    print(*switch[i*20:i*20 + n%20])
  else:
    print(*switch[i*20:(i+1)*20])