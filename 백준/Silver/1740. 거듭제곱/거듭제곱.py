n = int(input())

binn = bin(n)[2:]
# n번째 자리가 1이면 3**(n-1)을 사용한 것
ans = 0

for i in range (len(binn)):
  if binn[i] == '1':
    ans += 3 ** (len(binn) - 1 - i)

print(ans)