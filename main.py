import pygame as pg
import time
import random
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 0]
PURPLE = [128, 0, 128]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

def draw_text(screen, text):
    font = pg.font.Font(None, 30)
    text = font.render(text, True, BLACK)
    screen.blit(text, [30, 50])

def draw():
    pg.init()

    size = [900, 600]
    screen = pg.display.set_mode(size)

    pg.display.set_caption("!!!GAMES!!!")

    done = False
    score = 0

    while done == False:

        screen.fill(WHITE)

        rand_door = random.randint(1,3)
        door_surf = pg.image.load(f'source/doors{str(rand_door)}.jpg')
        #размещаем объект в окне (два да)
        door_rect = door_surf.get_rect(bottomright=(900, 500))
        screen.blit(door_surf, door_rect)

        draw_text(screen, f'Ты! Да ты! Выберай дверь! + {str(score)}')

        pg.display.update()
        ghost_door = random.randint(1, 3)
        #ghost_door = 1

        ev = False

        buttons = set()

        buttons.add(pg.K_1)
        buttons.add(pg.K_2)
        buttons.add(pg.K_3)

        while ev == False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    ev = True
                    done = True
                elif event.type == pg.KEYDOWN:
                    if event.key in buttons:
                        ev = True
                    if (event.key == pg.K_1)  and (ghost_door == 1) \
                        or (event.key == pg.K_2) and (ghost_door == 2) \
                        or (event.key == pg.K_3)  and (ghost_door == 3):
                        screen.fill(WHITE)
                        draw_text(screen, "Ты нашёл привидение! Ты лох!")
                        ghost_surf = pg.image.load('source/ghost1.jpg')
                        ghost_rect = ghost_surf.get_rect(bottomright=(900, 600))
                        screen.blit(ghost_surf, ghost_rect)
                        pg.display.update()
                        done = True
                        time.sleep(3)
                    else:
                        score += 1

def main():
    draw()

if __name__ =='__main__':
    main()