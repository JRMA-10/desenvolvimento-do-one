import pygame as pg
from random import randint, shuffle, choice

# INICIALIZAÇÃO
pg.init()
tela = pg.display.set_mode((0, 0), pg.FULLSCREEN)
LARGURA, ALTURA = tela.get_size()
relogio = pg.time.Clock()

fonte = pg.font.Font(None, 26)
fonte_grande = pg.font.Font(None, 36)

# CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

#Contadores
tempo_limite_turno = 10000
tempo_inicio_turno = pg.time.get_ticks()

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
    cartas.append({"tipo": "comunista", 
                   "cor": None,
                   "numero": None,
                   "imagem": pg.image.load("imgs/comunista.png").convert_alpha()})

    return cartas

cartas = carregar_cartas()
shuffle(cartas)

#Bolo 
bolo = []

#Telas do jogo:
MENU_INICIAL = 0
JOGO = 1
PAUSA = 2
TELA_FINAL = 3
ESTADO = MENU_INICIAL

#Menu inical 
def menu_inicial():
    global ESTADO
    tela_inicial = pg.image.load("imgs/tela_inicial.png").convert()
    tela.blit(tela_inicial, (0,0))

    if event.type == pg.MOUSEBUTTONDOWN:
        ESTADO = JOGO


#Funções principais
def sorteando(cartas):
    return randint(0, len(cartas)-1) 

#cartas dos players
def distribuindo(mao, cartas):
    for i in range(7):
        num_carta_escolhida = sorteando(cartas)
        carta = cartas[num_carta_escolhida]
        cartas.remove(cartas[num_carta_escolhida])
        mao.append(carta)
    

def puxar_cartas(mao):
    contador = 0
    for carta in mao:
        if carta['cor'] == ultima['cor'] or carta['numero'] == ultima['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            contador += 1
    if contador == 0:
        return True
    return False

def puxar_cartas_mais(lista_de_cartas, cartas):
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

def funcao_tornado(mao1, mao2):
    mao1[:], mao2[:] = mao2[:], mao1[:]

def carta_valida(carta, ultima):
    return (carta["cor"] == ultima["cor"]
        or carta["numero"] == ultima["numero"]
        or carta["tipo"] == "+4"
        or carta["tipo"] == "+10"
        or carta["tipo"] == "-4"
        or carta["tipo"] == "tornado"
        or carta["tipo"] == "comunista"
    )

carta_selecionada = {}
def jogadas_do_jogador(mao, bolo, carta_selecionada):
    if not carta_selecionada:
        return
    if carta_valida(carta_selecionada, ultima):
        bolo.append(carta_selecionada)
        mao.remove(carta_selecionada)
    else:
        print("Jogada inválida!")

def jogadas_computador(mao, bolo):
    possiveis_jogadas = []
    for carta in mao:
        if carta['cor'] == ultima['cor'] or carta['numero'] == ultima['numero'] or carta['tipo'] in ['+4', '-4', 'comunista', 'tornado']:
            possiveis_jogadas.append(carta)
    if len(possiveis_jogadas) == 0: #Se o computador não tiver cartas válidas, ele puxa uma carta
        mao.append(cartas[0])
        cartas.pop(0)
    else:
        escolha = randint(0, len(possiveis_jogadas) - 1)
        jogada_final = possiveis_jogadas[escolha]
        bolo.append(jogada_final)
        mao.remove(jogada_final)

def cartas_de_acao(mao):
    global turno, tempo_inicio_turno
    if ultima['tipo'] == 'bloqueio':
        tempo_inicio_turno = pg.time.get_ticks()
        if turno == 'jogador':
            turno = 'computador'
        else:
            turno = 'jogador'
    if puxar_cartas(mao) == True:
        mao.append(cartas[0])
        cartas.pop(0)
        tempo_inicio_turno = pg.time.get_ticks()
        if turno == 'jogador':
            turno = 'computador'
        else:
            turno = 'jogador'
    if ultima['tipo'] == 'tornado':
        funcao_tornado(cartas_jogador, cartas_computador)
        if turno == 'jogador':
            turno = 'computador'
        else:
            turno = 'jogador'

#carta inicial do bolo
num_carta_inicial = sorteando(cartas)
carta_inicial = cartas[num_carta_inicial]
cartas.remove(cartas[num_carta_inicial])
bolo.append(carta_inicial)

#jogador
cartas_jogador = []
quantidade_cartas_jogador = len(cartas_jogador)
distribuindo(cartas_jogador, cartas)
    
#computador
cartas_computador = []
quantidade_cartas_computador = len(cartas_computador)
distribuindo(cartas_computador, cartas)

#Turno
turno = choice(['jogador', 'computador'])

while True:
    relogio.tick(60)
    tela.fill(PRETO)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
    
    if ESTADO == MENU_INICIAL:
        menu_inicial()
    
    if ESTADO == JOGO:
        
        tempo_restante = max(0, (tempo_limite_turno - (pg.time.get_ticks() - tempo_inicio_turno)) // 1000)
        tela.blit(
            fonte.render(f"Turno: {turno.upper()} | Tempo: {tempo_restante}s", True, BRANCO),
            (20, 20)
        )
        
        #Recuperando a última carta do bolo
        ultima = bolo[-1]
        def aparicao_ultima_carta():
            last_card_image = ultima['imagem']
            last_card_image = pg.transform.scale(last_card_image, (400, 600))
            tela.blit(last_card_image, (LARGURA//2 - last_card_image.get_width()//2, ALTURA//2 - last_card_image.get_height()//2))
        aparicao_ultima_carta()

        #Pegando posição do mouse e clique
        mouse_pos = pg.mouse.get_pos()
        mouse_click = pg.mouse.get_pressed()[0]

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # APARIÇÃO DAS CARTAS DO JOGADOR    
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        largura = 100
        altura = 150
        espacamento = 20

        total = len(cartas_jogador) * (largura + espacamento) - espacamento # usei (- espacamento) para não adicionar espaço extra na última carta
        inicio_x = LARGURA//2 - total//2
        y = ALTURA - altura - 30

        for i, carta in enumerate(cartas_jogador): # i retorna o índice da carta e carta retorna a própria carta
            x = inicio_x + i * (largura + espacamento)
            rect = pg.Rect(x, y, largura, altura)

            sobre_carta = rect.collidepoint(mouse_pos)
            if sobre_carta:
                y_anim = y - 30
            else:
                y_anim = y

            img = pg.transform.scale(carta["imagem"], (largura, altura))
            tela.blit(img, (x, y_anim))

            if sobre_carta and mouse_click and turno == 'jogador':
                carta_selecionada = carta

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # LÓGICA DO JOGADOR
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        if turno == 'jogador':
            #fim = pg.time.get_ticks()
            puxar_cartas_mais(cartas_jogador, cartas)
            cartas_de_acao(cartas_jogador)
            jogadas_do_jogador(cartas_jogador, bolo, carta_selecionada)
            if tempo_restante == 0:
                print("Tempo acabou!")
                turno = 'computador'
                tempo_inicio_turno = pg.time.get_ticks()
        ultima = bolo[-1]
        aparicao_ultima_carta()

        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        # LÓGICA DO COMPUTADOR
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        if turno == 'computador':
            puxar_cartas_mais(cartas_computador, cartas)
            cartas_de_acao(cartas_computador)
            pg.time.delay(500)
            jogadas_computador(cartas_computador, bolo)
            turno = 'jogador'

    pg.display.flip()