import sys
input = sys.stdin.readline

word = input().strip()
bomb = list(input().strip())

stack = []
n, k = len(bomb), bomb[-1]

for i in range (len(word)):
  stack.append(word[i])
  
  if word[i] == k and stack[-n:] == bomb:
    del stack[-n:]

print(''.join(stack)) if stack else print('FRULA')