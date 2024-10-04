s = int(input())
dp = [1]
i = 1
temp = 1

while temp <= 4294967295:
  if len(dp)%2 == 1:
    temp = i * (2*i + 1)
    dp.append(temp)
  else:
    temp = (i+1) * (2*i + 1)
    dp.append(temp)
    i += 1

for i in range (1, len(dp)):
  if dp[i-1] <= s < dp[i]:
    print(i)
