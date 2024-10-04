t = int(input())
calc = {'@': '*3', '%': '+5', '#': '-7'}

for _ in range (t):
  form = input().split()
  ans = form[0]
  for i in range (1, len(form)):
    form[i] = calc[form[i]]
    ans = str(eval(ans+form[i]))
  ans = float(ans)
  print('%.2f'%ans)