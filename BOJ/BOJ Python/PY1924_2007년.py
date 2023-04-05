x, y = map(int, input().split())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]
days = 0

for i in range(x - 1):
    days += day[i]

days = (days + y) % 7

print(week[days])