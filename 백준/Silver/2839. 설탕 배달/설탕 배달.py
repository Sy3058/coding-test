import sys
input = sys.stdin.readline

n = int(input())

def sol(n):
    fk = n // 5 # 5kg 봉지
    tk = 0 # 3kg 봉지
    rn = n % 5
    if rn == 0:
        print(fk)
        exit()
    for i in range (fk, -1, -1):
        if rn % 3 == 0:
            print(fk + rn//3)
            exit()
        else:
            fk -= 1
            rn += 5
    
    print(-1)

sol(n)