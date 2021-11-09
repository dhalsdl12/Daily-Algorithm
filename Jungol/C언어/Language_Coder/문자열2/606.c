#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main()
{
	char c[21];

	gets(c);
	strcat(c, "fighting");
	printf("%s", c);

	return 0;
}