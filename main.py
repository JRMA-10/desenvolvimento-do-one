import pygame as pg

#Iniciar pygame
pg.init()

tela = pg.display.set_mode((640, 480))
relogio = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    tela.fill((0, 0, 0))

    pg.display.flip()

    relogio.tick(60)