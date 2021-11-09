#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int binary(int* arr, int num, int s, int e);
int main()
{
	int n, q, num;
	int* arr;
	int* result;

	scanf("%d", &n);
	arr = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);
		

	scanf("%d", &q);
	result = (int*)malloc(sizeof(int) * q);

	for (int i = 0; i < q; i++)
	{
		scanf("%d", &num);
		result[i] = binary(arr, num, 0, n - 1);
	}

	for (int i = 0; i < q; i++)
		printf("%d ", result[i]);
	printf("\n");

	return 0;
}
int binary(int* arr, int num, int s, int e)
{
	int mid;
	while (s <= e)
	{
		mid = (s + e) / 2;
		if (arr[mid] == num)
			return mid;
		if (arr[mid] > num)
			e = mid - 1;
		else
			s = mid + 1;
	}
	return -1;
}