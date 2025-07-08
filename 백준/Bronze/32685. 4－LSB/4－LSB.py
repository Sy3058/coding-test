ans = '0b'
for _ in range (3):
  num = bin(int(input()))

  if len(num) <= 5:
    num = num[2:].rjust(4, '0')
  else:
    num = num[-4:]
  
  ans += num

print(str(int(ans, 2)).zfill(4))