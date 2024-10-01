import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def merge_sort(arr, left, right):
  # arr에 원소가 하나씩만 남을 때까지 재귀호출
  if left < right:
    mid = (left + right) // 2
    merge_sort(arr, left, mid) # 왼쪽 배열 정렬
    merge_sort(arr, mid + 1, right) # 오른쪽 배열 정렬
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
  global count, result # K번째 배열 체크용

  temp = [] # 새롭게 정렬된 배열
  i, j = left, mid + 1 # 각각 가장 처음에 오게 되는 수

  # 두 부분 배열을 병합하는 과정
  while i <= mid and j <= right: # 각 배열의 끝까지
    if arr[i] <= arr[j]: # 왼쪽 배열보다 오른쪽 배열 값이 클 때
      temp.append(arr[i])
      i += 1
    else:
      temp.append(arr[j])
      j += 1
  
  # 왼쪽 배열이 먼저 다 정렬된 경우
  while i <= mid:
    temp.append(arr[i])
    i += 1
  
  # 오른쪽 배열이 먼저 다 정렬된 경우
  while j <= right:
    temp.append(arr[j])
    j += 1
  
  # 병합 결과를 원래 배열에 반영
  for idx in range (len(temp)):
    arr[left + idx] = temp[idx] # left는 현재 병합중인 배열의 시작 인덱스 (임시 배열의 값을 원래 배열의 위치에 덮어씀)
    count += 1
    if count == k:
      result = arr[left + idx]

count = 0
result = -1 # k번째 원소가 없는 경우 -1 return

merge_sort(arr, 0, n-1) # 0부터 이므로 n-1까지

print(result)