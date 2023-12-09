# 입력 받기
N = int(input())
queries = []

for _ in range(N):
    query = list(map(int, input().split()))
    queries.append(query)

# 초기화
timber_lengths = []  # 통나무 길이를 저장할 배열
result = 0

# 쿼리 처리
for query in queries:
    if query[0] == 1:  # 호반우가 통나무를 세울 때
        timber_lengths.append(query[1])  # 통나무 길이 추가
    elif query[0] == 2:  # 마물이 마법을 사용할 때
        magic_power = query[1]
        for i in range(len(timber_lengths) - 1, -1, -1):
            # 마법 사용 후 통나무 길이 갱신
            timber_lengths[i] = max(timber_lengths[i] - magic_power, 0)
            if timber_lengths[i] == 0:
                # 길이가 0인 통나무 제거
                timber_lengths.pop(i)
    result += sum(timber_lengths)  # 현재까지의 통나무 길이 합

print(result)
