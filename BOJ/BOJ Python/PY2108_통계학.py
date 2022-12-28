import sys

num = int(sys.stdin.readline())
arr = []

for i in range(num):
    arr.append(int(sys.stdin.readline()))
avg = sum(arr)/num
print(round(avg))

arr = sorted(arr)
mid1 = arr[num//2]
print(mid1)

from collections import Counter
k = Counter(arr).most_common()

if len(arr)>1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else: print(arr[0])

print(arr[-1] - arr[0])