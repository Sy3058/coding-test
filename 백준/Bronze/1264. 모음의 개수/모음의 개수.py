vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
text = input()

while text != '#':
  cnt = 0
  for t in text:
    if t in vowel:
      cnt += 1
  
  print(cnt)
  text = input()