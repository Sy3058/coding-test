#include <stdio.h>

int main()
{
  int n, student, apple;
  int rest = 0;
  scanf("%d", &n);
  for (int i = 1; i <= n; i++) {
    scanf("%d%d", &student, &apple);
    rest += apple % student;
  }
  printf("%d\n", rest);
}