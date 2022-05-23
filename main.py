import pygame


class Champion:
    x = 100
    y =100
    size = 20
    v = 0.1
    color = (52, 140, 235)

    def go(self, kierunek):
        if kierunek == 1:
            if self.y > self.v:
                self.y -= self.v
        elif kierunek == 2:
            self.x -= self.v


pygame.init()
ludzik = Champion()

width = 800
height = 800
tlo = (0, 0, 0)

okno = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ciekawa Gierka')

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ludzik.go(1)

    okno.fill((255, 255, 255))
    pygame.draw.rect(okno, ludzik.color, (ludzik.x, ludzik.y, ludzik.size, ludzik.size))
    pygame.display.update()
pygame.quit()