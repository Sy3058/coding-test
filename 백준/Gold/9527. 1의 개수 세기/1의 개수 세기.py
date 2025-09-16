a, b = map(int, input().split())

def count_all_ones(n):
  # 1부터 n까지의 정수들을 비트로 나타냈을 때 1의 개수를 모두 더한 값

  if n <= 0: return 0

  n += 1 # 0부터 n까지의 개수를 세기 위해 n + 1
  ans = 0

  # 2의 0승부터 n의 2진수 자릿수까지 반복
  # 10**16을 이진수로 나타내면 54번째 자리에서 끝남
  for k in range (55):
    # 2 ^ (k+1)을 기준으로 완전한 블록의 개수 계산
    # 각 블록마다 2^k개의 1이 k번째 자리에 존재
    full_blocks = n // (2**(k + 1))
    ans += full_blocks * (2 ** k)

    # 완전한 블록을 제외한 나머지 부분에서 1의 개수 계산
    rem = n % (2 ** (k+1))
    
    # 나머지 부분에서 k번째 자리의 1의 개수 더하기
    ans += max(0, rem - (2 ** k))
  
  return ans

# 누적합의 원리
print(count_all_ones(b) - count_all_ones(a-1))