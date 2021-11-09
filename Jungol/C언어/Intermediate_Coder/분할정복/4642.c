#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct student{
	char name[20];
	int score;
}std;

int n;

void quick_sort(std* arr, int low, int high);
int main()
{
	std* s;

	scanf("%d", &n);

	s = (std*)malloc(sizeof(std) * (n + 1));
	for (int i = 1; i <= n; i++)
		scanf("%s %d", &s[i].name, &s[i].score);

	quick_sort(s, 1, n);

	for (int i = 1; i <= n; i++)
		printf("%s %d\n", s[i].name, s[i].score);
	printf("\n");

	return 0;
}
void quick_sort(std* arr, int low, int high)
{
	int i, pivot;
	int tmp;
	char tmp2[20];
	char pivot2[20];

	if (low < high)
	{
		i = low - 1;
		pivot = arr[high].score;
		strcpy(pivot2, arr[high].name);

		for (int j = low; j < high; j++)
		{
			if (arr[j].score > pivot)
			{
				tmp = arr[++i].score;
				arr[i].score = arr[j].score;
				arr[j].score = tmp;

				strcpy(tmp2, arr[i].name);
				strcpy(arr[i].name, arr[j].name);
				strcpy(arr[j].name, tmp2);
			}
			else if (arr[j].score == pivot)
			{
				if (strcmp(arr[j].name, pivot2) == -1)
				{
					tmp = arr[++i].score;
					arr[i].score = arr[j].score;
					arr[j].score = tmp;

					strcpy(tmp2, arr[i].name);
					strcpy(arr[i].name, arr[j].name);
					strcpy(arr[j].name, tmp2);
				}
			}
		}
		tmp = arr[++i].score;
		arr[i].score = arr[high].score;
		arr[high].score = tmp;

		strcpy(tmp2, arr[i].name);
		strcpy(arr[i].name, arr[high].name);
		strcpy(arr[high].name, tmp2);

		quick_sort(arr, low, i - 1);
		quick_sort(arr, i + 1, high);
	}
}