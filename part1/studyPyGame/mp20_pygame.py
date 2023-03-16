# Python Game - PyGame => Game Framework
# pip install pygame
import pygame

pygame.init() # 게임초기화 무조건 필수!
width = 500; height = 500

win = pygame.display.set_mode((500, 500)) # 윈도우 640 * 400
pygame.display.set_caption('게임!')
icon = pygame.image.load('./studyPyGame/game.png')
pygame.display.set_icon(icon)

# object
x = 250
y = 250
radius = 10
vel_x = 10 
vel_y = 10
jump = False


run = True

while run:
    win.fill((0, 0, 0))
    pygame.draw.circle(win, (255, 255, 255), (x, y), radius)

    # 이벤트 = 시그널
    for event in pygame.event.get(): # get으로 이벤트 받기 중요!
        if event.type == pygame.QUIT: # 종료가 되면
            run = False # 종료

    # 객체이동
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 10:
        x -= vel_x # 왼쪽으로 10씩 이동
    if userInput[pygame.K_RIGHT] and x < width - 10:
        x += vel_x
    # if userInput[pygame.K_UP] and y > 10:
    #     y -= vel_y
    # if userInput[pygame.K_DOWN] and y < height - 10:
    #     y += vel_y
    
    # 객체 점프!
    if jump == False and userInput[pygame.K_SPACE]:
        jump = True
    if jump == True:
        y -= vel_y * 3
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10
    

    pygame.time.delay(10) # ms
    pygame.display.update() # 화면 업데이트 !!! 중요!!!!

