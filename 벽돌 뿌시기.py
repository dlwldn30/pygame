import pygame
import random

# 게임 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색깔 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def move(self, pixels):
        self.rect.x += pixels

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.width:
            self.rect.x = SCREEN_WIDTH - self.rect.width

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), -1]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - self.rect.width:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

# 벽돌 클래스
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

# 게임 초기화
pygame.init()

# 화면 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("벽돌 깨기 게임")

# 게임 속도 설정
clock = pygame.time.Clock()

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
bricks = pygame.sprite.Group()

# 패들 생성
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

all_sprites.add(paddle)

# 공 생성
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites.add(ball)

# 벽돌 생성
for row in range(5):
    for column in range(8):
        brick = Brick(RED, 80, 30)
        brick.rect.x = column * (brick.rect.width + 10)
        brick.rect.y = row * (brick.rect.height + 10)
        bricks.add(brick)
        all_sprites.add(brick)

# 게임 루프
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move(-5)
    if keys[pygame.K_RIGHT]:
        paddle.move(5)

    # 공과 패들 충돌 감지
    if pygame.sprite.collide_mask(ball, paddle):
        ball.velocity[1] = -ball.velocity[1]

    # 공과 벽돌 충돌 감지
    brick_collisions = pygame.sprite.spritecollide(ball, bricks, True)
    if brick_collisions:
        ball.velocity[1] = -ball.velocity[1]

    # 공 업데이트
    ball.update()

    # 화면 업데이트
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()

    # 게임 속도 설정
    clock.tick(200)

pygame.quit()
