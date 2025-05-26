#include <stdio.h>

int main() {
    int on, off, total, mt;
    total = 0;
    mt = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d %d", &off, &on);
        total += on;
        total -= off;
        if (total > mt) {
            mt = total;
        }
    }
    printf("%d\n", mt);
    return 0;
}