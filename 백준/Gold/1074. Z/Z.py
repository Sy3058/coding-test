import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

"""
보드 크기: 2**N * 2**N
1사분면: r: 0 ~ 2**(N-1) - 1, c: 0 ~ 2**(N-1) - 1
2사분면: r: 0 ~ 2**(N-1) - 1, c: 2**(N-1) ~ 2**N
3사분면: r: 2**(N-1) ~ 2**N, c: 0 ~ 2**(N-1) - 1
4사분면: r: 2**(N-1) ~ 2**N, c: 2**(N-1) ~ 2**N
"""
def search(n, r, c):
    global cnt
    if n == 0:
        cnt += 1
        return
    
    # 왼쪽 위
    if 0 <= r < 2 ** (n-1) and 0 <= c < 2 ** (n-1):
        search(n-1, r, c)
    
    # 오른쪽 위
    elif 0 <= r < 2 ** (n-1) and 2 ** (n-1) <= c < 2 ** n:
        cnt += 2 ** (n - 1 + n - 1)
        search(n-1, r, c - 2 ** (n-1)) # 4등분 후 2**(n-1) 기준 위치

    # 왼쪽 아래
    elif 2 ** (n-1) <= r < 2 ** n and 0 <= c < 2 ** (n-1):
        cnt += 2 * (2 ** (n - 1 + n - 1))
        search(n-1, r - 2 ** (n-1), c)

    # 오른쪽 아래
    else:
        cnt += 3 * (2 ** (n - 1 + n - 1))
        search(n-1, r - 2 ** (n-1), c - 2 ** (n-1))

cnt = -1 # 첫번째가 0번이므로
search(n, r, c)
print(cnt)