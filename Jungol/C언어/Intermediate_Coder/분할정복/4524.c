#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b)  
{
	int num1 = *(int*)a; 
	int num2 = *(int*)b; 

	if (num1 < num2)  
		return -1;   

	if (num1 > num2)   
		return 1;      

	return 0;   
}
int main()
{
	int n;
	int* arr;

	scanf("%d", &n);
	
	arr = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
		scanf("%d", &arr[i]);

	qsort(arr, n, sizeof(int), compare);

	for (int i = n - 1; i >= 0; i--)
		printf("%d ", arr[i]);
	printf("\n");

	return 0;
}