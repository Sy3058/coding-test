"""
KMP 알고리즘
문자는 접두사(prefix)와 접미사(suffix)로 이루어져 있음
pi 배열: prefix == suffix가 될 수 있는 부분 문자열 중에서 가장 긴 것의 길이
pi 배열을 이용해서 이미 검색한 부분을 건너뛸 수 있음
ex) P = "ababaca" 일 때
P[0] = 'a': pi[0] = 0
P[0...1] = 'ab': pi[1] = 0
P[0...2] = 'aba': pi[2] = 1 # 접두사 a, 접미사 a
P[0...3] = 'abab': pi[3] = 2 # 접두사 ab, 접미사 ab
P[0...4] = 'ababa': pi[4] = 3 # 접두사 aba, 접미사 aba
P[0...5] = 'ababac': pi[5] = 0
P[0...6] = 'ababaca': pi[6] = 1 # 접두사 a, 접미사 a
-> 패턴 내에서 반복되는 부분에 대한 정보를 저장
"""

# 1 ~ m까지의 각 j 값에 대해 최대의 k 계산하기 (P 안에서 반복되는 부분 찾기)
def make_pi():
  pi = [0 for i in range (m)] # 가장 긴 접두사이면서 동시에 접미사인 부분 문자열의 길이를 저장
  j = 0 # 현재 검사 중인 접두사의 끝 인덱스
  for i in range (1, len(P)): # 현재 검사 중인 접미사의 끝 인덱스
    # while문을 이용해서 j를 가장 적절한 위치로 옮김 (일치했던 부분 활용)
    while j > 0 and P[i] != P[j]:
      j = pi[j-1]
    
    if (P[i] == P[j]):
      j += 1
      pi[i] = j
  
  return pi

def sol(pi):
  result = []
  cnt = 0

  # pi를 만드는 것과 유사한 형태
  # j를 이용해서 접두사 확인, i를 이용해서 접미사 확인
  j = 0
  for i in range (n):
    while j > 0 and T[i] != P[j]:
      j = pi[j-1]
    
    if T[i] == P[j]:
      if j == m - 1: # 모든 부분이 일치한다면
        result.append(i - m + 2) # P가 나타나는 위치
        cnt += 1
        j = pi[j]
      else:
        j += 1
    
  print(cnt) # T 중간에 P가 나타나는 횟수

  for r in result:
    print(r) # P가 나타나는 위치

# 공백도 입력될 수 있으므로 strip 사용하지 않도록 주의
T = input()
P = input()
n = len(T)
m = len(P)
sol(make_pi())