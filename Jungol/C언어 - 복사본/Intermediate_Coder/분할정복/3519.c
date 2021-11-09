#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int n;

void mergesort(int* arr1, int* arr2, int low, int high);
int main()
{
	int* arr1;
	int* arr2;

	scanf("%d", &n);

	arr1 = (int*)malloc(sizeof(int) * (n + 1));
	arr2 = (int*)malloc(sizeof(int) * (n + 1));

	for (int i = 1; i <= n; i++)
		scanf("%d", &arr1[i]);

	mergesort(arr1, arr2, 1, n);

	return 0;
}
void mergesort(int* arr1, int* arr2, int low, int high)
{
	if (low >= high)
		return;

	int mid = (low + high) / 2;

	mergesort(arr1, arr2, low, mid);
	mergesort(arr1, arr2, mid + 1, high);

	int i = low;
	int j = mid + 1;

	for (int k = low; k <= high; k++)
	{
		if (j > high)
			arr2[k] = arr1[i++];
		else if (i > mid)
			arr2[k] = arr1[j++];
		else if (arr1[i] <= arr1[j])
			arr2[k] = arr1[i++];
		else
			arr2[k] = arr1[j++];
	}

	for (int i = low; i <= high; i++)
		arr1[i] = arr2[i];

	for (int i = 1; i <= n; i++)
		printf("%d ", arr1[i]);
	printf("\n");
}