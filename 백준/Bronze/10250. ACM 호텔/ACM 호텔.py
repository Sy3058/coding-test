import sys
input = sys.stdin.readline

for _ in range (int(input())):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print('%d%s'%(h, str(n//h).zfill(2)))
    
    else:
        print('%d%s'%(n%h, str(n//h+1).zfill(2)))