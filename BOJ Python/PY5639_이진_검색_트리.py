def postorder(start, end):
    if start > end:
        return

    division = end + 1  # 나눌위치
    for i in range(start + 1, end + 1):
        if post[start] < post[i]:
            division = i
            break

    postorder(start + 1, division - 1)  # 분할 왼쪽
    postorder(division, end)  # 분할 오른쪽
    print(post[start])


post = []
count = 0
while count <= 10000:
    try:
        num = int(input())
    except:
        break
    post.append(num)
    count += 1

postorder(0, len(post) - 1)