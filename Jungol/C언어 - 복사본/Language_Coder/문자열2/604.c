#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>

int cal_len(char* ch);
int main()
{
	char c[10][21];
	char last;
	int len[10];

	for (int i = 0; i < 10; i++)
	{	
		scanf("%s", c[i]);
		len[i] = cal_len(c[i]);
	}
	scanf(" %c", &last);
	for (int i = 0; i < 10; i++)
	{
		if (c[i][len[i] - 1] == last)
		{
			printf("%s\n", c[i]);
		}
	}

	return 0;
}
int cal_len(char* ch)
{
	int cnt = 0;
	while (ch[cnt] != '\0')
	{
		cnt++;
	}
	return cnt;
}