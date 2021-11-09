#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int main()
{
	char word[5][31];
	char string[31];

	for (int i = 0; i < 5; i++)
	{
		gets(string);
		strcpy(word[i], string);
	}
	for (int i = 4; i >= 0; i--)
	{
		printf("%s\n", word[i]);
	}
}