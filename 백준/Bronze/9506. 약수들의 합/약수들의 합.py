def division(n):
  result = [1]
  for i in range (2, int(n**0.5)+1):
    if n % i == 0:
      result.append(i)
      if n // i != i:
        result.append(n//i)
  result.sort()
  return result

n = int(input())

while n != -1:
  result = division(n)
  if sum(result) == n:
    print('%d ='%(n), ' + '.join(map(str,result)))
  else:
    print('%d is NOT perfect.'%(n))
  n = int(input())