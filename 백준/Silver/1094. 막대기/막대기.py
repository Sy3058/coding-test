import sys
input = sys.stdin.readline

x = int(input())
rod = [0, 0, 0, 0, 0, 0, 0]
rod[0] = x//64
x %= 64
rod[1] = x//32
x %= 32
rod[2] = x//16
x %= 16
rod[3] = x//8
x %= 8
rod[4] = x//4
x %= 4
rod[5] = x//2
x %= 2
rod[6] = x//1

print(rod.count(1))