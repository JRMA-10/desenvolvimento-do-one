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
PRETO = (0, 0, 0)

#Contadores 
tempo_inicio_jogo = pg.time.get_ticks()
tempo_inicio_turno = pg.time.get_ticks()
tempo_limite_turno = 10000

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
    

def possiveis_jogadas(mao):
    contador = 0
    for carta in mao:
        if carta['cor'] == ultima['cor'] or carta['numero'] == ultima['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            contador += 1
    return contador

def puxar_cartas_mais(lista_de_cartas):
    if ultima['tipo'] == '+2':
        for i in range(2):
            lista_de_cartas.append(cartas[0])
            cartas.pop(0)
    elif ultima['tipo'] == '+4':
        for i in range(4):
            lista_de_cartas.append(cartas[0])
            cartas.pop(0)
    elif ultima['tipo'] == '+10':
        for i in range(10):
            lista_de_cartas.append(cartas[0])
            cartas.pop(0)
    elif ultima['tipo'] == '-4':
        for i in range(4):
            cartas.append(lista_de_cartas[0])
            lista_de_cartas.pop(0)
    
def puxar_cartas(mao, cartas): 
    num = possiveis_jogadas(mao)
    if num == 0:
        mao.append(cartas[0])
        cartas.pop(0)
    
def jogadas_do_jogador(mao, bolo):
    puxar_cartas(cartas_jogador, cartas) #Colocar isso no loop
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
        mao.pop(carta_selecionada)

def jogada_computador(mao, bolo):
    puxar_cartas(mao, cartas)
    possiveis_jogadas = []
    for carta in mao:
        if carta['cor'] == ultima['cor'] or carta['numero'] == ultima['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            possiveis_jogadas.append(carta)
    escolha = randint(0, len(possiveis_jogadas) - 1)
    jogada_final = possiveis_jogadas[escolha]
    bolo.append(jogada_final)
    mao.remove(jogada_final)

#carta inicial do bolo
num_carta_inicial = sorteando()
carta_inicial = cartas[num_carta_inicial]
cartas.remove(cartas[num_carta_inicial])
bolo.append(carta_inicial)


#jogador
cartas_jogador = []
quantidade_cartas_jogador = len(cartas_jogador)
distribuindo(cartas_jogador)
    
#computador
cartas_computador = []
quantidade_cartas_computador = len(cartas_computador)
distribuindo(cartas_computador)

#Turno
turno = 'jogador'

while True:
    relogio.tick(60)
    tela.fill(PRETO)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    #Recuperando a última carta do bolo
    ultima = bolo[-1]

    mouse_pos = pg.mouse.get_pos()
    mouse_click = pg.mouse.get_pressed()[0]

    # CARTAS DO JOGADOR
    largura = 100
    altura = 150
    espacamento = 20

    total = len(cartas_jogador) * (largura + espacamento) - espacamento
    inicio_x = LARGURA//2 - total//2
    y = ALTURA - altura - 30

    for i, carta in enumerate(cartas_jogador):
        x = inicio_x + i * (largura + espacamento)
        rect = pg.Rect(x, y, largura, altura)

        sobre_carta = rect.collidepoint(mouse_pos)
        if sobre_carta:
            y_anim = y - 30
        else:
            y_anim = y

        img = pg.transform.scale(carta["imagem"], (largura, altura))
        tela.blit(img, (x, y_anim))

    if turno == 'jogador':
        puxar_cartas_mais(cartas_jogador)
        jogadas_do_jogador(cartas_jogador, bolo)
        fim = pg.time.get_ticks()
        if fim - tempo_inicio_turno >= tempo_limite_turno:
            print("Tempo acabou!")
            turno = 'computador'
            tempo_inicio_turno = pg.time.get_ticks()

    if turno == 'computador':
        puxar_cartas_mais(cartas_computador)
        pg.time.delay(500)
        jogada_computador(cartas_computador, bolo)
        turno = 'jogador'
    
    #transformando as cartas
    last_card_image = ultima['imagem']
    last_card_image = pg.transform.scale(last_card_image, (400, 600))

    tela.blit(last_card_image, (LARGURA//2 - last_card_image.get_width()//2, ALTURA//2 - last_card_image.get_height()//2))

    #elementos na tela

    pg.display.flip()
    
