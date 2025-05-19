#include <stdio.h>

int main()
{
    int n;
    int hap = 0;
    scanf("%d", &n);
    for (int i = 0; i < n + 1; i++)
    {
        for (int j = i; j < n + 1; j++)
        {
            hap += (i + j);
        }
    }
    printf("%d\n", hap);
}