n = int(input())
ans = -1

def palindrome(n):
  strn = str(n)
  for i in range (len(strn)//2):
    if strn[i] != strn[-1-i]: # 같지 않다면 팰린드롬이 아님
      return False
  return True # 위에서 걸러지지 않았다면 팰린드롬

def prime(n):
  if n < 2:
    return False
  for i in range (2, int(n**0.5)+1):
    if n % i == 0: # i로 나누어 떨어지면 소수가 아님
      return False
  return True # 위에서 걸러지지 않았다면 소수

while ans == -1:
  if palindrome(n): # true면 진행되고 false면 진행되지 않음
    if prime(n):
      ans = n
  n += 1

print(ans)