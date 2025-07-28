#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N, X;
    scanf("%d %d", &N, &X);
    int *array = malloc(N * sizeof(int));
    int *pa = array;
    for(int i = 0; i < N; i++) scanf("%d", pa++);
    pa = array;
    for(int i = 0; i < N; i++)
    {
        if(*pa < X) printf("%d ", *pa);
        pa++;
    }
    free(array);
    return 0;
}