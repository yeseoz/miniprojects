# dinoRun
import pygame
import os
import random

pygame.init()

ASSETS = './studyPyGame/Assets/'
SCREEN_WIDTH = 1100 # 게임 윈도우 넓이
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('게임 v0.3')
icon = pygame.image.load('./studyPyGame/dinoRun.png')
pygame.display.set_icon(icon)

# 배경이미지 로드
BG = pygame.image.load(os.path.join(f'{ASSETS}Other', 'Track.png'))

# 공룡을 그리기 위한 작업
RUNNING = [pygame.image.load(f'./studyPyGame/Assets/Dino/DinoRun1.png'),
           pygame.image.load(f'{ASSETS}Dino/DinoRun2.png'),]
DUCKING = [pygame.image.load(f'{ASSETS}Dino/DinoDuck1.png'),
           pygame.image.load(f'{ASSETS}Dino/DinoDuck2.png'),]
JUMPING = pygame.image.load(f'{ASSETS}Dino/DinoJump.png')
START = pygame.image.load(f'{ASSETS}Dino/DinoStart.png') # 첫시작 이미지
DEAD = pygame.image.load(f'{ASSETS}Dino/DinoDead.png') # 죽음 이미지

# 구름 이미지
CLOUD = pygame.image.load(f'{ASSETS}Other/Cloud.png')

# 익룡이미지 로드
BIRD  = [pygame.image.load(f'{ASSETS}Bird/Bird1.png'),
         pygame.image.load(f'{ASSETS}Bird/Bird2.png')]

# 선인장 이미지 로드 / 애니메이션을 위한게 아니라 선인장 종류가 3개씩 
LARGE_CACTUS = [pygame.image.load(f'{ASSETS}Cactus/LargeCactus1.png'),
                pygame.image.load(f'{ASSETS}Cactus/LargeCactus2.png'),
                pygame.image.load(f'{ASSETS}Cactus/LargeCactus3.png')]
SMALL_CACTUS = [pygame.image.load(f'{ASSETS}Cactus/SmallCactus1.png'),
                pygame.image.load(f'{ASSETS}Cactus/SmallCactus2.png'),
                pygame.image.load(f'{ASSETS}Cactus/SmallCactus3.png')]

class Dino: # 공룡 클래스
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340 
    JUMP_VEL = 9.0

    def __init__(self) -> None:
        self.run_img = RUNNING
        self.duck_img = DUCKING
        self.jump_img = JUMPING

        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL # 점프 초기 값 9.0
        self.image = self.run_img[0]

        # 공룡 사각형 사이즈를 잡기위해
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput) -> None:
        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0 # 애니메이션 스텝

        if userInput[pygame.K_UP] and not self.dino_jump: # 점프
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.dino_rect.y = self.Y_POS # 이게 없으면 공룡이 하늘로 날아감
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not(self.dino_jump or userInput[pygame.K_DOWN]): # 런
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect() # 이미지 사각형 정보
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.step_index // 5] # duck_img
        self.dino_rect = self.image.get_rect() # 이미지 사각형 정보
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK # 이미지 높이가 작으니까 변경해줘야함
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL: # -9.0 이 되면 점프 중단
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL # 9.0으로 초기화
    
    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud: # 구름 클래스
    def __init__(self) -> None:
        self.x = SCREEN_WIDTH + random.randint(300, 500)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self) -> None:
        self.x -= game_speed
        if self.x < -self.width: # 화면 밖으로 벗어나면
            self.x = SCREEN_WIDTH + random.randint(1300, 2000)
            self.y = random.randint(50, 100)
    
    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle: # 장애물 클래스(부모)
    def __init__(self, image, type) -> None:
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH # 1100

    def update(self) -> None:
        self.rect.x -= game_speed
        if self.rect.x <= -self.rect.width: # 왼쪽 화면밖으로 벗어나면
            obstacles.pop() # 장애물 리스트에 하나 꺼내오기

    def draw(self, SCREEN) -> None:
        SCREEN.blit(self.image[self.type], self.rect)

class Bird(Obstacle): # 장애물 클래스 상속 클래스
    def __init__(self, image) -> None:
        self.type = 0 # 새는 0이다
        super().__init__(image, self.type)
        self.rect.y = 250 # 새니까 하늘에 그리는거임
        self.index = 0

    def draw(self, SCREEN) -> None: # draw 재정의
        if self.index >=  9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

class LargeCactus(Obstacle):
    def __init__(self, image) -> None:
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class SmallCactus(Obstacle):
    def __init__(self, image) -> None:
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325    
    
def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, font
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    run = True
    clock = pygame.time.Clock()
    dino = Dino()
    cloud = Cloud()
    game_speed = 14
    obstacles = []
    death_count = 0

    font = pygame.font.Font(f'{ASSETS}NanumGothicBold.ttf', 20)

    def score(): # 함수 내 함수 점수 표시
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed +=1

        txtScore = font.render(f'SCORE : {points}', True, (83, 83, 83))
        txtRect = txtScore.get_rect()
        txtRect.center = (1000, 40)
        SCREEN.blit(txtScore, txtRect)           

    def background(): # 땅바닥 update, draw 동시에 해주는 함수
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width() # 2404
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg)) # 0, 380 먼저그림
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg)) # 2404 + 0, 380
        if x_pos_bg <= - image_width:
            x_pos_bg = 0
        
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255)) # 배경 흰색
        userInput = pygame.key.get_pressed()
        
        background()
        score()
        
        cloud.draw(SCREEN) # 구름 애니메이션
        cloud.update() # 구름이 공룡보다 먼저 그려져야 공룡이 앞으로 옴

        dino.draw(SCREEN) # 공룡 그리기        
        dino.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0: # 작은 선인장
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1: # 작은 선인장
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obs in obstacles:
            obs.draw(SCREEN)
            obs.update()
            if dino.dino_rect.colliderect(obs.rect): # 총알이날라가면 맞는다! 충돌감지 
                #pygame.draw.rect(SCREEN,(255,0,0), dino.dino_rect,3)
                pygame.time.delay(1500) # 1.5 초딜레이
                death_count +=1 # 죽음
                menu(death_count) # 메인 메뉴화면으로 전환

        clock.tick(30) # 30프레임 기본 , 수를 올릴 수록 빨라짐
        pygame.display.update() # 초당 30번 update 수행

# 메뉴함수
def menu(death_count):
    global points, font
    font = pygame.font.Font(f'{ASSETS}NanumGothicBold.ttf', 20)
    run = True
    while run:
        SCREEN.fill((255, 255, 255)) # 하얗게 칠함

        if death_count == 0: # 최초
            text = font.render('시작하려면 아무키나 누르세요', True, (83, 83, 83))
            SCREEN.blit(START, ((SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))) 
        elif death_count > 0: # 죽음
            text = font.render('재시작하려면 아무키나 누르세요', True, (83, 83, 83))
            score = font.render(f'SCORE : {points}', True, (83, 83, 83)) # 죽으면 보여주기
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50) # 정중앙보다 밑으로 더 떨어짐
            SCREEN.blit(score, scoreRect)
            SCREEN.blit(DEAD, ((SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140)))
    
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit() # 완전 종료
            if event.type == pygame.KEYDOWN:
                main() 



if __name__ == '__main__':
    menu(death_count=0)