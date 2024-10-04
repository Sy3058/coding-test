s = int(input())
dp = [1]
i = 1
temp = 1

while temp <= s:
  if len(dp)%2 == 1:
    temp = i * (2*i + 1)
    dp.append(temp)
  else:
    temp = (i+1) * (2*i + 1)
    dp.append(temp)
    i += 1

print(len(dp)-1)
