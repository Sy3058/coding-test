#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int mode, mode_cnt = 0, hap = 0;
    int arr[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
        hap += arr[i];
    }
    qsort(arr, 10, sizeof(arr[0]), compare);
    int tmp = 1; // 최빈값을 세기위한 개수
    int base = arr[0]; // 기준
    for (int j = 1; j < 10; j++) {
        if (arr[j] != base || j == 9) {
            // 현재 최빈값의 개수보다 tmp가 더 많으면 tmp에 해당하는 값을 최빈값으로 갱신
            if (tmp > mode_cnt) {
                mode = arr[j-1];
                mode_cnt = tmp;
            }
            base = arr[j];
            tmp = 0;
        } else {
            tmp += 1;
        }
    }
    printf("%d\n", hap/10); // mean
    printf("%d\n", mode); // mode
}