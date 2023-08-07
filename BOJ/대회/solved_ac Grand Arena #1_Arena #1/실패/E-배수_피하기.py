from itertools import combinations

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(2, n + 1):
    for tmp in combinations(arr, i):
        check = 0

        for x in range(len(tmp)):
            for y in range(x + 1, len(tmp)):
                if (tmp[x] + tmp[y]) % k == 0:
                    check = 1
        
        if check == 0:
            answer += 1

print(answer % 1000000007)