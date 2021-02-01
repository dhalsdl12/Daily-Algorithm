import sys
N, C = map(int, input().split())
house = []

for i in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

start = 1
end = house[-1] - house[0]

result = 0

while (start <= end):
    mid = (start + end)//2
    count = 1
    h = house[0]

    for i in range(1, N):
        if mid <= house[i]-h:
            count += 1
            h = house[i]
    if count >= C:
        result = mid
        start = mid+1
    else:
        end = mid-1
print(result)