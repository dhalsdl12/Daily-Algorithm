#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

typedef struct Rec{
	int width, height;
	int s;
}r;
int main()
{
	r r1;
	r r2;

	scanf("%d %d", &r1.width, &r1.height);
	scanf("%d %d", &r2.width, &r2.height);

	r1.s = r1.width * r1.height;
	r2.s = r2.width * r2.height;

	if (r1.s < r2.s)
		printf("a is smaller\n");
	else
		printf("b is smaller\n");

	return 0;
}