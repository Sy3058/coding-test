word = input()
ans = 1

for w in range (len(word)//2):
  if word[w] != word[-1-w]:
    ans = 0
    break

print(ans)