n = int(input())

a, b = 1, 1
for _ in range (3, n+1): # 1, 2는 이미 정의되어 있으므로 3부터 확인
  a, b = b, a+b # a = f(n-1); b = f(n-2)

print(b, n-2)