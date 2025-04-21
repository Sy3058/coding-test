#include <stdio.h>

int main()
{
  int n, plug, socket = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &plug); // 멀티탭에 꽂을 수 있는 플러그의 개수
    socket += plug;
  }
  socket = socket - n + 1; // 멀티탭을 연결하는데 필요한 플러그의 개수를 제외해야 함
  printf("%d\n", socket);
}