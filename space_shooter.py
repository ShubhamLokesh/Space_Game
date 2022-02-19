import time
import pygame
from pygame.font import Font
from pygame.locals import *
from pygame.transform import rotate
FPS=30
Screen_width=800
Screen_height=400
Spaceship_height=40
Spaceship_width=40
White=(255,255,255)
RED=(255,0,0)
YELLOW=(255,255,0)
black=(0,0,0)
speed= 10
ship_speed=5
MAX_BULLETS=3
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
class SPACESHIP :
    def __init__(self,screen,Starting_pos,ship_color):
        self.screen=screen
        self.images=pygame.image.load(fr"spaceship_{ship_color}.png").convert()
        self.images=pygame.transform.scale(self.images,(Spaceship_width,Spaceship_height))
        if ship_color=="yellow":
            self.images=pygame.transform.rotate(self.images,90)
        else:
            self.images=pygame.transform.rotate(self.images,90)

        self.x=Starting_pos
        self.y=200

    def yellow_spaceship_movement(self,keys_pressed, yellow,rotation):

        if rotation==0 or rotation==360:
            ke=[pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d]

        elif rotation==90:
            ke=[pygame.K_d,pygame.K_w,pygame.K_a,pygame.K_s]
 
        elif rotation==180:
            ke=[pygame.K_s,pygame.K_d,pygame.K_w,pygame.K_a]

        elif rotation==270:
            ke=[pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_w]

        if keys_pressed[ke[0]] :  # RIGHT
            if yellow.x>=Screen_width-Spaceship_width:pass
            else:
                yellow.x += ship_speed
        if keys_pressed[ke[1]] :  #up
            if yellow.y<Spaceship_height+10:pass
            else:  
                yellow.y -= ship_speed
        if keys_pressed[ke[2]] :  # LEFT
            if yellow.x<0:pass
            else:
                yellow.x -= ship_speed
        if keys_pressed[ke[3]]:  # DOWN
            if yellow.y>=Screen_height-Spaceship_height:pass
            else:
                yellow.y += ship_speed

    def red_spaceship_movement(self,keys_pressed, red,rotation):
        if rotation==0 or rotation==360:
            ke=[pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT]

        elif rotation==90:
            ke=[pygame.K_RIGHT,pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN]
 
        elif rotation==180:
            ke=[pygame.K_DOWN,pygame.K_RIGHT,pygame.K_UP,pygame.K_LEFT]

        elif rotation==270:
            ke=[pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_UP]

        
        if keys_pressed[ke[0]]  :# RIGHT
            if red.x>=Screen_width-Spaceship_width:pass
            else:
                red.x += ship_speed
        if keys_pressed[ke[1]]   :# UP
            if red.y<=Spaceship_height+10:pass
            else:
                red.y -= ship_speed
        if keys_pressed[ke[2]] :#left
            if red.x<0:pass
            else:
                red.x -= ship_speed
        if keys_pressed[ke[3]]  : # DOWN
            if red.y>=Screen_height-Spaceship_height:pass
            else:
                red.y += ship_speed    

class Bullet:
    def handel_bullet(self,right,left,up,down,ship,HIT):

        for bullet in right:
            bullet.x +=speed
            if ship.colliderect(bullet):
                pygame.event.post(pygame.event.Event(HIT))
                right.remove(bullet)

            elif bullet.x >Screen_width:
                right.remove(bullet)

        for bullet in left:
            bullet.x -=speed
            if ship.colliderect(bullet):
                pygame.event.post(pygame.event.Event(HIT))
                left.remove(bullet)
            elif bullet.x < 0:
                 left.remove(bullet)   

        for bullet in up:
            bullet.y -=speed
            if ship.colliderect(bullet):
                pygame.event.post(pygame.event.Event(HIT))
                up.remove(bullet)
            elif bullet.y < 0:
                 up.remove(bullet)  

        for bullet in down:
            bullet.y +=speed
            if ship.colliderect(bullet):
                pygame.event.post(pygame.event.Event(HIT))
                down.remove(bullet)
            elif bullet.y > Screen_height:
                 down.remove(bullet) 
    
class GAME:
    def __init__(self):
        pygame.init()
        self.Font = pygame.font.SysFont('arial', 30)
        self.MainFont=pygame.font.SysFont("arial",50)
        self.smallFont=pygame.font.SysFont("arial",15)
        pygame.display.set_caption("SPACE WAR")
        self.screen=pygame.display.set_mode((Screen_width,Screen_height))
        self.ship_red=SPACESHIP(self.screen,0,"red")
        self.ship_yellow=SPACESHIP(self.screen,760,"yellow")
        self.bullet=Bullet()
     
        self.startmenu()

    def var(self):
        self.red = pygame.Rect(700, 300, Spaceship_width, Spaceship_height)
        self.yellow = pygame.Rect(100, 300, Spaceship_width, Spaceship_height)
        self.red_hp=5
        self.red_bullet=[]
        self.r_right=[]
        self.r_left=[]
        self.r_up=[]
        self.r_down=[]
        self.y_right=[]
        self.y_left=[]
        self.y_up=[]
        self.y_down=[]
        self.yellow_hp=5
        self.rotate_yellow=0
        self.rotate_red=180

    def startmenu(self):
        flag=0
        while True:
            self.screen.fill(black)
            menu=self.MainFont.render("MAIN MENU",True,White)
               
            if flag==0:
                start=self.Font.render("START GAME",True,RED)
                control=self.Font.render("CONTROL",True,White)
                quit=self.Font.render(" QUIT",True,White)
            
            elif flag==1:
                start=self.Font.render("START GAME",True,White)
                control=self.Font.render("CONTROL",True,RED)
                quit=self.Font.render(" QUIT",True,White)
            
            elif flag==2:
                start=self.Font.render("START GAME",True,White)
                control=self.Font.render("CONTROL",True,White)
                quit=self.Font.render(" QUIT",True,RED)

            self.screen.blit(menu,(Screen_width//2-120,Screen_height//2-150))
            self.screen.blit(start,(Screen_width//2-100,Screen_height//2-30))
            self.screen.blit(control,(Screen_width//2-100,Screen_height//2))
            self.screen.blit(quit,(Screen_width//2-100,Screen_height//2+30))
            
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        pygame.quit()
                    elif event.key==K_UP:
                        if flag>0 and flag<=2:
                            flag-=1
                    elif event.key==K_DOWN:
                        if flag>=0 and flag<2:
                            flag+=1
                    elif event.key==K_RETURN:
                        if flag==0:
                            self.var()
                            self.run()
                        elif flag==1:
                            self.control()
                            
                        elif flag==2:
                            pygame.quit()
                               
                pygame.display.update() 
            
    def control(self):

        while True:
            self.screen.fill(black)
            back=self.Font.render("BACK",True,RED)
            ship=self.smallFont.render("YELLOW SHIP MOVEMENT           RED SHIP MOVEMENT",True,White)
            UPWARDS=self.smallFont.render("FORWARDS                     \t             W                                         UPWARDS ARROW ",True,White)
            DOWNWARDS=self.smallFont.render("BACKWARDS              \t             S                                           DOWNWARDS ARROW ",True,White)
            RIGHRWARDS=self.smallFont.render("RIGHRWARDS              \t             D                                          RIGHRWARDS ARROW",True,White)
            LEFTWARDS=self.smallFont.render("LEFTWARDS                 \t             A                                           LEFTWARDS ARROW",True,White)
            SHOOTING=self.smallFont.render("SHOOTING                     \t             LCTRL                                RCTRL",True,White)
            LEFTROTATION=self.smallFont.render("LEFTROTATION            \t             Q                                           PAGEUP",True,White)
            RIGHTTROTATION=self.smallFont.render("RIGHTTROTATION         \t             R                                           PAGEDON",True,White)
            self.screen.blit(back,(0,0))
            self.screen.blit(ship,(Screen_width//2-160,Screen_height//2-100))
            self.screen.blit(UPWARDS,(Screen_width//2-260,Screen_height//2-30))
            self.screen.blit(DOWNWARDS,(Screen_width//2-260,Screen_height//2))
            self.screen.blit(RIGHRWARDS,(Screen_width//2-260,Screen_height//2+30))
            self.screen.blit(LEFTWARDS,(Screen_width//2-260,Screen_height//2+60))
            self.screen.blit(SHOOTING,(Screen_width//2-260,Screen_height//2+90))
            self.screen.blit(LEFTROTATION,(Screen_width//2-260,Screen_height//2+120))
            self.screen.blit(RIGHTTROTATION,(Screen_width//2-260,Screen_height//2+150))

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type==KEYDOWN:
                    if event.key==K_RETURN:
                        self.startmenu()

            pygame.display.flip()
        
    def rotate(image ,rot):
        image=pygame.transform.rotate(image,rot+90)
        return image

    def display(self):
        self.screen.fill(black)
        red_health_text = self.Font.render("Health: " + str(self.red_hp), 1, White)
        yellow_health_text = self.Font.render("Health: " + str(self.yellow_hp), 1, White)
        self.screen.blit(red_health_text, (Screen_width - red_health_text.get_width() -10, 10))
        self.screen.blit(yellow_health_text, (10, 10))        
        self.screen.blit(rotate(self.ship_red.images,self.rotate_red),(self.red.x,self.red.y))
        self.screen.blit(rotate(self.ship_yellow.images,self.rotate_yellow),(self.yellow.x,self.yellow.y))
        self.Y_diection=[self.y_right,self.y_left,self.y_up,self.y_down]
        for i in self.Y_diection:
            for bullet in i:
                pygame.draw.rect(self.screen, YELLOW, bullet)
            pygame.display.flip()

        self.R_diection=[self.r_right,self.r_left,self.r_up,self.r_down]
        for i in self.R_diection:
            for bullet in i:
                pygame.draw.rect(self.screen, RED, bullet)
            pygame.display.flip()
   
    def draw_winner(self,text):
        self.screen.fill(black)
        draw_text =self.Font.render(text, 1, White)
        restart=self.smallFont.render("Press Enter to RESTART GAME",True,White)
        self.screen.blit(draw_text, (Screen_width/2 - draw_text.get_width() /
                         2, Screen_height/2 - draw_text.get_height()/2))
        self.screen.blit(restart, (0,0,))
        pygame.display.update()
        pygame.time.delay(1000)
      
    def run(self):
        clock=pygame.time.Clock()
        running=True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False 
                    if event.key==K_q:
                        self.rotate_yellow +=90
                        if self.rotate_yellow==360 or self.rotate_yellow==0:
                            self.rotate_yellow=0
                    if event.key==K_e:
                        if self.rotate_yellow==0 or self.rotate_yellow==360:
                            self.rotate_yellow=360
                        self.rotate_yellow-=90    
                    if event.key == K_LCTRL and len(self.y_right) +len(self.y_left)+len(self.y_down)+len(self.y_up) < MAX_BULLETS:
                        if self.rotate_yellow==0 or self.rotate_yellow==360:
                            bullet = pygame.Rect(
                                self.yellow.x + self.yellow.width, self.yellow.y + self.yellow.height//2 - 2, 10, 5)
                            self.y_right.append(bullet)
                        elif self.rotate_yellow==180:
                            bullet = pygame.Rect(
                                self.yellow.x , self.yellow.y + self.yellow.height//2 - 2, 10, 5)
                            self.y_left.append(bullet)
                        elif self.rotate_yellow==90:
                            bullet = pygame.Rect(
                                self.yellow.x + self.yellow.width//2-2, self.yellow.y , 5, 10)
                            self.y_up.append(bullet)    
                        elif self.rotate_yellow==270:
                            bullet = pygame.Rect(
                                self.yellow.x + self.yellow.width//2-2, self.yellow.y +self.yellow.height, 5, 10)
                            self.y_down.append(bullet)
                  

                    if event.key==K_PAGEUP:
                        self.rotate_red +=90
                        if self.rotate_red==360 or self.rotate_red==0:
                            self.rotate_red=0
                    if event.key==K_PAGEDOWN:
                        if self.rotate_red==0 or self.rotate_red==360:
                            self.rotate_red=360
                        self.rotate_red-=90   

                    if event.key == K_RCTRL and len(self.r_right) +len(self.r_left)+len(self.r_down)+len(self.r_up) < MAX_BULLETS:
                        if self.rotate_red==0 or self.rotate_red==360:
                            bullet = pygame.Rect(
                                self.red.x + self.red.width, self.red.y + self.red.height//2 - 2, 10, 5)
                            self.r_right.append(bullet)
                        elif self.rotate_red==180:
                            bullet = pygame.Rect(
                                self.red.x , self.red.y + self.red.height//2 - 2, 10, 5)
                            self.r_left.append(bullet)
                        elif self.rotate_red==90:
                            bullet = pygame.Rect(
                                self.red.x + self.red.width//2-2, self.red.y , 5, 10)
                            self.r_up.append(bullet)    
                        elif self.rotate_red==270:
                            bullet = pygame.Rect(
                                self.red.x + self.red.width//2-2, self.red.y +self.red.height, 5, 10)
                            self.r_down.append(bullet)
                  
                    
                if event.type==QUIT:
                    running=False
             

                if event.type == RED_HIT:
                    self.red_hp -= 1
    

                if event.type == YELLOW_HIT:
                    self.yellow_hp -= 1
            
            key_pressed=pygame.key.get_pressed()
            self.ship_yellow.yellow_spaceship_movement(key_pressed,self.yellow,self.rotate_yellow)
            self.ship_red.red_spaceship_movement(key_pressed,self.red,self.rotate_red)
            
            winner_text = ""
            if self.red_hp == 0:
                winner_text = "Yellow Wins!"
            
            if self.yellow_hp == 0:
                winner_text = "Red Wins!"

            if winner_text != "":
                self.draw_winner(winner_text)
                 
                break
            self.bullet.handel_bullet(self.y_right,self.y_left,self.y_up,self.y_down,self.red,RED_HIT)
            self.bullet.handel_bullet(self.r_right,self.r_left,self.r_up,self.r_down,self.yellow,YELLOW_HIT)
            self.display()     
                
if __name__=='__main__':

    game=GAME()
    game.run()
       