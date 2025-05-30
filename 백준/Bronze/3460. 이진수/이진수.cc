#include <stdio.h>

int main() {
    int  t, n;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        int arr[100] = {0, };
        scanf("%d", &n);
        int j = 0;
        while (n > 0) {
            if (n % 2 == 1) {
                printf("%d ", j);
            }
            n /= 2;
            j += 1;
        }
    }
}