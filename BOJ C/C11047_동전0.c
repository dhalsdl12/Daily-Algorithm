#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n, k;
	int* a;
	int cnt = 0;

	scanf("%d %d", &n, &k);
	
	a = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}

	for (int i = n - 1; i >= 0; i--)
	{
		if (k >= a[i])
		{
			cnt += (k / a[i]);
			k %= a[i];
		}
	}
	printf("%d\n", cnt);

	return 0;
}