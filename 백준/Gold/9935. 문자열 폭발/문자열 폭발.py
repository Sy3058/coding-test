import sys
input = sys.stdin.readline

word = input().strip()
bomb = list(input().strip())
stack = []
sb = set(bomb)

for i in range (len(word)):
  stack.append(word[i])
  
  while len(stack) >= len(bomb) and stack[-len(bomb):] == bomb:
    for _ in range (len(bomb)):
      stack.pop()

print(''.join(stack)) if stack else print('FRULA')