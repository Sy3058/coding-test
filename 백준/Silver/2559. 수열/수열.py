import sys

N, K = map(int, sys.stdin.readline().split())
temps = list(map(int, sys.stdin.readline().split()))
hap = sum(temps[:K]) # 0부터 K개의 합
mhap = hap

for i in range (0, N-K): # 0일 때는 위에서 이미 구했으므로
  hap = hap - temps[i] + temps[i+K]
  if hap > mhap:
    mhap = hap

print(mhap)