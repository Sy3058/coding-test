#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    
    for (int i = 1; i < n + 1; i++) {
        if (i % 2 == 1) {
            for (int j = 0; j < n; j++) {
                printf("%s*", j == 0 ? "":" ");
            }
        } else {
            for (int j = 0; j < n; j++) {
                printf("%s*", " ");
            }
        }
        printf("\n");
    }
}