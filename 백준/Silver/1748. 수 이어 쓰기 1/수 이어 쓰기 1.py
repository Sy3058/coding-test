n = input()
ans = 0
for i in range (1, len(n)):
  ans += 9 * (10 ** (i - 1)) * i

# 남은 자리 추가
ans += (int(n) - 10 ** (len(n) - 1) + 1) * len(n)
print(ans)