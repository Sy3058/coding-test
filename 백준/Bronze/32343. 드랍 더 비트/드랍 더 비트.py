n = int(input())
a, b = map(int, input().split())

# XOR 값이 최대가 되려면 a와 b의 1 위치가 달라야함
if a + b > n:
  mo = 2 * n - (a + b)
else:
  mo = a + b

ans = '0b' + '1' * mo # 이진수로 저장하기 위해 앞에 0b를 붙임

print(int(ans.ljust(n+2, '0'), 2)) # 문자열 왼쪽에 0 채움