#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int* queue;
int front = -1;
int rear = -1;
int max;

void addq(int value) 
{
	rear = (rear + 1) % (max);
	queue[rear] = value;
}
int deleteq() 
{
	front = (front + 1) % (max);
	return queue[front];
}
int main()
{
	int n, k, a = 0, f;
	int* arr;
	scanf("%d %d", &n, &k);
	max = n + 2;

	queue = malloc(sizeof(*queue) * (max));
	arr = malloc(sizeof(*arr) * (max));

	for (int i = 1; i <= n; i++)
		addq(i);

	while (1)
	{
		f = front;
		for (int i = f + 1; i < f  + k; i++)
		{
			addq(queue[i % max]);
			deleteq();
		}
		arr[a++] = deleteq();
		if (a == n)
			break;
	}
	printf("<");
	for (int i = 0; i < n; i++)
	{
		printf("%d", arr[i]);
		if (i != n - 1)
			printf(", ");
	}
	printf(">\n");
}