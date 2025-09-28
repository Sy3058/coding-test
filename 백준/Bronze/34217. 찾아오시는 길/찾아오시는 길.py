a, b = map(int, input().split()) # 출발지 -> 한양대역 / 용답역
c, d = map(int, input().split()) # 한양대역 / 용답역 -> 목적지

if a + c < b + d: print("Hanyang Univ.")
elif a + c > b + d: print("Yongdap")
else: print("Either")