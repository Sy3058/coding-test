#include <stdio.h>

int main() {
    int n;
    int tmp = 0, score = 0;
    scanf("%d", &n);
    int result[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &result[i]);
    }
    for (int j = 0; j < n; j++) {
        if (result[j] == 1) {
            tmp += 1;
            score += tmp;
        } else {
            tmp = 0;
        }
    }
    printf("%d\n", score);
}