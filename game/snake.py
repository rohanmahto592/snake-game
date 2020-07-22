import pygame
import random
import os
pygame.mixer.init()
pygame.mixer.music.load("back2.mp3")
pygame.mixer.music.play()
pygame.init()
## colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,128)
green=(0,200,0)
shadow=(192,192,192)
purple=(102,0,102)
screen_width=900
screen_height=600
game_window=pygame.display.set_mode((screen_width,screen_height))
bgimg=pygame.image.load("snakes.png").convert()
bgimg=pygame.transform.scale(bgimg, (screen_width,screen_height)).convert_alpha()
## title
pygame.display.set_caption("Snake Game")
pygame.display.update()

##game  specific variables
## game loop

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])
def plot_snake(game_window,color,snk_lst,snake_size):
    for x,y in snk_lst:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

    

def gameloop():
    exit_game=False
    game_over=False
    snake_x=45## position of snake in x axis
    snake_y=55## in y axis
    snake_size=10## inital size
    fps=40
    velocity_x=0
    velocity_y=0
    food_x=random.randint(0,screen_width/2)
    food_y=random.randint(0,screen_height/2)
    init_velocity=5
    score=0
    snk_lst=[]
    snk_length=1
    with open("highscore.txt","r") as f:
        hiscore=f.read()
    while not exit_game:
        if game_over:
            with open("highscore.txt","w") as f:
                f.write(str(hiscore))

            game_window.fill(white)
            text_screen("Game Over!",red ,100,200)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                        exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score+=1*10
                        #print(score)
                        # text_screen=["Score:"+str(score*10),red,5,5]
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                snk_length+=5
                if score >int(hiscore):
                    hiscore=score



            game_window.fill(white)
            game_window.blit(bgimg,(0, 0))
            text_screen("Score:"+str(score) +" Hiscore :"+str(hiscore),red,5,5)
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)
            if len(snk_lst)>snk_length:
                del snk_lst[0]
            if head in snk_lst[:-1]:
                game_over=True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                print("game over")
                        #pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])## inital position of the snake
            plot_snake(game_window,purple,snk_lst,snake_size)
            pygame.display.update()
            clock.tick(fps)
    pygame.quit()
    quit()
gameloop()