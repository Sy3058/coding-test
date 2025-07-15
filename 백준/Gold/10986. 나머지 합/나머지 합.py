import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr[0] %= m
rd = {i:0 for i in range (m)}
rd[arr[0]] += 1
sam = arr.copy()

for i in range (1, n):
    sam[i] = (sam [i] + sam[i - 1]) % m # 누적합 % m
    rd[sam[i]] += 1

# sam[i] - sam[j] == 0 이어야 구간의 합 % m이 0이므로 나머지가 같아야 함
# 나머지가 같은 것들 중에서 2개를 순서없이 뽑아내는 경우의 수와 같음
rl = list(rd.values())
ans = rl[0] # 하나만 있어도 m의 배수
for v in rl:
    if v > 1:
        ans += (v * (v-1)) // 2 # xC2

print(ans)