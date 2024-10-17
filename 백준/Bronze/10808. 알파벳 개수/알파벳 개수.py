import string

alphabet = list(string.ascii_lowercase)
ans = []

s = input() # 주어진 단어
for alpha in alphabet:
  ans.append(s.count(alpha))

print(' '.join(map(str, ans)))