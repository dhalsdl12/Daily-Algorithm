#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

void mergesort(int arr[], int f, int l);
void merge(int arr[], int f, int m, int l);
int main()
{
	int num;
	int arr[1000000];
	scanf("%d", &num);
	for (int i = 0; i < num; i++)
	{
		scanf("%d", &arr[i]);
	}
	mergesort(arr, 0, num-1);

	for (int i = 0; i < num; i++)
	{
		printf("%d\n", arr[i]);
	}
}
void mergesort(int arr[], int f, int l)
{
	int mid;
	if (f < l)
	{
		mid = (f + l) / 2;
		mergesort(arr, f, mid);
		mergesort(arr, mid+1, l);
		merge(arr, f, mid, l);
	}
}
void merge(int arr[], int f, int m, int l)
{
	int b[1000000];
	int i = f;
	int j = m + 1;
	int k = 0;

	while(i <= m && j <= l)
	{ 
		if (arr[i] <= arr[j])
		{
			b[k++] = arr[i++];
		}
		else
		{
			b[k++] = arr[j++];
		}
	}
	while (i <= m)
	{
		b[k++] = arr[i++];
	}
	while (j <= l)
	{
		b[k++] = arr[j++];
	}
	k--;
	while (k >= 0)  
	{
		arr[f + k] = b[k];
		k--;
	}
}