import pygame
import random

# 화면 크기 설정
size = [600,800]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

pygame.display.set_caption("피하기 게임") 


## 컬러 세팅 ##
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

background = pygame.image.load("C:\project\파이썬 스터디\pyGame 만들기\배경.png")
character = pygame.image.load("C:\project\파이썬 스터디\pyGame 만들기\졸라맨.png")
bomb = pygame.image.load("C:\project\파이썬 스터디\pyGame 만들기\폭탄.png")



