dishes = input()

height = 10
for i in range (1, len(dishes)):
  if dishes[i-1] == dishes[i]:
    height += 5
  else:
    height += 10

print(height)