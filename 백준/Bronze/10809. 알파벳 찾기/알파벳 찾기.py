import sys
input = sys.stdin.readline

s = input().strip()
alpha = {chr(i):-1 for i in range (97, 123)}

for i in range (len(s)):
    if alpha[s[i]] == -1:
        alpha[s[i]] = i

for value in alpha.values():
    print(value)