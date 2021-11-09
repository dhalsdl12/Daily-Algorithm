#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int n;

void quick_sort(int* arr, int low, int high);
int main()
{
	int* arr;

	scanf("%d", &n);

	arr = (int*)malloc(sizeof(int) * (n + 1));
	for (int i = 1; i <= n; i++)
		scanf("%d", &arr[i]);

	quick_sort(arr, 1, n);

	return 0;
}
void quick_sort(int* arr, int low, int high)
{
	int i, pivot;
	int tmp;

	if (low < high)
	{
		i = low - 1;
		pivot = arr[high];

		for (int j = low; j < high; j++)
		{
			if (arr[j] < pivot)
			{
				tmp = arr[++i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
		tmp = arr[++i];
		arr[i] = arr[high];
		arr[high] = tmp;

		for (int k = 1; k <= n; k++)
			printf("%d ", arr[k]);
		printf("\n");

		quick_sort(arr, low, i - 1);
		quick_sort(arr, i + 1, high);
	}
}