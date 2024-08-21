import sys
N = int(sys.stdin.readline())
Ncard = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mcard = list(map(int, sys.stdin.readline().split()))
arr = ["0"] * M
Ncard = set(Ncard)

for i in range (M):
    if Mcard[i] in Ncard:
        arr[i] = "1"

answer = " ".join(arr)
print(answer)