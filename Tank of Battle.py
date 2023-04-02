import pygame, math, time, os, sys, random
clock = pygame.time.Clock()
crosshair = pygame.image.load('image/crosshair.png')
crosshair = pygame.transform.scale(crosshair, (10, 10))
cursor_rect = crosshair.get_rect()

intro = pygame.image.load('image/menu/intro.png')
os.environ['SDL_VIDEO_CENTERED'] = '1' 
pygame.init()
win = pygame.display.set_mode((900,650),pygame.NOFRAME) 
win.blit(pygame.image.load('image/menu/intro.png'), (0, 0))
pygame.display.update() 
                
               ####        IMPORT IMAGES       ####

tank_blue = [pygame.image.load('image/tank_blue/right(171).png'), pygame.image.load('image/tank_blue/right(162).png'), pygame.image.load('image/tank_blue/right(153).png'),
pygame.image.load('image/tank_blue/right(144).png'), pygame.image.load('image/tank_blue/right(135).png'), pygame.image.load('image/tank_blue/right(126).png'),
pygame.image.load('image/tank_blue/right(117).png'), pygame.image.load('image/tank_blue/right(108).png'), pygame.image.load('image/tank_blue/right(99).png'),
pygame.image.load('image/tank_blue/right(90).png'), pygame.image.load('image/tank_blue/right(81).png'), pygame.image.load('image/tank_blue/right(72).png'),
pygame.image.load('image/tank_blue/right(63).png'), pygame.image.load('image/tank_blue/right(54).png'), pygame.image.load('image/tank_blue/right(45).png'),
pygame.image.load('image/tank_blue/right(36).png'), pygame.image.load('image/tank_blue/right(27).png'), pygame.image.load('image/tank_blue/right(18).png'),
pygame.image.load('image/tank_blue/right(9).png'), pygame.image.load('image/tank_blue/back.png'),
pygame.image.load('image/tank_blue/left(9).png'), pygame.image.load('image/tank_blue/left(18).png'), pygame.image.load('image/tank_blue/left(27).png'),
pygame.image.load('image/tank_blue/left(36).png'), pygame.image.load('image/tank_blue/left(45).png'), pygame.image.load('image/tank_blue/left(54).png'),
pygame.image.load('image/tank_blue/left(63).png'), pygame.image.load('image/tank_blue/left(72).png'), pygame.image.load('image/tank_blue/left(81).png'),
pygame.image.load('image/tank_blue/left(90).png'), pygame.image.load('image/tank_blue/left(99).png'), pygame.image.load('image/tank_blue/left(108).png'),
pygame.image.load('image/tank_blue/left(117).png'), pygame.image.load('image/tank_blue/left(126).png'), pygame.image.load('image/tank_blue/left(135).png'),
pygame.image.load('image/tank_blue/left(144).png'), pygame.image.load('image/tank_blue/left(153).png'), pygame.image.load('image/tank_blue/left(162).png'),
pygame.image.load('image/tank_blue/left(171).png'), pygame.image.load('image/tank_blue/front.png')]
for i in range(40):
   tank_blue[i] = pygame.transform.scale(tank_blue[i], (200, 160))

tank_red = [pygame.image.load('image/tank_red/right(171).png'), pygame.image.load('image/tank_red/right(162).png'), pygame.image.load('image/tank_red/right(153).png'),
pygame.image.load('image/tank_red/right(144).png'), pygame.image.load('image/tank_red/right(135).png'), pygame.image.load('image/tank_red/right(126).png'),
pygame.image.load('image/tank_red/right(117).png'), pygame.image.load('image/tank_red/right(108).png'), pygame.image.load('image/tank_red/right(99).png'),
pygame.image.load('image/tank_red/right(90).png'), pygame.image.load('image/tank_red/right(81).png'), pygame.image.load('image/tank_red/right(72).png'),
pygame.image.load('image/tank_red/right(63).png'), pygame.image.load('image/tank_red/right(54).png'), pygame.image.load('image/tank_red/right(45).png'),
pygame.image.load('image/tank_red/right(36).png'), pygame.image.load('image/tank_red/right(27).png'), pygame.image.load('image/tank_red/right(18).png'),
pygame.image.load('image/tank_red/right(9).png'), pygame.image.load('image/tank_red/back.png'),
pygame.image.load('image/tank_red/left(9).png'), pygame.image.load('image/tank_red/left(18).png'), pygame.image.load('image/tank_red/left(27).png'),
pygame.image.load('image/tank_red/left(36).png'), pygame.image.load('image/tank_red/left(45).png'), pygame.image.load('image/tank_red/left(54).png'),
pygame.image.load('image/tank_red/left(63).png'), pygame.image.load('image/tank_red/left(72).png'), pygame.image.load('image/tank_red/left(81).png'),
pygame.image.load('image/tank_red/left(90).png'), pygame.image.load('image/tank_red/left(99).png'), pygame.image.load('image/tank_red/left(108).png'),
pygame.image.load('image/tank_red/left(117).png'), pygame.image.load('image/tank_red/left(126).png'), pygame.image.load('image/tank_red/left(135).png'),
pygame.image.load('image/tank_red/left(144).png'), pygame.image.load('image/tank_red/left(153).png'), pygame.image.load('image/tank_red/left(162).png'),
pygame.image.load('image/tank_red/left(171).png'), pygame.image.load('image/tank_red/front.png')]

for i in range(40):
   tank_red[i] = pygame.transform.scale(tank_red[i], (200, 160))

menu = [pygame.image.load('image/menu/play.png'), pygame.image.load('image/menu/controling.png'), pygame.image.load('image/menu/back.png'),
        pygame.image.load('image/menu/quit.png'), pygame.image.load('image/menu/exit.png'), pygame.image.load('image/menu/pic.png'),]
menu[4] = pygame.transform.scale(menu[4], (70, 70))

help = [pygame.image.load('image/menu/wasd.png'), pygame.image.load('image/menu/space.png'), pygame.image.load('image/menu/up+down.png'),]
help[0] = pygame.transform.scale(help[0], (422, 251))
help[1] = pygame.transform.scale(help[1], (422, 150))
help[2] = pygame.transform.scale(help[2], (422, 150))

point = [pygame.image.load('image/point/point_up_blue.png'), pygame.image.load('image/point/point_down_blue.png'),
         pygame.image.load('image/point/point_up_red.png'), pygame.image.load('image/point/point_down_red.png')]
for i in range(4):
    point[i] = pygame.transform.scale(point[i], (50, 30))

wall = [pygame.image.load("image/walls/box.png"), pygame.image.load("image/walls/barrel.png"), #0 1
        pygame.image.load("image/walls/grass.png"), pygame.image.load("image/walls/water.png"), #2 3
        pygame.image.load("image/walls/up_walls_v2.png"), pygame.image.load("image/walls/mid.png"), #4 5
        pygame.image.load("image/walls/midg.png"), pygame.image.load("image/walls/midg2.png"), #6 7
        pygame.image.load("image/walls/midb.png"), pygame.image.load("image/building.png")] #8 9

health_bar = [pygame.image.load("image/health_ind/healthbar.png"), pygame.image.load("image/health_ind/blue.png"), 
              pygame.image.load("image/health_ind/yellow.png"), pygame.image.load("image/health_ind/hard.png")]

tab_anim = [pygame.image.load("image/tab/1.png"), pygame.image.load("image/tab/2.png"), pygame.image.load("image/tab/3.png"),
            pygame.image.load("image/tab/4.png"), pygame.image.load("image/tab/5.png"), pygame.image.load("image/tab/6.png"),]

text_win = pygame.image.load("image/win.png")
text_lose = pygame.image.load("image/lose.png")

width_map = 900
height_map = 1400
map = pygame.image.load("image/map/map_sand.png")
map = pygame.transform.scale(map, (width_map, height_map))

        ##Show game


#time.sleep(1) 

pygame.display.set_caption("Tank battles")
win = pygame.display.set_mode((900, 650))
pygame.mouse.set_visible(False)

font = pygame.font.Font(None, 40)
font_text = pygame.font.SysFont("comicsansms", 20)
font_text2 = pygame.font.SysFont("comicsansms", 10)

tank_hp = font_text.render(str("100 HP"), True, (0, 0, 0))
base_hp = font_text.render(str("100 HP"), True, (0, 0, 0))
t_time = font_text.render(str("Time"), True, (255, 255, 255))
t_kill = font_text.render(str("Kills"), True, (255, 255, 255))
t_deaths = font_text.render(str("Deaths"), True, (255, 255, 255))
t_press = font_text.render(str("Press SPACE..."), True, (255, 255, 255))
PROPERTY = font_text2.render(str("This product is property of Squad"), True, (255, 255, 255))
        ## $
x = 400
y = 350
x_const = 400
y_const = 350

px = 0
py = -750
mx = 0
my = 0   
pos = 19
degree = -(math.pi/2)

x_left = 61
x_right = 900 - 61 - 197
y_up = -400 - 50 + 3
y_down = 200 + 14
y_mid = -197 + 50

x_build = 341
y_build = 250 + 4

y_over_up = -630 - 80
y_over_down = 650 - 170 - 110

run = 1
check = True

x_anemy = 350
y_anemy = -900
x_anemyRespawn = 350
y_anemyRespawn = -900 
Rerotate = False

blueT_healht = 100
base_healht = 100

speed = 4
speed_scroll = 5

bullets = []
anemy1_bullets = []
anemy2_bullets = []
black = (0, 0, 0)
white = (255, 255, 255)

x_health_bar_menu = width_map-200
x_healthbase_bar_menu = width_map-169

timer_play=0
timer_milsec=0
timer_sec=0
timer_min=0

timer_bool = False
timer_block_movement=0 

run_death_time = False
death_enemy_count = 0
deaths = 0
        ##
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def timer():
   now = time.localtime(time.time())
   return now[5]
def menu_init():
    win.blit(intro, (0, 0))
    win.blit(menu[0], (-40, 250))
    win.blit(menu[1], (20, 350))
    win.blit(menu[3], (-20, 470))
    win.blit(PROPERTY, (0,0))
    win.blit(crosshair, cursor_rect)  
def cont_init():
    win.blit(menu[5], (0, 0))
    win.blit(menu[2], (-40, 150))
    win.blit(help[0], (450, 30))
    win.blit(help[1], (450, 300))
    win.blit(help[2], (450, 450))
    win.blit(crosshair, cursor_rect)
def drawWindow():
    global px, py, pos, deaths, death_enemy_count, base_healht, timer_min
    win.blit(map, (px, py)) 

    for bullet in bullets:
        bullet.draw()
    for anemy1_bullet in anemy1_bullets:
        anemy1_bullet.draw()
    for anemy2_bullet in anemy2_bullets:
        anemy2_bullet.draw()

    win.blit(tank_blue[pos], (x, y))
    anemy1.TankShow()
    anemy2.TankShow()

    win.blit(wall[2], (x_left, y_down))
    win.blit(wall[2], (x_right, y_down))
    win.blit(wall[4], (x_left, y_up))
    win.blit(wall[4], (x_right, y_up))
    win.blit(wall[6], (width_map/2 - 197, y_mid))
    win.blit(wall[5], (width_map/2 - 197, y_mid))
    win.blit(wall[5], (width_map/2 - 197, y_mid))
    win.blit(wall[9], (x_build, y_build))
    #win.blit(menu[4], (10, 10))
    x_point = x + 75
    if y < -110:
        win.blit(point[0], (x_point, 20))
    elif y > 610:
        win.blit(point[1], (x_point, 610))

    win.blit(health_bar[1], (x_health_bar_menu, 58))
    win.blit(health_bar[2], (x_healthbase_bar_menu, 155))
    win.blit(health_bar[0], (width_map-200, 0))
    if deaths == 0:
        win.blit(health_bar[3], (width_map-160, 50))
        win.blit(health_bar[3], (width_map-180, 50))
        win.blit(health_bar[3], (width_map-200, 50))
    elif deaths == 1:
        win.blit(health_bar[3], (width_map-200, 50))
        win.blit(health_bar[3], (width_map-180, 50))
    elif deaths == 2:
        win.blit(health_bar[3], (width_map-200, 50))
    win.blit(health_bar[3], (width_map-170, 135))

    win.blit(tank_hp, (720, 20))
    win.blit(base_hp, (745, 115))

    t2_time = font_text.render(str(timer_min)+":"+str(timer_sec)+":"+str(timer_milsec), True, (255, 255, 255))
    t2_kill = font_text.render(str(death_enemy_count), True, (255, 255, 255))
    t2_deaths = font_text.render(str(deaths), True, (255, 255, 255))
    if deaths == 3 or base_healht <= 0:
        win.blit(tab_anim[5], (0, 0))
        if timer_min >= 1:
            win.blit(text_win,(width_map/2-100, 50))
        else:
            win.blit(text_lose,(width_map/2-100, 50))
        win.blit(t_time, (width_map/2-100, 200))
        win.blit(t_kill, (width_map/2-100, 300))
        win.blit(t_deaths, (width_map/2-100, 400))

        win.blit(t2_time, (width_map/2, 200))
        win.blit(t2_kill, (width_map/2, 300))
        win.blit(t2_deaths, (width_map/2, 400))

        win.blit(t_press, (width_map/2-70, 580))
        
    #win.blit(crosshair, cursor_rect)
    pygame.draw.circle(win, white, (mx, my), 5)
  

class Anemy():
    def __init__(self, x, y, pos, cx, cy, degree):  
                    ### Initialisation integers
        self.x = x
        self.y = y
        self.pos = 39
        self.cx = cx
        self.cy = cy
        self.degree = math.pi/2
        self.health = 100
        self.death_enemy_count = 0
                    ###       Riding      ###
    def RadingForward(self):
        self.x = self.x + self.cx*speed
        self.y = self.y + self.cy*speed
    def RadingBackward(self):
        self.x = self.x - self.cx*speed
        self.y = self.y - self.cy*speed
                    ### Rotating ###
    def RotateLeft(self):
        self.pos = self.pos - 1
        self.degree = self.degree - math.pi/20
        if self.pos < 0:
            self.pos = 39
        self.cx = math.cos(self.degree)
        self.cy = math.sin(self.degree)
    def RotateRight(self):
        self.pos = self.pos + 1
        self.degree = self.degree + math.pi/20
        if self.pos > 39:
            self.pos = 0
        self.cx = math.cos(self.degree)
        self.cy = math.sin(self.degree)
                    ### Initialisation tank ###
    def TankShow(self):
        win.blit(tank_red[self.pos], (self.x, self.y))
                    ### Change health ###
    def Damage(self, new_health):
        self.health -= new_health
                    ###     Respawn     ###
    def Respawn(self):
        self.x = x_anemyRespawn
        self.y = y_anemyRespawn
        self.degree = math.pi/2
        self.pos = 39
        self.health = 100
        self.cx = math.cos(self.degree)
        self.cy = math.sin(self.degree)
        health_bar[1] = pygame.transform.scale(health_bar[1], (200, 32))
        #x_health_bar_menu = width_map-200
                    #      Scrolling        #
    def ScrollUp(self):
        global y_anemyRespawn
        self.y += speed_scroll
        y_anemyRespawn += speed_scroll
    def ScrollDown(self):
        global y_anemyRespawn
        self.y -= speed_scroll
        y_anemyRespawn -= speed_scroll
                    ##      Collution with walls        ##
    def Collution(self):
        if (x_left <= self.x+46 <= x_left+197) and (y_down-200 <= self.y+29 <= y_down) or (x_right-110 <= self.x+46 <= x_right+197) and (y_down-200 <= self.y+29 <= y_down) or (x_left-197 <= self.x+46 <= x_left+197) and (y_up-30 <= self.y+29 <= y_up+170) or (x_right-110 <= self.x+46 <= x_right+197) and (y_up-30 <= self.y+29 <= y_up+170) or (150 <= self.x+46 <= width_map/2+200-5) and (y_mid-100 <= self.y+29 <= y_mid+100) or self.x <= 20 or self.x >= 680 or self.y >= y_over_down-100 or (width_map/2-100 <= self.x+46 <= width_map/2+50) and (y_mid+70 <= self.y+29 <= y_mid+270) or (x_left-150 <= self.x <= x_left+230) and (y_up-500 <= self.y <= y_up-280) or (x_right-230 <= self.x <= x_right+300) and (y_up-500 <= self.y <= y_up-280) or (x_right-250 <= self.x <= x_right-200) and (y_up-200 <= self.y <= y_up):
            a = random.randint(0, 1)
            #print("Left/Right: ", a)
            anemy1.RadingBackward()
            if a == 1:
                print("Rotate Left")
                for i in range(10):
                    anemy1.RotateLeft()
            else:
                print("Rotate Right")
                for i in range(10):
                    anemy1.RotateRight()
        if (y_over_up-200 >= self.y):
            anemy1.RadingBackward()
            print("Rotate Back ")
            for i in range(20):
                anemy1.RotateLeft()
    def mod(self):
        global Rerotate, x, y, blueT_healht, x_health_bar_menu, x_healthbase_bar_menu, base_healht, py, run, death_enemy_count
        anemy1_bullet = Ammo(self.x, self.y, 5, black, self.cx, self.cy, self.degree)
        for anemy1_bullet in anemy1_bullets:
            if (x_left <= anemy1_bullet.x+46 <= x_left+160) and (y_down-110 <= anemy1_bullet.y+29 <= y_down) or (x_right-60 <= anemy1_bullet.x+46 <= x_right+150) and (y_down-110 <= anemy1_bullet.y+29 <= y_down) or (x_left <= anemy1_bullet.x+46 <= x_left+160) and (y_up-30 <= anemy1_bullet.y+29 <= y_up+50) or (x_right-60 <= anemy1_bullet.x+46 <= x_right+150) and (y_up-30 <= anemy1_bullet.y+29 <= y_up+50) or (230 <= anemy1_bullet.x+46 <= width_map/2+150) and (y_mid <= anemy1_bullet.y+29 <= y_mid+50) or anemy1_bullet.x <= -30 or anemy1_bullet.x >= 730 or anemy1_bullet.y >= y_over_down+20 or anemy1_bullet.y <= y_over_up-100:
                anemy1_bullets.pop(anemy1_bullets.index(anemy1_bullet))
            elif (x-46 <= anemy1_bullet.x <= x+46) and (y-29 <= anemy1_bullet.y <= y+29):
                anemy1_bullet.BlueTdamage()  
                anemy1_bullets.pop(anemy1_bullets.index(anemy1_bullet))
            elif (x_build-246 <= anemy1_bullet.x <= x_build+246) and (y_build+100 <= anemy1_bullet.y <= y_build+304):
                anemy1_bullet.Basedamage()
                if self.y > 610:
                    win.blit(point[3], (self.x+75, 610))
                anemy1_bullets.pop(anemy1_bullets.index(anemy1_bullet))
            else:
                anemy1_bullet.ShootMove()
        if math.pow((x_build+123 - self.x), 2) + math.pow((y_build+152 - self.y), 2) <= math.pow(325, 2):   ### Detect Base
            if len(anemy1_bullets) < 1:
                anemy1_bullets.append(Ammo(self.x, self.y, 5, black, self.cx, self.cy, self.degree))
 
            if self.x+200/2 < x_build+246/2 and self.y+160/2 < y_build+304/2:      # 1/4
                gip = math.sqrt(math.pow((y_build+304/2-self.y+160/2), 2) + math.pow((x_build+246/2-self.x+200/2), 2))
                alol = (y_build+304/4-self.y+160/2)/gip
                alol = math.floor(math.degrees(alol))
                if alol > 45:
                    alol = 45
            elif self.x+200/2 > x_build+246/2 and self.y+160/2 < y_build+304/2:    # 2/4
                gip = math.sqrt(math.pow((y_build-self.y), 2) + math.pow((self.x-x_build), 2))
                alol = (x_build+246/4-self.x)/gip
                alol = -(math.floor(math.degrees(alol)))+45
                if alol > 90:
                    alol = 90
            elif self.x+200/2 > x_build+246/2 and self.y+160/2 > y_build+304/2:    # 3/4
                gip = math.sqrt(math.pow((self.y+160/2-y_build+304/2), 2) + math.pow((self.x+200/2-x_build+246/2), 2))
                alol = (self.y+160/2-y_build+304/2)/gip
                alol = math.floor(math.degrees(alol))+90
                if alol > 135:
                    alol = 135
            elif self.x+200/2 < x_build+246/2 and self.y+160/2 > y_build+304/2:    # 4/4       
                gip = math.sqrt(math.pow((self.y+160/2-y_build+304/2), 2) + math.pow((x_build+246/2-self.x+200/2), 2))
                alol = (x_build+246/2-self.x+200/2)/gip
                alol = math.floor(math.degrees(alol))+135
                if alol > 180:
                    alol = 180

            if alol%9 == 1:
                alol -= 1
            elif alol%9 == 2:
                alol -= 2
            elif alol%9 == 3:
                alol -= 3
            elif alol%9 == 4:
                alol -= 4
            elif alol%9 == 5:
                alol += 4
            elif alol%9 == 6:
                alol += 3
            elif alol%9 == 7:
                alol += 2
            elif alol%9 == 8:
                alol += 1
            alol = alol/5
            #print(alol)
            self.degree = math.pi*2
            self.pos = 29
            self.cx = math.cos(self.degree)
            self.cy = math.sin(self.degree)
            for i in range(int(alol)):
                anemy1.RotateRight()
            if self.health <= 0:
                anemy1.Respawn()
        elif math.pow((x+100 - self.x), 2) + math.pow((y+80 - self.y), 2) <= math.pow(350, 2):   ### Detect Tank
            Rerotate = True
            if len(anemy1_bullets) < 1:
                anemy1_bullets.append(Ammo(self.x, self.y, 5, black, self.cx, self.cy, self.degree))
            if self.x < x and self.y < y:      # 1/4
                gip = math.sqrt(math.pow((y-self.y), 2) + math.pow((x-self.x), 2))
                alol = (y-self.y)/gip
                alol = math.floor(math.degrees(alol))
                if alol > 45:
                    alol = 45
            elif self.x > x and self.y < y:    # 2/4
                gip = math.sqrt(math.pow((y-self.y), 2) + math.pow((self.x-x), 2))
                alol = (x-self.x)/gip
                alol = -(math.floor(math.degrees(alol)))+45
                if alol > 90:
                    alol = 90
            elif self.x > x and self.y > y:    # 3/4
                gip = math.sqrt(math.pow((self.y-y), 2) + math.pow((self.x-x), 2))
                alol = (self.y-y)/gip
                alol = math.floor(math.degrees(alol))+90
                if alol > 135:
                    alol = 135
            elif self.x < x and self.y > y:    # 4/4         
                gip = math.sqrt(math.pow((self.y-y), 2) + math.pow((x-self.x), 2))
                alol = (x-self.x)/gip
                alol = math.floor(math.degrees(alol))+135
                if alol > 180:
                    alol = 180

            if alol%9 == 1:
                alol -= 1
            elif alol%9 == 2:
                alol -= 2
            elif alol%9 == 3:
                alol -= 3
            elif alol%9 == 4:
                alol -= 4
            elif alol%9 == 5:
                alol += 4
            elif alol%9 == 6:
                alol += 3
            elif alol%9 == 7:
                alol += 2
            elif alol%9 == 8:
                alol += 1
            alol = alol/5#4.5
            print(alol)
            self.degree = math.pi*2
            self.pos = 29
            self.cx = math.cos(self.degree)
            self.cy = math.sin(self.degree)
            for i in range(int(alol)):
                anemy1.RotateRight()
            if self.health <= 0:
                anemy1.Respawn()
        else:
            if Rerotate == True:
                self.pos = 39
                self.degree = math.pi/2
                self.cx = math.cos(self.degree)
                self.cy = math.sin(self.degree)
                Rerotate = False
            if self.health > 0:
                anemy1.RadingForward()
                anemy1.Collution()
            else:
                anemy1.Respawn()
        if base_healht <= 0 :
            death_enemy_count += 1
  

anemy1 = Anemy(x_anemy, y_anemy, 39, 0, 1, math.pi/2)
anemy2 = Anemy(x_anemy, y_anemy, 39, 0, 1, math.pi/2)

class Ammo():
    def __init__(self, x, y, radius, color, cx, cy, degree):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.cx = cx
        self.cy = cy
    def draw(self):
        pygame.draw.circle(win, self.color,  (math.ceil(self.x+200/2), math.ceil(self.y+160/2)), self.radius)
    def ShootMove(self):
        self.x = self.x + self.cx * speed*5
        self.y = self.y + self.cy * speed*5
    def AnemyCollution(self):
        random_damage = random.randint(25, 50)
        print("Damage: ", random_damage)
        anemy1.Damage(random_damage) 
    def BlueTdamage(self):
        global blueT_healht, x_health_bar_menu, tank_hp, x, y, deaths, timer_bool, timer_block_movement

        random_damage = random.randint(10, 25)
        x_health_bar_menu += int((203/100)*random_damage)
        blueT_healht -= random_damage

        if blueT_healht <= 0:
            blueT_healht = 100 
            x_health_bar_menu = width_map - 200
            deaths += 1
            x = x_const
            y = y_const
        tank_hp = font_text.render(str(blueT_healht)+" HP", True, (0, 0, 0))
    def Basedamage(self):
        global base_healht, x_healthbase_bar_menu, base_hp, death_enemy_count

        random_damage = random.randint(1, 5)
        x_healthbase_bar_menu += int((186/100)*random_damage)
        base_healht -= random_damage

        if base_healht <= 0:
            #base_healht = 100 
            x_healthbase_bar_menu = width_map - 169
            death_enemy_count += 1
        base_hp = font_text.render(str(base_healht)+" HP", True, (0, 0, 0))
                ## ///  Change a bullet degree  /// ##
    def ArotateLeft(self):
        self.degree = self.degree - math.pi/20
        self.cx = math.cos(self.degree)
        self.cy = math.sin(self.degree)
    def ArotateRight(self):
        self.degree = self.degree + math.pi/20
        self.cx = math.cos(self.degree)
        self.cy = math.sin(self.degree)

while check:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check = False
            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos
                mx, my = pygame.mouse.get_pos()
    pygame.display.update()
    if run == 1:                                                         # MENU
        clock.tick(60)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 60 and mx <= 330 and my >= 250 and my <= 250+76:
                run = 3
            elif mx >= 25 and mx <= 15+392 and my >= 360 and my <= 355+76:
                run = 2
            elif mx >= 80 and mx <= 310 and my >= 470 and my <= 460+76:
                check = False
        menu_init()
    elif run == 2:                                                      # HELP of CONTROLL
        clock.tick(60)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx >= 60 and mx <= 330 and my >= 150 and my <= 150+76:
                run = 1
        cont_init()  
    elif run == 3:                                                      # PLAY
        clock.tick(60)
        cx = math.cos(degree)
        cy = math.sin(degree)
        bullet = Ammo(x, y, 5, black, cx, cy, degree)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 1
            elif event.type == pygame.MOUSEMOTION:
                cursor_rect.center = event.pos
                mx, my = pygame.mouse.get_pos()
        if keys[pygame.K_ESCAPE]:
            run = 1
                        ## Shooting ## 
        for bullet in bullets:
            if (x_left <= bullet.x+46 <= x_left+160) and (y_down-110 <= bullet.y+29 <= y_down) or (x_right-60 <= bullet.x+46 <= x_right+150) and (y_down-110 <= bullet.y+29 <= y_down) or (x_left <= bullet.x+46 <= x_left+160) and (y_up-30 <= bullet.y+29 <= y_up+50) or (x_right-60 <= bullet.x+46 <= x_right+150) and (y_up-30 <= bullet.y+29 <= y_up+50) or (230 <= bullet.x+46 <= width_map/2+180) and (y_mid <= bullet.y+29 <= y_mid+50) or bullet.x <= -30 or bullet.x >= 730 or bullet.y >= y_over_down+20 or bullet.y <= y_over_up-100:
                bullets.pop(bullets.index(bullet))
            elif (anemy1.x-46 <= bullet.x <= anemy1.x+46) and (anemy1.y-29 <= bullet.y <= anemy1.y+29):
                bullet.AnemyCollution()
                print ("Anemy damaged!")
                bullets.pop(bullets.index(bullet))
            else:
                bullet.ShootMove()
        if keys[pygame.K_SPACE]:
            if len(bullets) < 1:
                bullets.append(Ammo(x, y, 5, black, cx, cy, degree))
                    ## $ ##
            #### Tank rotating ####
        if keys[pygame.K_a]:
            #bullet.ArotateLeft()
            if keys[pygame.K_LCTRL]:
                clock.tick(40)
            pos = pos - 1
            degree = degree - math.pi/20
            if pos < 0:
                pos = 39
        if keys[pygame.K_d]:
            #bullet.ArotateRight()
            if keys[pygame.K_LCTRL]:
                clock.tick(40)
            degree = degree + math.pi/20
            pos = pos + 1
            if pos > 39:
                pos = 0
            #### $ ####
            #   # Rading #   #
        if keys[pygame.K_w] and x >= 20 and x <= 680 and y >= y_over_up and y <= y_over_down:
            x = x + cx*speed
            y = y + cy*speed
            if (x_left <= x+46 <= x_left+197) and (y_down-200 <= y+29 <= y_down) or (x_right-110 <= x+46 <= x_right+197) and (y_down-200 <= y+29 <= y_down) or (x_left-197 <= x+46 <= x_left+197) and (y_up-30 <= y+29 <= y_up+170) or (x_right-110 <= x+46 <= x_right+197) and (y_up-30 <= y+29 <= y_up+170) or (150 <= x+46 <= width_map/2+200-5) and (y_mid-30 <= y+29 <= y_mid+70):
                x = x - cx*speed       
                y = y - cy*speed
        if keys[pygame.K_s] and x > 20 and x < 680 and y >= y_over_up and y <= y_over_down:
            x = x - cx*speed
            y = y - cy*speed
            if (x_left <= x+46 <= x_left+197) and (y_down-200 <= y+29 <= y_down) or (x_right-110 <= x+46 <= x_right+197) and (y_down-200 <= y+29 <= y_down) or (x_left-197 <= x+46 <= x_left+197) and (y_up-30 <= y+29 <= y_up+170) or (x_right-110 <= x+46 <= x_right+197) and (y_up-30 <= y+29 <= y_up+170) or (150 <= x+46 <= width_map/2+200-5) and (y_mid-30 <= y+29 <= y_mid+70):
                x = x + cx*speed
                y = y + cy*speed
        if x < 20:
            x = 20
        elif x > 680:
            x = 680
        elif y <= y_over_up:
            y = y_over_up
        elif y >= y_over_down:
            y = y_over_down

            #   # $ #   #
        ### Moving map ###
        if keys[pygame.K_UP] and py <= 0 - 5:
            y += speed_scroll
            py += speed_scroll
            y_down += speed_scroll
            y_up += speed_scroll
            y_mid += speed_scroll
            y_build += speed_scroll
            y_over_down += speed_scroll
            y_over_up += speed_scroll
            y_anemy += speed_scroll
            bullet.y += speed_scroll
            y_const += speed_scroll
            anemy1.ScrollUp()
        if keys[pygame.K_DOWN] and py >= -750 + 5:
            y -= speed_scroll
            py -= speed_scroll
            y_down -= speed_scroll
            y_up -= speed_scroll
            y_mid -= speed_scroll
            y_build -= speed_scroll
            y_over_down -= speed_scroll
            y_over_up -= speed_scroll
            y_anemy -= speed_scroll
            bullet.y -= speed_scroll
            y_const -= speed_scroll
            anemy1.ScrollDown()
                    ### $ ###
        if deaths == 3 or base_healht <= 0:
            anemy1.Respawn()
            while py >= -750 + 5:
                y -= speed_scroll
                py -= speed_scroll
                y_down -= speed_scroll
                y_up -= speed_scroll
                y_mid -= speed_scroll
                y_build -= speed_scroll
                y_over_down -= speed_scroll
                y_over_up -= speed_scroll
                y_anemy -= speed_scroll
                bullet.y -= speed_scroll
                y_const -= speed_scroll
                anemy1.ScrollDown()
            anemy1.health = 100
            if keys[pygame.K_SPACE]:
                run = 1
                deaths = 0
                death_enemy_count = 0
                timer_play=0
                timer_milsec=0
                timer_sec=0
                timer_min=0
                base_healht = 100
                blueT_healht = 100
                x_healthbase_bar_menu = width_map - 169
                x_health_bar_menu = width_map - 200
        else:
            timer_play = pygame.time.get_ticks()
            if timer_play >= 10000:
                timer_milsec += 1
                timer_play = 0 
            if timer_milsec >= 60:
                timer_sec += 1
                timer_milsec = 0
            if timer_sec >= 60:
                timer_min += 1
                timer_sec = 0
            anemy1.mod()

        pygame.display.update()

        drawWindow()