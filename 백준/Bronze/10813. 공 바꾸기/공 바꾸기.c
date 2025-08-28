#include <stdio.h>
#include <stdlib.h>
void swap(int *pa, int *pb);
int main(void)
{
	int N;
	scanf("%d", &N);
	int *array = (int *)malloc(N * sizeof(int));
	if (array == NULL) exit(1);

	// index i번 바구니에 i + 1을 넣자
	for (int i = 0; i < N; i++) array[i] = i + 1;

	int M;
	scanf("%d", &M);
	for (int a = 0; a < M; a++)
	{
		int i, j;
		scanf("%d %d", &i, &j);
		// array[i - 1] 과 array[j - 1]의 값을 swap
		swap(&(array[i - 1]), &(array[j - 1]));
	}
	for (int i = 0; i < N; i++) printf("%d ", array[i]);
	printf("\n");
	free(array);
	return 0;
}
void swap(int *pa, int *pb)
{
	int temp;
	temp = *pa;
	*pa = *pb;
	*pb = temp;
}