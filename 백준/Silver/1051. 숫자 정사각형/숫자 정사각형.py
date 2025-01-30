import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range (n)]

def check_square(size):
  for i in range (n-size+1):
    for j in range (m-size+1):
      if (arr[i][j] == arr[i][j+size-1] == arr[i+size-1][j] == arr[i+size-1][j+size-1]): # 네 꼭짓점에 쓰여 있는 수가 같다면 True 반환
        return True
  return False

ans = 1
max_size = min(n, m)
for i in range (1, max_size+1):
  if check_square(i): # 네 꼭짓점에 쓰여 있는 수가 같다면 크기 갱신
    ans = i

print(ans**2)