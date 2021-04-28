import pygame
from pygame import mixer
screen = pygame.display.set_mode((800, 600))
# tlo gry
background = pygame.image.load('galaxy.jpg')
# soundtrack

mixer.music.load('soundtrack.wav')
mixer.music.set_volume(0.5)
mixer.music.play(-1)
#highscore
highscore_file = 'highscore.txt'

# ikony i display
pygame.display.set_caption("Rocky The Destroyer")
icon = pygame.image.load('nuke.png')
pygame.display.set_icon(icon)

# gracz
playerImage = pygame.image.load('rock.png')
playerX = 370
playerY = 512
playerX_change = 0
# przeciwnik

enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_enemy = 6



# strzal
bulletImage = pygame.image.load('moon.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# wynik
score_val = 0
font = pygame.font.Font('Pacifico.ttf', 24)

fontX = 5
fontY = 5
# game over
over_font = pygame.font.Font('Roboto.ttf', 50)
byetext = pygame.image.load('gameover.jpg')

level_val = 1

