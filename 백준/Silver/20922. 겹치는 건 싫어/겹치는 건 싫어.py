from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))
num_list = set(arr)
cnt = {key:0 for key in num_list}
i = 0 # left
j = 0 # right

max_length = 0 # 같은 정수를 K개 이하로 포함하는 부분 수열의 길이
part = deque([])

while j < N:
  part.append(arr[j])
  cnt[arr[j]] += 1

  if cnt[arr[j]] > K:
    if max_length < len(part) - 1: # 하나 더 넣었을 때 같은 정수가 K개보다 커지므로 넣기 전까지의 길이를 재야 함
      max_length = len(part) - 1
    while arr[i] != arr[j]: #  같은 정수 하나를 제거해줘야 뒤에 같은 정수를 추가할 수 있음
      i += 1
      tmp = part.popleft()
      cnt[tmp] -= 1 # pop한 것들의 개수를 줄여줘야함
    # arr[i] == arr[j]가 되면 아래의 함수를 실행하지 않으므로 따로 실행해줘야 함
    i += 1
    tmp = part.popleft()
    cnt[tmp] -= 1
  
  j += 1

if max_length < len(part):
  max_length = len(part)

print(max_length)