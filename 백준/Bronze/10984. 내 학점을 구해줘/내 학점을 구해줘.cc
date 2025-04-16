#include <stdio.h>

int main()
{
  int t, n, c;
  float g;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    scanf("%d", &n);
    int tc = 0;
    float tg = 0;
    for (int j = 1; j <= n; j++) {
      scanf("%d%f", &c, &g);
      tc += c;
      tg += g * c;
    }
    printf("%d %.1f\n", tc, tg/tc);
  }
}