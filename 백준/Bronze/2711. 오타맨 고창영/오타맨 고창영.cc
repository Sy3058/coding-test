#include <stdio.h>
#include <string.h>

int main() {
    int t, idx;
    char word[80];
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d %s", &idx, word);
        idx -= 1;
        for (int j = 0; j < strlen(word); j++) {
            if (j != idx) {
                printf("%c", word[j]);
            }
        }
        printf("\n");
    }
}