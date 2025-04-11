import sys
input = sys.stdin.readline

def check(w1, w2): # word1과 word2의 최장 문자열 길이 찾기
  cnt = 0
  for i in range (min(len(w1), len(w2))):
    if w1[i] == w2[i]:
      cnt += 1
    else:
      break
  return cnt

n = int(input())
b_words = list(input().strip() for _ in range (n)) # 정렬 전의 문자열 

# 순서 정렬
words = sorted(list(enumerate(b_words)), key = lambda x: x[1])

dp = [0] * n # i번째 문자의 최장 접두사 길이 저장
ml = 0 # max_length

for i in range (n-1):
  tcnt = check(words[i][1], words[i+1][1]) # temp cnt
  ml = max(ml, tcnt)

  dp[words[i][0]] = max(dp[words[i][0]], tcnt)
  dp[words[i+1][0]] = max(dp[words[i+1][0]], tcnt)

fw = '' # first word
mdp = max(dp)
for i in range (n):
  if fw == '':
    if dp[i] == mdp: # 현재 접두사의 길이가 최장접두사의 길이와 같음
      fw = b_words[i]
      print(fw)
      prefix = fw[:ml]
  
  else:
    if dp[i] == mdp and b_words[i][:ml] == prefix: # 최장 접두사의 길이가 동일하고 접두사가 같은 단어 
      print(b_words[i])
      break