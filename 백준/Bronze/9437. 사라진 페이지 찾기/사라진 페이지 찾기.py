"""
페이지 구성: [2*i + 1, 2*i + 2, n - 2*i - 1, n - 2*i]
p가 홀수라면 2*i + 1의 형태, 짝수라면 2*i + 2의 형태
따라서 i = (p-1)/2 거나 i = (p-2)/2
이를 페이지 구성 식에 대입하면
홀수일 때 페이지 구성: [p + 1, p, n - p, n - p + 1]
짝수일 때 페이지 구성: [p - 1, p, n - p + 1, n - p + 2]
"""

ab = list(map(int, input().split()))
while ab[0] != 0:
  n, p = ab # 전체 페이지 수, 선택된 한 페이지
  
  if p % 2 == 1: # p가 홀수 페이지인 경우
    group = [p + 1, n - p, n - p + 1]
  
  else:
    group = [p - 1, n - p + 1, n - p + 2]
  
  group.sort()
  print(*group)
  
  ab = list(map(int, input().split()))