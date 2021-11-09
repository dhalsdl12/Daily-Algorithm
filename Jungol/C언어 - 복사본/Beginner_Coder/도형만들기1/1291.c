#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main()
{
	int s, e;

	while (1)
	{
		scanf("%d %d", &s, &e);
		if (s < 2 || s > 9 || e < 2 || e > 9)
		{
			printf("INPUT ERROR!\n");
			continue;
		}
		else
			break;
	}
	if (s <= e)
	{
		for (int j = 1; j <= 9; j++)
		{
			for (int i = s; i <= e; i++)
			{
				printf("%d * %d = %2d   ", i, j, i * j);
			}
			printf("\n");
		}
	}
	else
	{
		for (int j = 1; j <= 9; j++)
		{
			for (int i = s; i >= e; i--)
			{
				printf("%d * %d = %2d   ", i, j, i * j);
			}
			printf("\n");
		}
	}

	return 0;
}