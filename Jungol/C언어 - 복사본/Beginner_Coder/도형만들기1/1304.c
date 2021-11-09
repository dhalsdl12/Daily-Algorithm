#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int n;
	int a;

	scanf("%d", &n);

	for (int i = 1; i <= n; i++)
	{
		a = i;
		for (int j = 1; j <= n; j++)
		{
			printf("%d ", a);
			a += n;
		}
		printf("\n");
	}

	return 0;
}