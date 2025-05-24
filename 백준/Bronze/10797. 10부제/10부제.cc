#include <stdio.h>

int main() {
    int num, car[5];
    int cnt = 0;
    scanf("%d", &num);
    for (int i = 0; i < 5; i++) {
        scanf("%d", &car[i]);
        if (car[i] == num) {
            cnt += 1;
        }
    }
    printf("%d\n", cnt);
}