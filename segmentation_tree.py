import sys
input = sys.stdin.readline

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Q : len(arr) * 4로 tree 사이즈를 정해놓는 건가?
# A : 
# 보통배열의 크기(n)보다 큰 가장 가까운 n의 제곱수를 구한 뒤, 2배를 한다.
# 예를 들어 n이 10일 때, n보다 큰 가장 가까운 제곱수는 16이 된다.
# 16의 2배인 32를 보통 tree의 사이즈로 설정한다.
# 이때, 4를 곱하면 보통 그 사이즈만큼 할당할 수 있기 때문에 그냥 편하게 4를 곱하는 것이다.
tree = [0 for _ in range(len(arr) * 4)]


# <세그먼트 트리를 배열의 각 구간 합으로 채워주기>
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스
# index : 세그먼트 트리의 인덱스 (무조건 1부터 시작)
def init(start, end, index):
    # 가장 끝에 도달했으면 arr 삽입
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채워준다.
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

# <특정 원소의 값을 수정하는 함수>
# start : 시작 인덱스, end : 마지막 인덱스
# what : 구간 합을 수정하고자 하는 노드
# value : 수정할 값
def update(start, end, index, what, value):
    # 범위 밖에 있는 경우
    if what < start or what > end:
        return
    # 범위 안에 있으면 내려가면서 다른 원소도 갱신
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)
    

# <구간 합을 구하는 함수>
# start : 시작 인덱스, end : 마지막 인덱스
# index : 세그먼트 트리의 인덱스 (무조건 1부터 시작)
# left, right : 구간 합을 구하고자 하는 범위
def interval_sum(start, end, index, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return tree[index]
    # 그렇지 않다면 두 부분으로 나누어 합을 구하기
    mid = (start + end) // 2
    # start와 end가 변하면서 구간 합인 부분을 더해준다고 생각하면 된다.
    return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)

init(0, len(arr) - 1, 1)
print(interval_sum(0, 9, 1, 6, 9))