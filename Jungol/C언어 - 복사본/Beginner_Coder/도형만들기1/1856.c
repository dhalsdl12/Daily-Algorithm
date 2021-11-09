#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int n, m;
	int cnt = 0;
	int mul;

	scanf("%d %d", &n, &m);
	mul = m * n;

	for (int i = 0; i < n; i++)
	{
		if (i % 2 == 0)
		{
			for (int j = 1; j <= m; j++)
			{
				printf("%d ", i * m + j);
			}
			printf("\n");
		}
		else
		{
			for (int j = m; j >= 1; j--)
			{
				printf("%d ", i * m + j);
			}
			printf("\n");
		}
	}

	return 0;
}