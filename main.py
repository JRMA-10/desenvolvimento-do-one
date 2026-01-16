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

#Bolo 
bolo = []

#carta inicial
def sorteando():
    sorteio = randint(0, len(cartas)-1)
    return sorteio

#Funções principais

#cartas dos players
def escolhendo_cartas(a):
    for i in range(7):
        num_carta_escolhida = sorteando()
        carta = cartas[num_carta_escolhida]
        cartas.remove(cartas[num_carta_escolhida])
        a.append(carta)
    

def posso_jogar():
    contador = 0
    for carta in cartas_computador:
        if carta['cor'] == ultima_carta_do_bolo['cor'] or carta['numero'] == ultima_carta_do_bolo['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            contador += 1
    return contador

def puxar_cartas(vez_de, lista_de_cartas): 
    num = posso_jogar()
    if num == 0:
        print(f'{vez_de} não tem cartas jogáveis!')
        lista_de_cartas.append(cartas[0])
    else:
        jogadas_do_jogador()

#Recuperando a última carta do bolo
ultima_carta_do_bolo = bolo[-1]

def jogadas_do_jogador():
    puxar_cartas('Player', cartas_jogador)
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
    
    if bolo[ultima_carta_do_bolo]['cor'] == cartas_jogador[carta_selecionada]['cor'] or bolo[ultima_carta_do_bolo]['numero'] == cartas_jogador[carta_selecionada]['numero'] or cartas_jogador[carta_selecionada]['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
        print('Jogada válida!')
        bolo.append(cartas_jogador[carta_selecionada])
        cartas_jogador.pop(carta_selecionada)

def jogada_computador():
    puxar_cartas('Computador', cartas_computador)
    possiveis_jogadas = []
    for carta in cartas_computador:
        if carta['cor'] == ultima_carta_do_bolo['cor'] or carta['numero'] == ultima_carta_do_bolo['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            possiveis_jogadas.append(carta)
    escolha = randint(0, len(possiveis_jogadas) - 1)
    jogada_final = possiveis_jogadas[escolha]
    bolo.append(jogada_final)
    cartas.remove(jogada_final)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    num_carta_inicial = sorteando()
    carta_inicial = cartas[num_carta_inicial]
    cartas.remove(cartas[num_carta_inicial])
    bolo.append(carta_inicial)


    #jogador
    cartas_jogador = []
    quantidade_cartas_jogador = len(cartas_jogador)
    escolhendo_cartas(cartas_jogador)
        
    #computador
    cartas_computador = []
    quantidade_cartas_computador = len(cartas_computador)
    escolhendo_cartas(cartas_computador)
    
    #transformando as cartas
    last_card_image = bolo[-1]['imagem']
    last_card_image = pg.transform.scale(last_card_image, (400, 600))

    #elementos na tela
    tela.fill((255, 0, 0))

    tela.blit(last_card_image, (tela.get_width()//2 - last_card_image.get_width()//2, tela.get_height()//2 - last_card_image.get_height()//2))

    #cartas do jogador na tela
    for c in range(len(cartas_jogador)):
        tamanho_carta = (100, 150)
        cartas_jogador[c] = pg.transform.scale(cartas_jogador[c]['imagem'], tamanho_carta)
        tela.blit(cartas_jogador[c], (tela.get_width() // 2 - cartas_jogador[c].get_width() // 2 - 150*c, tela.get_height() - cartas_jogador[c].get_height() - 20))

    pg.display.flip()
    
    relogio.tick(1)