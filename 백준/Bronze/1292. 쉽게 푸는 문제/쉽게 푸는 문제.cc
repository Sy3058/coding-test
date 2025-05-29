#include <stdio.h>

int main() {
    int a, b, sum = 0, idx = 1, num = 1;
    int arr[1001] = {0, };
    scanf("%d %d", &a, &b);

    // fill array
    while (idx < 1000) {
        for (int i = 0; i < num; i++) {
            arr[idx] = num;
            idx += 1;
            if (idx == 1001) {
                break;
            }
        }
        num += 1;
    }

    for (a; a < b + 1; a++) {
        sum += arr[a];
    }
    printf("%d\n", sum);
}