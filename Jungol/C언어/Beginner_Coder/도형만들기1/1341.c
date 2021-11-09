#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int s, e;

	scanf("%d %d", &s, &e);

	if (s <= e)
	{
		for (int i = s; i <= e; i++)
		{
			for (int j = 1; j <= 9; j++)
			{
				printf("%d * %d = %2d   ", i, j, i * j);
				if (j % 3 == 0)
					printf("\n");
			}
			printf("\n");
		}
	}
	else
	{
		for (int i = s; i >= e; i--)
		{
			for (int j = 1; j <= 9; j++)
			{
				printf("%d * %d = %2d   ", i, j, i * j);
				if (j % 3 == 0)
					printf("\n");
			}
			printf("\n");
		}
	}

	return 0;
}