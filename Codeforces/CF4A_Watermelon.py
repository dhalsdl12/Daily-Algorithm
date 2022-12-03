def gcds(n,m):
    if m>n :
        m,n = n,m
    while m != 0 :
        n = n%m
        n,m = m,n
    return n


a, b = map(int, input().split())
print(gcds(a, b))