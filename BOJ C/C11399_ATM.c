#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int start, end;
}element;

int compare(const void* a, const void* b)
{
	const element* n1, * n2;
	n1 = (const element*)a;
	n2 = (const element*)b;

	if (n1->end != n2->end)
	{
		if (n1->end < n2->end)
			return -1;
		if (n1->end > n2->end)
			return 1;
		return 0;
	}
	else
	{
		if (n1->start < n2->start)
			return -1;
		if (n1->start > n2->start)
			return 1;
		return 0;
	}
}
int main()
{
	int n, time = 0;
	element* arr;

	scanf("%d", &n);
	arr = (element*)malloc(sizeof(element) * n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i].end);
		arr[i].start = i;
	}

	qsort(arr, n, sizeof(element), compare);

	time = arr[0].end;
	for (int i = 1; i < n; i++)
	{
		arr[i].end += arr[i - 1].end;
		time += arr[i].end;
	}
	printf("%d\n", time);

	return 0;
}