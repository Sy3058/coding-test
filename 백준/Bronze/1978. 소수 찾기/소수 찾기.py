import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def is_prime(num):
    if num == 1:
        return False
    for i in range (2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

cnt = 0
for num in arr:
    if is_prime(num):
        cnt += 1

print(cnt)