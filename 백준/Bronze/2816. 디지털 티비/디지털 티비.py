n = int(input()) # 채널의 수
channels = []
remote = '' # 눌러야하는 리모컨 번호

for _ in range (n):
  c = input() # 채널
  channels.append(c)

k1 = channels.index('KBS1')
k2 = channels.index('KBS2')

# KBS1을 인덱스 0으로 이동
remote += '1' * k1 # KBS1까지 이동
remote += '4' * k1 # KBS1을 맨 앞으로 이동

if k1 > k2: # KBS1이 KBS2보다 밑에 있었다면 KBS2의 인덱스가 하나 밀림
  k2 += 1

# KBS2를 인덱스 1로 이동
remote += '1' * k2 # KBS2까지 이동
remote += '4' * (k2 - 1) # KBS2를 인덱스 1로 이동

print(remote)