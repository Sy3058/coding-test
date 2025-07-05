sa, sb = map(int, input().split())

# 둘 중 하나만 참일 때 참이므로 XOR
print(sa ^ sb)