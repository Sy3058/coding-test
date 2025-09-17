import sys
input = sys.stdin.readline

n = int(input())

# 큰 수들이 가운데에 몰리면 점수가 가장 높아짐
ans = [i for i in range (1, n+1, 2)] + [i for i in range (2, n+1, 2)][::-1]
print(*ans)