import pygame
import sys

# 게임 설정
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 초기화
pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
WINDOW.fill(WHITE)

# 게임 변수
board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]
player_turn = True
game_over = False

# 그리드 그리기
def draw_grid():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(WINDOW, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(WINDOW, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# 마크 그리기
def draw_markers():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                pygame.draw.line(WINDOW, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(WINDOW, BLACK, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), 
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(WINDOW, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, LINE_WIDTH)

# 마우스 클릭 위치 변환
def get_mouse_pos():
    x, y = pygame.mouse.get_pos()
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# 빈 공간 확인
def is_space_empty(row, col):
    return board[row][col] is None

# 보드 업데이트
def update_board(row, col, player_turn):
    if player_turn:
        board[row][col] = "X"
    else:
        board[row][col] = "O"

# 승리 조건 확인
def check_win(player_mark):
    # 가로
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player_mark for col in range(BOARD_COLS)):
            return True
    # 세로
    for col in range(BOARD_COLS):
        if all(board[row][col] == player_mark for row in range(BOARD_ROWS)):
            return True
    # 대각선
    if all(board[i][i] == player_mark for i in range(BOARD_ROWS)) or \
       all(board[i][BOARD_COLS-i-1] == player_mark for i in range(BOARD_ROWS)):
        return True
    return False

# 게임 결과 메시지
def display_gameover_msg(winner):
    font = pygame.font.SysFont(None, 40)
    if winner == "Tie":
        text = font.render("Tie!", True, GREEN)
    else:
        text = font.render(f"{winner} wins!", True, GREEN)
    WINDOW.blit(text, ((WIDTH - text.get_width()) // 2, (HEIGHT - text.get_height()) // 2))

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_row, mouse_col = get_mouse_pos()
                if is_space_empty(mouse_row, mouse_col):
                    update_board(mouse_row, mouse_col, player_turn)
                    if check_win("X"):
                        game_over = True
                    elif check_win("O"):
                        game_over = True
                    elif all(board[i][j] is not None for i in range(BOARD_ROWS) for j in range(BOARD_COLS)):
                        game_over = True
                    player_turn = not player_turn

    WINDOW.fill(WHITE)
    draw_grid()
    draw_markers()

    if game_over:
        display_gameover_msg("Tie" if all(board[i][j] is not None for i in range(BOARD_ROWS) for j in range(BOARD_COLS))
                             else "X" if player_turn else "O")

    pygame.display.update()
