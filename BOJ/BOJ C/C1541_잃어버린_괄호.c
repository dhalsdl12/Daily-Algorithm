#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char math[51];
	char num[6];
	int i = 0, j = 0, result = 0;
	int pm = 0;

	scanf("%s", math);

	while (math[i] != NULL)
	{
		if (math[i] == '+' || math[i] == '-')
		{
			if (pm == 0)
				result += atoi(num);
			else if (pm == 1)
				result -= atoi(num);
			memset(num, NULL, 6);
			j = 0;
			if (math[i] == '-') 
				pm = 1;
		}
		else
		{
			num[j] = math[i];
			j++;
		}
		i++;
	}
	if (pm == 0)
		result += atoi(num);
	else if (pm == 1)
		result -= atoi(num);

	printf("%d\n", result);

	return 0;
}