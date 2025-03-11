# Asegúrate de tener instalado pygame usando: pip install pygame
import pygame

pygame.init()

#colores

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

#tamaño de la pantalla
size = width, height = 400, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Solo Un Jueguito De Una Bola Rebotando")

#posicion de la bola
x = 200 
y = 200


#velociad de la bola
velocidad = [4, 4]
bola = pygame.Rect(x, y, 50, 50)
platform = pygame.Rect(150, 500, 100, 20)

cub = []
cub_width = 50
cub_height = 20
for i in range(8):  # 8 cubitos por fila
    cub.append(pygame.Rect(i * cub_width, 0, cub_width, cub_height))
    
relog = pygame.time.Clock()

hola = True
while hola:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hola = False
    
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and platform.left >=0:
        platform.x -= 5
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and platform.right <= width: 
        platform.x += 5  
            

    bola.x += velocidad[0]
    bola.y += velocidad[1]

    if bola.left <= 0 or bola.right >= width:   
        velocidad[0] = -velocidad[0]

    if bola.top <= 0:
        velocidad[1] = -velocidad[1]
    elif bola.bottom >= height:
        hola = False
        
        
    if bola.colliderect(platform) and velocidad[1] > 0:
        velocidad[1] = -velocidad[1]
        
        
    for c in cub:
        if bola.colliderect(c):
            velocidad[1] = -velocidad[1]
            cub.remove(c)
            break

    screen.fill(black)

    pygame.draw.circle(screen, white, (bola.x + bola.width // 2, bola.y + bola.height // 2), 25)
    pygame.draw.rect(screen, red, platform)
    
    for c in cub:
        pygame.draw.rect(screen, green, c)

    pygame.display.flip()
    relog.tick(60)
