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
	int n, last = 0, cnt = 0;
	element* arr;

	scanf("%d", &n);
	arr = (element*)malloc(sizeof(element) * n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %d", &arr[i].start, &arr[i].end);
	}

	qsort(arr, n, sizeof(element), compare);

	for (int i = 0; i < n; i++)
	{
		if (arr[i].start >= last)
		{
			cnt++;
			last = arr[i].end;
		}
	}
	printf("%d\n", cnt);

	return 0;
}