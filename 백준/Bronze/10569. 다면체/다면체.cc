#include <stdio.h>

int main()
{
  int t, v, e, s;
  scanf("%d", &t);

  for (int i = 0; i < t; i++)
  {
    scanf("%d %d", &v, &e);
    s = 2 - v + e;
    printf("%d\n", s);
  }
}