import sys

N = int(sys.stdin.readline()) # 표의 크기
base = list(map(int, sys.stdin.readline().split()))
base.sort()
arr = base # 비교를 위해 base를 하나 설정

for _ in range (N-1): # 첫번째 리스트를 이미 받았으므로 N-1까지만 받으면 됨
  num = list(map(int, sys.stdin.readline().split()))
  arr.extend(num)
  arr.sort()
  arr = arr[N:]

print(arr[0])