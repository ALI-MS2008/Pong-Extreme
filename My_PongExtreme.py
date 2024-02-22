#To import game
import pygame

#Start pygame
pygame.init()
 
#Screen display
WIDTH, HEIGHT = 1000, 600

#Colors 
BLUE = (0, 0, 255 )
BLACK= (0, 0, 0)
WHITE = (255, 255, 255)
RED =(255, 0, 0)



#ball vaiables
radius = 15
ball_x,ball_y=500,300
ball_vel_x,ball_vel_y = 1, 1


#Paddle variables
paddle_width, paddle_height = 20,120
left_paddle_y = right_paddle_y = 300 - 20
left_paddle_x, right_paddle_x = 20,960
right_paddle_vel = left_paddle_vel = 0

#Picture
image = pygame.image.load('space.jpg')
def Background_sky(image):
    size = pygame.transform.scale(image, (1000,600))
    wn.blit(size, (0,0))



#Main loop and key
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("P O N G --- E X T R E M E")

#Window code
running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    wn.fill((BLACK))

 
#Paddle movement
    left_paddle_y += left_paddle_vel
    right_paddle_y += right_paddle_vel

    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

#Paddle colisions
#Left
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x 
            ball_vel_x *= -1


#Ball movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        ball_x,ball_y=500,300
        ball_vel_x *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius:
        ball_x,ball_y=500,300  
        ball_vel_x,ball_vel_y =1, 1


#Picture
    Background_sky(image)

    


        

    #Objects
    pygame.draw.circle(wn, WHITE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, BLUE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update() 






















pygame.quit()
