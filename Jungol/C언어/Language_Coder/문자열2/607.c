#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main()
{
	char c1[21];
	char c2[21];

	scanf("%s %s", c1, c2);

	strncpy(c2, c1, 2);
	strncat(c2, c1, 2);

	printf("%s", c2);

	return 0;
}