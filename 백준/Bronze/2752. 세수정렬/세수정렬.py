a, b, c = map(int, input().split())
answer = []

if a > b:
  sm = b
  bi = a
else:
  sm = a
  bi = b
if sm < c:
  answer.append(sm)
  if c < bi:
    answer.append(c)
    answer.append(bi)
  else:
    answer.append(bi)
    answer.append(c)
else:
  answer.append(c)
  answer.append(sm)
  answer.append(bi)

print(' '.join(map(str,answer)))