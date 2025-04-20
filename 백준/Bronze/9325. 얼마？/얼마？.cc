#include <stdio.h>

int main()
{
  int t, s, n, q, p;
  scanf("%d", &t);
  for (int i = 0; i < t; i++) {
    scanf("%d", &s); // 자동차 가격
    scanf("%d", &n); // 서로 다른 옵션의 개수
    for (int j = 0; j < n; j ++) {
      scanf("%d%d", &q, &p); // 특정 옵션의 개수, 해당 옵션의 가격
      s += q * p;
    }
    printf("%d\n", s);
  }
}