import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

paddle = pygame.Rect(175, 350, 50, 10)
ball = pygame.Rect(200, 50, 5, 5)

ball_y_change = 1

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    if ball.y < 0:
        ball_y_change = 1
    
    ball.y += ball_y_change
    
    pygame.draw.rect(screen, (100, 100, 100), paddle)
    pygame.draw.rect(screen, (0, 0, 0), ball)
    
    if ball.colliderect(paddle):
        ball_y_change = -1
    
    pygame.display.update()