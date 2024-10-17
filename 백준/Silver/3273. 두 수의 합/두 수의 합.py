from collections import deque

n = int(input()) # 수열의 크기
arr = list(map(int, input().split())) # 수열
x = int(input()) # ai + aj = x
cnt = 0 # 조건을 만족하는 쌍의 개수

arr.sort()

for i in range (len(arr)):
  if arr[i] >= x: # 합이 x여야하므로 x보다 큰 수는 연산에 필요없음
    arr = arr[:i]
    break

if x%2 == 0 and x//2 in arr: # 동일한 수를 두 번 사용할 수 없으므로 그냥 제거
  arr.remove(x//2)

deq = deque(arr)

while deq:
  if deq[0] + deq[-1] == x: # 만족하는 경우 둘을 deque에서 제거하고 cnt +1
    deq.popleft()
    deq.pop()
    cnt += 1
  elif deq[0] + deq[-1] < x: # 최소값과 최대값의 합이 x보다 큰 경우
    deq.popleft()
  else: # 최소값과 최대값의 합이 x보다 작은 경우
    deq.pop()

print(cnt)