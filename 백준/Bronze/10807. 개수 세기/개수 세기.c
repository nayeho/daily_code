#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);
    int array[N];
    for(int i = 0; i < N; i++)
    {
        scanf("%d", &array[i]);
    }
    
    int v;
    int count = 0;
    scanf("%d", &v);
    for(int i = 0; i < N; i++)
    {
        if(v == array[i])
        {
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}