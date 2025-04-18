#include <stdio.h>

long long fibo(int n)
{
  long long arr[91];
  arr[0] = 0; arr[1] = 1; arr[2] = 1;
  for (int i = 3; i <= n; i++) {
    arr[i] = arr[i-1] + arr[i-2];
  }
  return arr[n];
}

int main()
{
  int n;
  scanf("%d", &n);
  long long ans = fibo(n);
  printf("%lld\n", ans);
}