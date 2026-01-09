import pygame as pg
from random import choice, randint
from time import sleep

#Iniciar pygame
pg.init()

tela = pg.display.set_mode((0, 0), pg.FULLSCREEN)
relogio = pg.time.Clock()

#Fontes
fonte = pg.font.Font(None, 30)

#variáveis
cartas = []

#cartas normais
cores = ["y", "r", "g", "b"]

for cor in cores:
    for numero in range(10):
        cartas.append({
            "tipo": "normal",
            "cor": cor,
            "numero": numero,
            "imagem": pg.image.load(f'imgs/{cor}{numero}.png').convert()
        })
#cartas especiais
cartas.append({
    "tipo": "+4",
    "cor": None,
    "numero": None,
    "imagem": pg.image.load('imgs/+4.png').convert()
})
cartas.append({
    "tipo": "-4",
    "cor": None,
    "numero": None,
    "imagem": pg.image.load('imgs/-4.png').convert()
})
for cor in cores:
    cartas.append({
        "tipo": "+2",
        "cor": cor,
        "numero": None,
        "imagem": pg.image.load(f'imgs/{cor}+2.png').convert()
    })
    cartas.append({
        "tipo": "bloqueio",
        "cor": cor,
        "numero": None,
        "imagem": pg.image.load(f'imgs/{cor}bloqueio.png').convert()
    })
    cartas.append({
        "tipo": "reverse",
        "cor": cor,
        "numero": None,
        "imagem": pg.image.load(f'imgs/{cor}reverse.png').convert()
    })
cartas.append({
    "tipo": "comunista",
    "cor": None,
    "numero": None,
    "imagem": pg.image.load('imgs/comunista.png').convert()
})
cartas.append({
    "tipo": "tornado",
    "cor": None,
    "numero": None,
    "imagem": pg.image.load('imgs/tornado.png').convert()
})

'''''
Carregar imagens; 
Identidade das cartas; 
Cartas iniciais e dos players;
Criar o bolo principal; 
loop das jogadas dos players e do computador cuja condição é: while cartas_jogador == 0 or cartas_computador == 0; 
    vez do jogador()
    if cor_carta_escolhida == cor_carta_inicial or numero_carta_escolhida == numero_carta_bolo:
        jogar_carta()
    else:
        comprar_carta()
        vez do computador()
'''

'''
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
'''



'''
#bolo de cartas
bolo = []

#Adicionando cartas comuns ao bolo
cartas_comuns = [y0, y1, y2, y3, y4, y5, y6, y7, y8, y9,
          b0, b1, b2, b3, b4, b5, b6, b7, b8, b9,
          g0, g1, g2, g3, g4, g5, g6, g7, g8, g9,
          r0, r1, r2, r3, r4, r5, r6, r7, r8, r9] * 2
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
'''




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
    
    #Bolo 
    bolo = []

    #carta inicial
    def sorteando():
        sorteio = randint(0, len(cartas)-1)
        return sorteio

    num_carta_inicial = sorteando()
    carta_inicial = cartas[num_carta_inicial]["imagem"]
    cartas.remove(cartas[num_carta_inicial])
    carta_inicial = pg.transform.scale(carta_inicial, (400, 600))
    bolo.append(carta_inicial)

    #embaralhando o bolo

    #cartas dos players
    def escolhendo_cartas(a):
        for i in range(7):
            sorteando()
            num_carta_escolhida = sorteando()
            carta = cartas[num_carta_escolhida]["imagem"]
            cartas.remove(cartas[num_carta_escolhida])
            carta = pg.transform.scale(carta, (100, 200))
            a.append(carta)

    #jogador
    cartas_jogador = []
    quantidade_cartas_jogador = len(cartas_jogador)
    escolhendo_cartas(cartas_jogador)
        
    #computador
    cartas_computador = []
    quantidade_cartas_computador = len(cartas_computador)
    escolhendo_cartas(cartas_computador)

    def jogadas_do_jogador():
        carta_selecionada = 0
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_0:
                    carta_selecionada = 0
                if event.key == pg.K_1:
                    carta_selecionada = 1
                if event.key == pg.K_2:
                    carta_selecionada = 2
                if event.key == pg.K_3:
                    carta_selecionada = 3
                if event.key == pg.K_4:
                    carta_selecionada = 4
                if event.key == pg.K_5:
                    carta_selecionada = 5
                if event.key == pg.K_6:
                    carta_selecionada = 6
                if event.key == pg.K_o:
                    print('Jogador só tem uma carta!')
        
        if bolo[-1]['cor'] == cartas_jogador[carta_selecionada]['cor'] or bolo[-1]['numero'] == cartas_jogador[carta_selecionada]['numero'] or cartas_jogador[carta_selecionada]['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            print('Jogada válida!')
            bolo.append(cartas_jogador[carta_selecionada])
            cartas_jogador.pop(carta_selecionada)
        
    #Quem começa?
    while quantidade_cartas_jogador > 0 and quantidade_cartas_computador > 0:
        primeira_jogada = choice(['jogador', 'computador'])
        print(f'Quem começa: {primeira_jogada}')
        
            
    

    #elementos na tela
    tela.fill((255, 0, 0))

    tela.blit(bolo[-1], (tela.get_width()//2 - bolo[-1].get_width()//2, tela.get_height()//2 - bolo[-1].get_height()//2))

    #cartas do jogador na tela
    for c in range(len(cartas_jogador)):
        tela.blit(cartas_jogador[c], (tela.get_width() // 2 - cartas_jogador[c].get_width() // 2 - 150*c, tela.get_height() - cartas_jogador[c].get_height() - 20))
    
    

    pg.display.flip()
    
    relogio.tick(1)