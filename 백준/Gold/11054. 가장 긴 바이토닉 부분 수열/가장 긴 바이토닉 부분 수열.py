import sys
input = sys.stdin.readline

def binary_left (array, target):
  start, end = 0, len(array) - 1
  while start <= end:
    mid = (start + end) // 2
    if array[mid][0] < target[0]:
      start = mid + 1
    else:
      end = mid - 1
  return start

n = int(input())
arr = list(map(int, input().split()))
rarr = arr[::-1]
dp1, dp2, sub1, sub2 = [], [], [], []

for i in range (n):
  pos1 = binary_left(sub1, (arr[i], i)) # sub에서 arr[i]가 들어갈 위치
  if pos1 == len(sub1): # pos가 가장 큰 수인 경우
    sub1.append((arr[i], i))
  else:
    if sub1[pos1][0] != arr[i]:
      sub1[pos1] = (arr[i], i) # 기존 숫자를 갱신
  
  pos2 = binary_left(sub2, (rarr[i], n - 1 - i))
  if pos2 == len(sub2):
    sub2.append((rarr[i], n - 1 - i))
  else:
    if sub2[pos2][0] != rarr[i]:
      sub2[pos2] = (rarr[i], n - 1 - i)

  dp1.append(sub1.copy())
  dp2.append(sub2.copy())

max_length = 0
for i in range (len(dp1)):
  for j in range (len(dp2)):
    if dp1[i][-1][1] == dp2[j][-1][1]: # dp1과 dp2의 마지막 인덱스가 동일하다면 왼쪽은 증가하는 수열 오른쪽은 감소하는 수열 (가운데는 겹치므로 하나 제거 필수)
      max_length = max(max_length, len(dp1[i]) + len(dp2[j]) - 1)
    
    elif dp1[i][-1][1] < dp2[j][-1][1]: # 증가하는 수열의 마지막 인덱스가 감소하는 수열의 마지막 인덱스보다 작아야 둘을 합칠 수 있음
      if dp1[i][-1][0] == dp2[j][-1][0]: # dp1과 dp2의 마지막 값이 동일하다면 가운데 하나는 겹치므로 제거 필요
        max_length = max(max_length, len(dp1[i]) + len(dp2[j]) - 1)
      else:
        max_length = max(max_length, len(dp1[i]) + len(dp2[j]))

print(max_length)