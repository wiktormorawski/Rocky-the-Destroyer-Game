import pygame, random, math
from pygame import mixer
from os import path

pygame.init()

screen = pygame.display.set_mode((800, 600))
# tlo gry
background = pygame.image.load('galaxy.jpg')
# soundtrack

mixer.music.load('soundtrack.wav')
mixer.music.set_volume(0.5)
mixer.music.play(-1)
# highscore


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


def creating_enemies_tables(number_enemy):
    for e in range(number_enemy):
        enemyImage.append(pygame.image.load('spaceship.png'))
        enemyX.append(random.randint(0, 735))
        enemyY.append(0)
        speed_change_val = random.randint(1, 3)
        enemyX_change.append(1 * speed_change_val)
        speed_change_val = random.randint(1, 3)
        enemyY_change.append(1 * speed_change_val)


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
over_font = pygame.font.Font('Roboto.ttf', 40)
byetext = pygame.image.load('gameover.jpg')

level_val = 1


def number_enemy_add(number_enemy, level_val):
    if level_val == 2:
        number_enemy = 8
    if level_val == 3:
        number_enemy = 9
    if level_val == 4:
        number_enemy = 10
    if level_val == 5:
        number_enemy = 11
    if level_val == 6:
        number_enemy = 13
    if level_val == 7:
        number_enemy = 15
    if level_val == 8:
        number_enemy = 17
    if level_val == 9:
        number_enemy = 19
    return number_enemy


def level(level_val):
    if score_val > 10:
        level_val = 2
    if score_val > 30:
        level_val = 3
    if score_val > 40:
        level_val = 4
    if score_val > 50:
        level_val = 5
    return level_val


def score_display(x, y):
    score = font.render("score  " + str(score_val), True, (0, 0, 200))
    screen.blit(score, (x, y))


def level_display():
    level_in_game0 = font.render("level  " + str(level_val), True, (250, 250, 250))
    screen.blit(level_in_game0, (700, 0))


def game_over_str(score_val):
    high = score_val
    over_text = over_font.render("U GOT HIT BY AN ENEMY :(", True, (255, 255, 255))
    screen.blit(over_text, (100, 0))
    score_end = font.render('Your score was : ' + str(score_val), True, (255, 0, 0))
    screen.blit(score_end, (100, 250))
    level_end = font.render('You have reached level : ' + str(level_val), True, (0, 0, 255))
    screen.blit(level_end, (100, 340))
    x = highscore(high)
    if x == True:
        score_new = over_font.render('New HighScore : ' + str(high), True, (0, 0, 255))
        screen.blit(score_new, (100, 550))


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y, k):
    screen.blit(enemyImage[k], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImage, (x + 16, y + 16))


# dystans pomiedzy wrogiem a naszym pociskiem

def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 36:
        return True
    else:
        return False


def game_over(enemyX, enemyY, playerX, playerY):
    distance_game_over = math.sqrt(math.pow(playerX - enemyX, 2) + math.pow(playerY - enemyY, 2))
    if distance_game_over < 36:
        return True
    else:

        return False


def highscore(high):
    with open("score_file.txt", "r+") as hisc:
        hi = hisc.read()
        if not hi:  # not hi will only be true for strings on an empty string
            hi = '0'
        if high > int(hi):
            hisc.seek(0)  # We already read to the end. We need to go back to the start
            hisc.write(str(high))
            hisc.truncate()  # Delete anything left over... not strictly necessary
        if high == int(hi):
            return True
        else:
            return False

highscore(-1)
# glowny loop
running = True
while running:

    screen.fill((0, 255, 0))
    creating_enemies_tables(number_enemy)
    # dodanie tla
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -7
            if event.key == pygame.K_RIGHT:
                playerX_change = 7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('bulletshot.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # uderzanie o sciane statku
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    # GAME OVER
    for k in range(number_enemy):
        isgame_over = game_over(enemyX[k], enemyY[k], playerX, playerY)
        if isgame_over:
            screen.fill((0, 0, 0))
            game_over_str(score_val)
            break
        enemyX[k] += enemyX_change[k]
        if enemyX[k] < 0 or enemyX[k] > 736:
            enemyX_change[k] = -enemyX_change[k]
        enemyY[k] += enemyY_change[k]
        if enemyY[k] > 600:
            enemyY[k] = 0
        # kolizja
        collis = collision(enemyX[k], enemyY[k], bulletX, bulletY)
        if collis:
            boom_sound = mixer.Sound('hurt.wav')
            boom_sound.play()
            bullet_state = "ready"
            bulletY = 480
            score_val += 1
            level_val = level(level_val)
            number_enemy = number_enemy_add(number_enemy, level_val)
            enemyX[k] = random.randint(0, 735)
            enemyY[k] = 0

        enemy(enemyX[k], enemyY[k], k)

    # strzal
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if isgame_over == False:
        player(playerX, playerY)
        score_display(fontX, fontY)
        level_display()
        pygame.display.update()
    if isgame_over == True:
        playerX_change = 0
        pygame.display.update()
if __name__ == '__main__':
    test_add_enemy()
    print('test1 : ok')
