height = []

for _ in range (9):
  h = int(input())
  height.append(h)

height.sort()
diff = sum(height) - 100

for i in range (9):
  if diff-height[i] in height:
    a = height[i]
    b = diff-height[i]
    height.remove(a)
    height.remove(b)
    break

for j in range (7):
  print(height[j])