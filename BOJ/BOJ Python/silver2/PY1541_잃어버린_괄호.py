import sys

exp = sys.stdin.readline().split('-')
ssum = []

for ex in exp:
	temp = list(map(int, ex.split('+')))
	ssum.append(sum(temp))

total_sum = ssum[0]

for i in ssum[1:]:
	total_sum -= i

print(total_sum)