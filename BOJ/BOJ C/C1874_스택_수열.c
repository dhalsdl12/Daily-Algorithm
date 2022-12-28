#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#define SIZE 100000

char result[SIZE * 2];
int stack[SIZE];
int top = -1;

int main()
{
    int n;
    scanf("%d", &n);
    int* arr = (int*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);
 
    int num = 1, idx = 0, result_idx = 0;

    while (result_idx != n * 2)
    {
        if (top == -1 || stack[top] < arr[idx])
        {
            stack[++top] = num++;
            result[result_idx++] = '+';
        }
        else if (stack[top] == arr[idx])
        {
            top--;
            result[result_idx++] = '-';
            idx++;
        }
        else
        {
            printf("NO");
            return 0;
        }
    }
    for (int i = 0; i < result_idx; i++)
        printf("%c\n", result[i]);

    return 0;
}
