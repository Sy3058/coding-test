s = input()
ans = ''
for x in s:
  if x.isupper():
    ans += chr(ord("A") + (ord(x) - ord("A") + 13) % 26)
  elif x.islower():
    ans += chr(ord("a") + (ord(x) - ord("a") + 13) % 26)
  else:
    ans += x
print(ans)