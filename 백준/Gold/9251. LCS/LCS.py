a = ' ' + input().strip()
b = ' ' + input().strip()
LCS = [[0] * len(b) for _ in range (len(a))]

for i in range (1, len(a)):
  for j in range (1, len(b)):
    if a[i] == b[j]: # a의 i번째 문자와 b의 j번째 문자가 같으면 길이 추가
      LCS[i][j] = LCS[i-1][j-1] + 1
    else:
      LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]) # 문자열 a와 문자열 b 중 더 긴 쪽의 최장 공통 부분 수열 길이를 유지

print(LCS[-1][-1])