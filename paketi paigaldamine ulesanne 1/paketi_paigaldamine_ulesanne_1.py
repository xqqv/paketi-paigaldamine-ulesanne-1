import pygame

# Defineeri värvid
valge = (255, 255, 255)
must = (0, 0, 0)
oranž = (255, 165, 0)
kolane= (255,255,0)
sinine= (0, 0, 255)

# Initsialiseeri pygame
pygame.init()

# Määra akna suurus
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

screen.fill(sinine)

# Määra akna pealkiri
pygame.display.set_caption("Lumemees")

# Joonista esimene pall (pea)
pygame.draw.circle(screen, valge, (150, 80), 35)

# Joonista teine pall (keha)
pygame.draw.circle(screen, valge, (150, 150), 40)

# Joonista kolmas pall (jalad)
pygame.draw.circle(screen, valge, (150, 235), 50)
pygame.draw.circle(screen, valge, (170, 325), 25)
pygame.draw.circle(screen, valge, (180, 325), 25)



# Joonista nina
pygame.draw.polygon(screen, oranž, [(140, 75), (160, 75), (150, 100)])

# Joonista silmad
pygame.draw.circle(screen, must, (135, 65), 5)
pygame.draw.circle(screen, must, (165, 65), 5)

#Joonista paike
pygame.draw.circle(screen, kolane, (50, 25), 70)

# Uuenda ekraani
pygame.display.flip()

# Jätka kuni kasutaja sulgeb akna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Vabasta mälu
pygame.quit()

