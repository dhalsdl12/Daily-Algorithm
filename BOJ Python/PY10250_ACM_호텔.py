num = int(input())
room = []

for i in range(num):
    h, w, n = map(int, input().split())
    floor = 0
    ho = 0
    
    if n%h == 0:
        floor = h*100
        ho = (n//h)
        room.append(floor+ho)
    else:
        floor = (n%h)*100
        ho = (n//h)+1
        room.append(floor+ho)

for i in range(num):
    print(room[i])