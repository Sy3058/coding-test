import math

l, a, b, c, d = (int(input()) for _ in range (5))
need = max(math.ceil(a/c), math.ceil(b/d))
print(l - need)