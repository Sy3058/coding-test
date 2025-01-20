import sys
input = sys.stdin.readline

n = int(input())
sn = []
num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
for _ in range (n):
  s = input().strip()
  hap = 0
  for i in range (len(s)):
    if s[i] in num:
      hap += int(s[i])
  sn.append((s, hap))

sn.sort(key = lambda x:x[0]) # 사전순 정렬
sn.sort(key = lambda x:x[1]) # 자리수의 합이 작은 순
sn.sort(key = lambda x:len(x[0])) # 길이 순 정렬

for i in range (n):
  print(sn[i][0])