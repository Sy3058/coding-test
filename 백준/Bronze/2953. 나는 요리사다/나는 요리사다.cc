#include <stdio.h>

int main() {
    int s1, s2, s3, s4, ts, winner, hs = 0;
    for (int i = 1; i < 6; i++) {
        scanf("%d %d %d %d", &s1, &s2, &s3, &s4);
        ts = s1 + s2 + s3 + s4;
        if (ts > hs) {
            winner = i;
            hs = ts;
        }
    }
    printf("%d %d\n", winner, hs);
}