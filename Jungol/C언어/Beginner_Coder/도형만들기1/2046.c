#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int n, m;
	int a;

	scanf("%d %d", &n, &m);

	if (m == 1)
	{
		for (int i = 1; i <= n; i++)
		{
			for (int j = 0; j < n; j++)
				printf("%2d ", i);
			printf("\n");
		}
	}
	else if (m == 2)
	{
		for (int i = 1; i <= n; i++)
		{
			if (i % 2 == 1)
			{
				for (int j = 1; j <= n; j++)
					printf("%2d ", j);
				printf("\n");
			}
			else
			{
				for (int j = n; j >= 1; j--)
					printf("%2d ", j);
				printf("\n");
			}
		}
	}
	else
	{
		for (int i = 1; i <= n; i++)
		{
			a = i;
			for (int j = 0; j < n; j++)
			{
				printf("%2d ", a);
				a += i;
			}
			printf("\n");
		}
	}
}