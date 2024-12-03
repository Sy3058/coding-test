import sys

# M 이상인 단어 중 자주 나오는 -> 길이 긴 -> 알파벳 사전 순

n, m = map(int, sys.stdin.readline().split())
voca = {}

for _ in range (n):
  v = sys.stdin.readline().strip()
  if len(v) >= m:
    voca[v] = voca.get(v, 0) + 1 # 없으면 1, 있으면 해당하는 값에 1을 추가한 값 반환

sv = sorted(voca.items(), key = lambda x: x[0]) # 사전순으로 정렬
sv = sorted(sv, key = lambda x: (x[1], len(x[0])), reverse = True) # 사전에 나온 횟수가 많은 순, 동일하다면 길이가 긴 순으로 정렬

for word, num in sv:
  print(word)