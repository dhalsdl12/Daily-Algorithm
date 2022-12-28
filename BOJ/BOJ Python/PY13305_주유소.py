import sys

num = int(sys.stdin.readline())
distance = []
cost = []
cost_sum = 0

distance = list(map(int,sys.stdin.readline().split()))
cost = list(map(int,sys.stdin.readline().split()))

cost_sum = distance[0]*cost[0]
min_cost = cost[0]

for i in range(1, num-1):
    if min_cost > cost[i]:
        cost_sum += cost[i]*distance[i]
        min_cost = cost[i]
    else:
        cost_sum += min_cost*distance[i]

print(cost_sum)