#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main()

{
	char string[101];
	int cnt = 0;

	gets(string);

	char* ptr = strtok(string, " ");
	cnt++;

	while (ptr != NULL)
	{
		if (cnt % 2 == 1)
			printf("%s\n", ptr);
		ptr = strtok(NULL, " ");
		cnt++;
	}

	return 0;
}