import pygame as pg
from random import randint, choice, shuffle
import time

# INICIALIZAÇÃO
pg.init()
tela = pg.display.set_mode((0, 0), pg.FULLSCREEN)
LARGURA, ALTURA = tela.get_size()
relogio = pg.time.Clock()

fonte = pg.font.Font(None, 26)
fonte_grande = pg.font.Font(None, 36)

# CORES
BRANCO = (255, 255, 255)
AMARELO = (255, 255, 0)
VERDE = (20, 120, 20)
VERMELHO = (200, 0, 0)

# CARTAS
def carregar_cartas():
    cartas = []
    cores = ["y", "r", "g", "b"]

    for cor in cores:
        for num in range(10):
            cartas.append({
                "tipo": "normal",
                "cor": cor,
                "numero": num,
                "imagem": pg.image.load(f"imgs/{cor}{num}.png").convert_alpha()
            })

    for cor in cores:
        cartas.append({"tipo": "+2", 
                       "cor": cor, 
                       "numero": None,
                       "imagem": pg.image.load(f"imgs/{cor}+2.png").convert_alpha()})
        cartas.append({"tipo": "bloqueio", 
                       "cor": cor, 
                       "numero": None,
                       "imagem": pg.image.load(f"imgs/{cor}bloqueio.png").convert_alpha()})
        cartas.append({"tipo": "reverse", 
                       "cor": cor, 
                       "numero": None,
                       "imagem": pg.image.load(f"imgs/{cor}reverse.png").convert_alpha()})

    cartas.append({"tipo": "+4", 
                   "cor": None, 
                   "numero": None,
                   "imagem": pg.image.load("imgs/+4.png").convert_alpha()})
    cartas.append({"tipo": "+10", 
                   "cor": None, 
                   "numero": None,
                   "imagem": pg.image.load("imgs/+10.png").convert_alpha()})
    cartas.append({"tipo": "-4", 
                   "cor": None, 
                   "numero": None,
                   "imagem": pg.image.load("imgs/-4.png").convert_alpha()})
    cartas.append({"tipo": "tornado", 
                   "cor": None, 
                   "numero": None,
                   "imagem": pg.image.load("imgs/tornado.png").convert_alpha()})

    return cartas

cartas = carregar_cartas()
shuffle(cartas)


#Bolo 
bolo = []


#Funções principais
def sorteando():
    sorteio = randint(0, len(cartas)-1)
    return sorteio

#cartas dos players
def distribuindo(mao):
    for i in range(7):
        num_carta_escolhida = sorteando()
        carta = cartas[num_carta_escolhida]
        cartas.remove(cartas[num_carta_escolhida])
        mao.append(carta)
    

def posso_jogar():
    contador = 0
    for carta in cartas_computador:
        if carta['cor'] == ultima['cor'] or carta['numero'] == ultima['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            contador += 1
    return contador

def puxar_cartas(vez_de, lista_de_cartas): 
    num = posso_jogar()
    if num == 0:
        print(f'{vez_de} não tem cartas jogáveis!')
        lista_de_cartas.append(cartas[0])

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
    
    if ultima['cor'] == cartas_jogador[carta_selecionada]['cor'] or ultima['numero'] == cartas_jogador[carta_selecionada]['numero'] or cartas_jogador[carta_selecionada]['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
        print('Jogada válida!')
        bolo.append(cartas_jogador[carta_selecionada])
        cartas_jogador.pop(carta_selecionada)

def jogada_computador():
    puxar_cartas('Computador', cartas_computador)
    possiveis_jogadas = []
    for carta in cartas_computador:
        if carta['cor'] == ultima['cor'] or carta['numero'] == ultima['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            possiveis_jogadas.append(carta)
    escolha = randint(0, len(possiveis_jogadas) - 1)
    jogada_final = possiveis_jogadas[escolha]
    bolo.append(jogada_final)
    cartas.remove(jogada_final)

#carta inicial do bolo
num_carta_inicial = sorteando()
carta_inicial = cartas[num_carta_inicial]
cartas.remove(cartas[num_carta_inicial])
bolo.append(carta_inicial)

#Recuperando a última carta do bolo
ultima = bolo[-1]

#jogador
cartas_jogador = []
quantidade_cartas_jogador = len(cartas_jogador)
distribuindo(cartas_jogador)
    
#computador
cartas_computador = []
quantidade_cartas_computador = len(cartas_computador)
distribuindo(cartas_computador)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    #transformando as cartas
    last_card_image = bolo[-1]['imagem']
    last_card_image = pg.transform.scale(last_card_image, (400, 600))

    tela.blit(last_card_image, (tela.get_width()//2 - last_card_image.get_width()//2, tela.get_height()//2 - last_card_image.get_height()//2))

    #elementos na tela
    tela.fill(VERMELHO)

    

    #cartas do jogador na tela
    for c in range(len(cartas_jogador)):
        tamanho_carta = (100, 150)
        cartas_jogador[c] = pg.transform.scale(cartas_jogador[c]['imagem'], tamanho_carta)
        tela.blit(cartas_jogador[c], (tela.get_width() // 2 - cartas_jogador[c].get_width() // 2 - 150*c, tela.get_height() - cartas_jogador[c].get_height() - 20))

    pg.display.flip()
    
    relogio.tick(1)