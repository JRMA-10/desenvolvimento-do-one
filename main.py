import pygame as pg
from random import choice
from time import sleep

#Iniciar pygame
pg.init()

tela = pg.display.set_mode((0, 0), pg.FULLSCREEN)
relogio = pg.time.Clock()


#variáveis
n1 = {'amarelo' : 1, 'verde' : 1, 'azul' : 1, 'vermelho' : 1}
n2 = {'amarelo' : 2, 'verde' : 2, 'azul' : 2, 'vermelho' : 2}
n3 = {'amarelo' : 3, 'verde' : 3, 'azul' : 3, 'vermelho' : 3}
n4 = {'amarelo' : 4, 'verde' : 4, 'azul' : 4, 'vermelho' : 4}




#amarelas
y0 = pg.image.load('imgs/y0.png').convert()
y1 = pg.image.load('imgs/y1.png').convert()
y2 = pg.image.load('imgs/y2.png').convert()
y3 = pg.image.load('imgs/y3.png').convert()
y4 = pg.image.load('imgs/y4.png').convert()
y5 = pg.image.load('imgs/y5.png').convert()
y6 = pg.image.load('imgs/y6.png').convert()
y7 = pg.image.load('imgs/y7.png').convert()
y8 = pg.image.load('imgs/y8.png').convert()
y9 = pg.image.load('imgs/y9.png').convert()
#vermelhas
r0 = pg.image.load('imgs/r0.png').convert()
r1 = pg.image.load('imgs/r1.png').convert()
r2 = pg.image.load('imgs/r2.png').convert()
r3 = pg.image.load('imgs/r3.png').convert()
r4 = pg.image.load('imgs/r4.png').convert()
r5 = pg.image.load('imgs/r5.png').convert()
r6 = pg.image.load('imgs/r6.png').convert()
r7 = pg.image.load('imgs/r7.png').convert()
r8 = pg.image.load('imgs/r8.png').convert()
r9 = pg.image.load('imgs/r9.png').convert()
#verdes 
g0 = pg.image.load('imgs/g0.png').convert()
g1 = pg.image.load('imgs/g1.png').convert()
g2 = pg.image.load('imgs/g2.png').convert()
g3 = pg.image.load('imgs/g3.png').convert()
g4 = pg.image.load('imgs/g4.png').convert()
g5 = pg.image.load('imgs/g5.png').convert()
g6 = pg.image.load('imgs/g6.png').convert()
g7 = pg.image.load('imgs/g7.png').convert()
g8 = pg.image.load('imgs/g8.png').convert()
g9 = pg.image.load('imgs/g9.png').convert()

#azuis
b0 = pg.image.load('imgs/b0.png').convert()
b1 = pg.image.load('imgs/b1.png').convert()
b2 = pg.image.load('imgs/b2.png').convert()
b3 = pg.image.load('imgs/b3.png').convert()
b4 = pg.image.load('imgs/b4.png').convert()
b5 = pg.image.load('imgs/b5.png').convert()
b6 = pg.image.load('imgs/b6.png').convert()
b7 = pg.image.load('imgs/b7.png').convert()
b8 = pg.image.load('imgs/b8.png').convert()
b9 = pg.image.load('imgs/b9.png').convert()

#+4
mais_4 = pg.image.load('imgs/+4.png').convert()

#-4
doe_4 = pg.image.load('imgs/-4.png').convert()

#+2 
b_mais_2 = pg.image.load('imgs/b+2.png').convert()
r_mais_2 = pg.image.load('imgs/r+2.png').convert()
y_mais_2 = pg.image.load('imgs/y+2.png').convert()
g_mais_2 = pg.image.load('imgs/g+2.png').convert()

#comunista
comunista = pg.image.load('imgs/comunista.png').convert()

#bloqueios
b_bloqueio = pg.image.load('imgs/bbloqueio.png').convert()
r_bloqueio = pg.image.load('imgs/rbloqueio.png').convert()
y_bloqueio = pg.image.load('imgs/ybloqueio.png').convert()
g_bloqueio = pg.image.load('imgs/gbloqueio.png').convert()

#reverse 
b_reverse = pg.image.load('imgs/breverse.png').convert()
r_reverse = pg.image.load('imgs/rreverse.png').convert()
y_reverse = pg.image.load('imgs/yreverse.png').convert()
g_reverse = pg.image.load('imgs/greverse.png').convert()

#tornado 
tornado = pg.image.load('imgs/tornado.png').convert()





#bolo de cartas
bolo = []

#Adicionando cartas comuns ao bolo
cartas_comuns = [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9,
          b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,
          g0, g1, g2, g3, g4, g5, g6, g7, g8, g9,
          r0, r1, r2, r3, r4, r5, r6, r7, r8,] * 2
for item in cartas_comuns:
    bolo.append(item)

#Adicionando cartas +4 ao bolo
cartas_mais_4 = [mais_4] * 4
for item in cartas_mais_4:
    bolo.append(item)

#Adicionandp cartas -4 ao bolo
cartas_doe_4 = [doe_4] * 4
for item in cartas_doe_4:
    bolo.append(item)

#Adicionando cartas +2 ao bolo
cartas_mais_2 = [b_mais_2, r_mais_2, y_mais_2, g_mais_2] * 2
for item in cartas_mais_2:
    bolo.append(item)

#Adicionando cartas bloqueio ao bolo
cartas_bloqueio = [b_bloqueio, r_bloqueio, y_bloqueio, g_bloqueio] * 2
for item in cartas_bloqueio:    
    bolo.append(item)

#Adicionando cartas reverse ao bolo
cartas_reverse = [b_reverse, r_reverse, y_reverse, g_reverse]
for item in cartas_reverse:
    bolo.append(item)

#Adicionando carta comunista ao bolo
bolo.append(comunista)

#Adicionado carta tornado ao bolo
bolo.append(tornado)





while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    #carta inicial
    carta_inicial = choice(bolo)
    bolo.remove(carta_inicial)
    carta_inicial = pg.transform.scale(carta_inicial, (400, 600))
    
    #cartas dos players
    def escolhendo_cartas(a):
        for i in range(7):
            carta = choice(bolo)
            bolo.remove(carta)
            carta = pg.transform.scale(carta, (100, 200))
            a.append(carta)

    #jogador
    cartas_jogador = []
    escolhendo_cartas(cartas_jogador)
        
    #computador
    cartas_computador = []
    escolhendo_cartas(cartas_computador)

    #elementos na tela
    tela.fill((255, 0, 0))

    tela.blit(carta_inicial, (tela.get_width()//2 - carta_inicial.get_width()//2, tela.get_height()//2 - carta_inicial.get_height()//2))

    #cartas do jogador na tela
    for c in range(len(cartas_jogador)):
        tela.blit(cartas_jogador[c], (tela.get_width() // 2 - cartas_jogador[c].get_width() // 2 - 150*c, tela.get_height() - cartas_jogador[c].get_height() - 20))
    

    pg.display.flip()
    sleep(5)
    relogio.tick(60)