import pygame
import random

# 게임 창 크기
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 게임 보드 크기
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# 블록 크기
BLOCK_SIZE = 30

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)

# 테트리스 블록 모양
SHAPES = [
    [[1, 1, 1, 1]],  # I 모양
    [[1, 1], [1, 1]],  # O 모양
    [[1, 1, 1], [0, 1, 0]],  # T 모양
    [[1, 1, 0], [0, 1, 1]],  # Z 모양
    [[0, 1, 1], [1, 1, 0]],  # S 모양
    [[1, 1, 1], [0, 0, 1]],  # J 모양
    [[1, 1, 1], [1, 0, 0]]  # L 모양
]

# 블록 색깔
COLORS = [
    BLACK,
    RED,
    GREEN,
    BLUE,
    YELLOW,
    CYAN,
    MAGENTA,
    ORANGE
]


# 새로운 블록 생성
def create_new_block():
    shape = random.choice(SHAPES)
    color = random.randint(1, len(COLORS) - 1)
    x = int(BOARD_WIDTH / 2 - len(shape[0]) / 2)
    y = 0
    block = {'shape': shape, 'color': color, 'x': x, 'y': y}
    return block


# 게임 보드 초기화
def create_board():
    board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    return board


# 블록을 보드에 추가
def add_block_to_board(board, block):
    for row in range(len(block['shape'])):
        for col in range(len(block['shape'][row])):
            if block['shape'][row][col]:
                board[block['y'] + row][block['x'] + col] = block['color']


# 보드와 블록을 그리기
def draw_board(screen, board):
    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH):
            color = COLORS[board[row][col]]
            pygame.draw.rect(screen, color, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, WHITE, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


# 블록 그리기
def draw_block(screen, block):
    for row in range(len(block['shape'])):
        for col in range(len(block['shape'][row])):
            if block['shape'][row][col]:
                color = COLORS[block['color']]
                pygame.draw.rect(screen, color, ((block['x'] + col) * BLOCK_SIZE, (block['y'] + row) * BLOCK_SIZE,
                                                 BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, WHITE, ((block['x'] + col) * BLOCK_SIZE, (block['y'] + row) * BLOCK_SIZE,
                                                 BLOCK_SIZE, BLOCK_SIZE), 1)


# 블록 이동
def move_block(board, block, dx, dy):
    if is_valid_move(board, block, dx, dy):
        block['x'] += dx
        block['y'] += dy
        return True
    return False


# 블록 회전
def rotate_block(board, block):
    rotated_shape = list(zip(*reversed(block['shape'])))
    if is_valid_move(board, block, 0, 0, shape=rotated_shape):
        block['shape'] = rotated_shape


# 이동 또는 회전이 유효한지 확인
def is_valid_move(board, block, dx, dy, shape=None):
    shape = shape or block['shape']
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                new_x = block['x'] + col + dx
                new_y = block['y'] + row + dy
                if not (0 <= new_x < BOARD_WIDTH and 0 <= new_y < BOARD_HEIGHT) or \
                        board[new_y][new_x]:
                    return False
    return True


# 행이 꽉 찼는지 확인하고 제거
def remove_full_rows(board):
    full_rows = []
    for row in range(BOARD_HEIGHT):
        if all(board[row]):
            full_rows.append(row)
    for row in full_rows:
        del board[row]
        board.insert(0, [0] * BOARD_WIDTH)
    return len(full_rows)


# 게임 실행
def play_game():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Tetris')

    clock = pygame.time.Clock()
    FPS = 1

    board = create_board()
    block = create_new_block()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_block(board, block, -1, 0)
                elif event.key == pygame.K_RIGHT:
                    move_block(board, block, 1, 0)
                elif event.key == pygame.K_DOWN:
                    if not move_block(board, block, 0, 1):
                        add_block_to_board(board, block)
                        score += remove_full_rows(board)
                        block = create_new_block()
                elif event.key == pygame.K_UP:
                    rotate_block(board, block)

        screen.fill(WHITE)
        draw_board(screen, board)
        draw_block(screen, block)
        pygame.display.update()

        if not move_block(board, block, 0, 1):
            add_block_to_board(board, block)
            score += remove_full_rows(board)
            block = create_new_block()

        if is_game_over(board):
            pygame.quit()
            print('Game Over! Your score:', score)
            return

        clock.tick(FPS)


# 게임 종료 확인
def is_game_over(board):
    return any(board[0])


# 게임 시작
play_game()