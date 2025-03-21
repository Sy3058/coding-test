import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def sol():
  if len(arr) == len(set(arr)): # non duplicated list
    return (n*(n+1))//2

  l = 0
  r = 1
  part = set([arr[0]]) # use set to reduce time complexity
  cnt = 1

  while r < n:
    if arr[r] in part:
      while arr[r] in part: # remove arr[l] until arr[r] is removed
        part.remove(arr[l])
        l += 1

    part.add(arr[r])
    cnt += len(part)
    r += 1
  
  return cnt

ans = sol()
print(ans)