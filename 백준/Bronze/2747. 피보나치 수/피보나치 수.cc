#include <stdio.h>

int main() {
    int n, arr[46];
    arr[0] = 0;
    arr[1] = 1;
    
    scanf("%d", &n);
    for (int i = 2; i < n + 1; i++) {
        arr[i] = arr[i-1] + arr[i-2];
    }
    printf("%d\n", arr[n]);
}