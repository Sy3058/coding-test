for tc in range (1, int(input()) + 1):
  n, k = map(int, input().split()) # 숫자의 개수, 크기 순서
  
  # n은 4의 배수 (각 면에 n//4개씩)
  num = list(input().strip())
  for i in range (n//4 - 1):
    num += num[i]
  
  pos_num = set()

  for i in range (n):
    hexa = num[i:i+n//4]
    changed_hexa = int('0x'+''.join(hexa), 16)
    pos_num.add(changed_hexa)
  
  pos_num = sorted(list(pos_num), reverse = True)
  print(f"#{tc} {pos_num[k-1]}")