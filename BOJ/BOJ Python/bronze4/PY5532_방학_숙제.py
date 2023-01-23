import math


l = int(input())
a = int(input()) # 국어
b = int(input()) # 수학
c = int(input()) # 국어 맥스
d = int(input()) # 수학 맥스

k = math.ceil(a / c)
m = math.ceil(b / d)

print(l - max(k, m))