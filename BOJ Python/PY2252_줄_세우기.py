def topological(numCourses, prerequisites):
    pre = [[]for _ in range(numCourses)]
    num = [0 for _ in range(numCourses)]

    queue = []
    answer = []

    for a, b in prerequisites:
        pre[b].append(a)
        num[a] += 1

    for i in range(numCourses):
        if num[i] == 0:
            queue.append(i)
    while queue:
        course = queue.pop()
        answer.append(course)
        for crs in pre[course]:
            num[crs] -= 1
            if num[crs] == 0:
                queue.append(crs)
    if len(answer) == numCourses:
        return answer
    return -1


n, m = map(int, input().split())
c = []
for i in range(m):
    a, b = map(int, input().split())
    c.append([b-1, a-1])

result = topological(n, c)
for re in result:
    print(re + 1, end=' ')