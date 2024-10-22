N = int(input())
stack = []
buildings = []
ans = 0

for _ in range (N):
  building = int(input())
  buildings.append(building)

for b in buildings:
  while stack and stack[-1] <= b: # 현재 건물보다 작으면 스택에서 제거
    stack.pop()
  ans += len(stack) # 스택에 남은 건물은 현재 건물보다 높은 건물
  stack.append(b)

print(ans)