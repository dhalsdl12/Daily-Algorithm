answer = 0
max_ans = 0

for i in range(10):
    a, b = map(int, input().split())

    answer -= a
    answer += b
    max_ans = max(max_ans, answer)

print(max_ans)