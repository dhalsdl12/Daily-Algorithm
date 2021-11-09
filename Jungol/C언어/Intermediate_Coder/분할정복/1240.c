#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

unsigned long long binary(unsigned long long num, 
	unsigned long long s, unsigned long long e);
int main()
{
	unsigned long long n;
	unsigned long long result = 0;


	scanf("%llu", &n);

	result = binary(n, 1, n);
	printf("%llu\n", result);

	return 0;
}
unsigned long long binary(unsigned long long num, 
	unsigned long long s, unsigned long long e)
{
	unsigned long long mid;
	unsigned long long ans;
	while (s <= e)
	{
		mid = (s + e) / 2;
		if (mid <= num / mid)
		{
			ans = mid;
			s = mid + 1;
		}
		else
			e = mid - 1;
	}
	return ans;
}