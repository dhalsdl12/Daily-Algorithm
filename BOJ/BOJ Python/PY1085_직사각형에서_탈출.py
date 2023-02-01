x, y, w, h = map(int, input().split())

move_x = min(w-x, x)
move_y = min(h-y, y)

print(min(move_x, move_y))