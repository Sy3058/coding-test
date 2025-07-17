import sys
input = sys.stdin.readline

for _ in range (int(input())):
    ox = input().strip()

    tp = 0
    p = 0
    for i in range (len(ox)):
        if ox[i] == 'X':
            p = 0
        else:
            p += 1
            tp += p
    print(tp)