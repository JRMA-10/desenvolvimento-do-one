import pygame as pg
from random import shuffle, choice

pg.init()
TELA = pg.display.set_mode((0, 0), pg.FULLSCREEN)
LARGURA, ALTURA = TELA.get_size()
FPS = 60
RELOGIO = pg.time.Clock()

FONTE = pg.font.Font(None, 28)
FONTE_GRANDE = pg.font.Font(None, 40)

BRANCO, PRETO, VERMELHO, VERDE, AMARELO = (255,255,255),(0,0,0),(200,0,0),(0,200,0),(200,200,0)
COSTA = pg.image.load("imgs/costa.png").convert_alpha()

#ESTADOS
TELA_INICIAL, TELA_JOGO, TELA_FINAL = 0, 1, 2

#TELA INICIAL
class TelaInicial:
    def __init__(self):
        self.fundo = pg.transform.scale(pg.image.load("imgs/tela_inicial.png").convert_alpha(),(LARGURA, ALTURA))
        self.play = pg.transform.scale(pg.image.load("imgs/Play.png").convert_alpha(),(250, 110))
        self.play_rect = self.play.get_rect(center = (LARGURA // 2 - 110, ALTURA//2 + 200))
        self.config = pg.transform.scale(pg.image.load("imgs/Gear.png").convert_alpha(),(110, 110))
        self.config_rect = self.config.get_rect(center=(LARGURA//2 + 110, ALTURA//2 + 200))

    def desenhar(self):
        TELA.blit(self.fundo, (0, 0))
        TELA.blit(self.play, self.play_rect)
        TELA.blit(self.config, self.config_rect)
        pg.display.flip()

    def clicar_play(self, pos):
        return self.play_rect.collidepoint(pos)

    def clicar_config(self, pos):
        return self.config_rect.collidepoint(pos)

class TelaFinal:
    def __init__(self):
        self.tela_final = pg.transform.scale(pg.image.load("imgs/tela_final.png").convert_alpha(),(LARGURA, ALTURA))
        self.texto_vencedor = FONTE_GRANDE.render(f"", True, BRANCO)
        self.texto_vencedor_rect = self.texto_vencedor.get_rect(center = (LARGURA // 2, ALTURA // 2))
        
        self.menu = pg.transform.scale(pg.image.load("imgs/Menu.png").convert_alpha(),(250, 110))
        self.menu_rect = self.menu.get_rect(center = (LARGURA // 2  - 200, ALTURA // 2 + 200))

        self.reiniciar = pg.transform.scale(pg.image.load("imgs/Reiniciar.png").convert_alpha(),(250, 110))
        self.reiniciar_rect = self.reiniciar.get_rect(center=(LARGURA//2 + 200, ALTURA//2 + 200))

    def desenhar(self):
        TELA.blit(self.tela_final, (0, 0))
        TELA.blit(self.texto_vencedor, self.texto_vencedor_rect)
        TELA.blit(self.menu, self.menu_rect)
        TELA.blit(self.reiniciar, self.reiniciar_rect)
        pg.display.flip()
        
    def clicar_menu(self, pos):
        return self.menu_rect.collidepoint(pos)

    def clicar_reiniciar(self, pos):
        return self.reiniciar_rect.collidepoint(pos)

#CARTAS
class Carta:
    def __init__(self, tipo, cor = None, numero = None):
        self.tipo = tipo
        self.cor = cor
        self.numero = numero
        nome = cor + str(numero) if tipo == "normal" else (cor + tipo if cor else tipo)
        self.img = pg.image.load(f"imgs/{nome}.png").convert_alpha()

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []
        self.uno = False

#JOGO
class Jogo:
    def __init__(self):
        self.estado = TELA_INICIAL #estado do jogo
        self.tela_inicial = TelaInicial()
        self.tela_final = TelaFinal()

        self.tela_de_jogo = pg.transform.scale(pg.image.load("imgs/tela_de_jogo.png").convert_alpha(),(LARGURA, ALTURA))
        self.baralho = self.criar_baralho()
        self.bolo = []

        self.jogador = Jogador("Jogador")
        self.computador = Jogador("Computador")
        self.turno = choice([self.jogador, self.computador])

        self.mensagem = None #Mensagens que aparecerão na tela
        self.msg_tempo = 0

        self.contador_one = 0
        self.contador_turno = 0
        self.tempo_turno = 10 * FPS

        self.distribuir(7) #Distribuição das cartas para os jogadores
        self.carta_inicial()

        self.rodando = True

    #BARALHO
    def criar_baralho(self):
        baralho = []
        cores = ["y", "r", "g", "b"]
        for cor in cores:
            for numero in range(10):
                baralho.extend([Carta("normal", cor, numero) for i in range(3)])
            for t in ["+2", "bloqueio", "reverse"]:
                for i in range(2):
                    baralho.append(Carta(t, cor))
        for t in ["+4","+10","-4","tornado","comunista"]:
            for i in range(2):
                baralho.append(Carta(t))
        shuffle(baralho)
        return baralho

    def distribuir(self, qtd):
        for i in range(qtd):
            self.jogador.mao.append(self.baralho.pop()) #A mão do jogador recebe cartas do baralho e estas são excluidas do baralho
            self.computador.mao.append(self.baralho.pop())

    def carta_inicial(self):
        while True: #Não pode começar com carta especial
            c = self.baralho.pop()
            if c.tipo == "normal":
                self.bolo.append(c)
                break
            self.baralho.insert(0, c)

    def ultima(self):
        return self.bolo[-1] #Retornar última carta

    def carta_valida(self, carta):
        ultima = self.ultima()
        if carta.tipo in ["+4", "+10", "-4", "tornado", "comunista"]:
            return True
        if carta.cor is not None and ultima.cor is not None:
            if carta.cor == ultima.cor:
                return True
        if carta.numero is not None and ultima.numero is not None:
            if carta.numero == ultima.numero:
                return True
        return False

    def jogador_tem_jogada(self):
        return any(self.carta_valida(c) for c in self.jogador.mao)

    

    #MENSAGENS
    def msg(self, texto, cor = BRANCO):
        self.mensagem = (texto, cor)
        self.msg_tempo = 3 * FPS

    #FIM / ONE
    def checar_uno(self):
        if len(self.jogador.mao) == 1 and not self.jogador.uno:
            self.msg("Pressione O para ONE!", AMARELO)
        if len(self.computador.mao) == 1 and not self.computador.uno:
            self.msg("Computador só tem UMA carta!", AMARELO)
            self.computador.uno = True

        if len(self.jogador.mao) > 1:
            self.jogador.uno = False
        if len(self.computador.mao) > 1:
            self.computador.uno = False

    def checar_fim(self):
        if len(self.jogador.mao) == 0:
            self.tela_final.texto_vencedor = FONTE_GRANDE.render(f"Você ganhou!!", True, BRANCO)
            self.tela_final.texto_vencedor_rect = self.tela_final.texto_vencedor.get_rect(center = (LARGURA // 2, ALTURA // 2))
            self.estado = TELA_FINAL
        elif len(self.computador.mao) == 0:
            self.tela_final.texto_vencedor = FONTE_GRANDE.render(f"Computador ganhou!!", True, BRANCO)
            self.tela_final.texto_vencedor_rect = self.tela_final.texto_vencedor.get_rect(center = (LARGURA // 2, ALTURA // 2))
            self.estado = TELA_FINAL

    #JOGO
    def puxar(self, jogador, qtd=1):
        for i in range(qtd):
            if self.baralho:
                jogador.mao.append(self.baralho.pop())
    
    def devolver(self, jogador, qtd=1):
        if len(jogador.mao) <= 4:
            while len(jogador.mao) > 1:
                self.baralho.append(jogador.mao.pop())
        else:
            for i in range(qtd):
                if jogador.mao:
                    self.baralho.append(jogador.mao.pop())
            shuffle(self.baralho)

    def jogar_computador(self):
        self.contador_turno += 1
        if self.contador_turno < 5 * FPS:
            return

        jogada = self.computador
        jogaveis = []
        for c in jogada.mao:
            if self.carta_valida(c):
                jogaveis.append(c) #lista "jogaveis" tem as cartas válidas para jogar

        if not jogaveis:
            self.puxar(jogada)
            self.msg("Computador puxou 1!", VERMELHO)
            self.turno = self.jogador
        else:
            c = choice(jogaveis)
            jogada.mao.remove(c)
            self.bolo.append(c)
            self.efeito(c, self.jogador)

        self.contador_turno = 0

    def efeito(self, carta, oponente):
        def nome_cor(cor):
            return {"r":"vermelha", "g":"verde", "b":"azul", "y":"amarela"}[cor]
        j = self.turno
        if carta.tipo == "+2":
            self.puxar(oponente, 2)
            self.msg(f"{oponente.nome} puxou 2!", VERMELHO)
            self.turno = oponente
        elif carta.tipo in ["+4", "+10"]:
            self.puxar(oponente, 4 if carta.tipo == "+4" else 10)
            self.msg(f"{oponente.nome} puxou {carta.tipo}!", VERMELHO)
            carta.cor = choice(["r","g","b","y"])
            self.msg(f"A cor escolhida foi {nome_cor(carta.cor)}!", AMARELO)
            self.turno = oponente
        elif carta.tipo == "-4":
            self.devolver(j, 4)
            self.msg("Efeito -4!", VERMELHO)
            carta.cor = choice(["r","g","b","y"])
            self.msg(f"A cor escolhida foi {nome_cor(carta.cor)}!", AMARELO)
            self.turno = oponente
        elif carta.tipo == "tornado":
            self.jogador.mao, self.computador.mao = self.computador.mao, self.jogador.mao
            self.msg("Tornado! Mãos trocadas!", VERDE)
            carta.cor = choice(["r","g","b","y"])
            self.msg(f"A cor escolhida foi {nome_cor(carta.cor)}!", AMARELO)
        elif carta.tipo == "bloqueio":
            self.msg("Turno bloqueado!", AMARELO)
            self.turno = j
        elif carta.tipo == "reverse":
            self.msg("Inversão de turno!", AMARELO)
            self.turno = j
        elif carta.tipo == "comunista":
            cartas_totais = self.jogador.mao + self.computador.mao
            quantidade_total = len(cartas_totais)
            shuffle(cartas_totais)
            if quantidade_total % 2 == 0:
                metade = quantidade_total // 2
                self.jogador.mao = cartas_totais[:metade]
                self.computador.mao = cartas_totais[metade:]
            else: 
                cartas_totais.append(self.baralho.pop())
                metade = quantidade_total // 2
                self.jogador.mao = cartas_totais[:metade + 1]
                self.computador.mao = cartas_totais[metade:]
            self.msg("Comunista! Cartas igualadas", VERDE)
            carta.cor = choice(["r","g","b","y"])
            self.msg(f"A cor escolhida foi {nome_cor(carta.cor)}!", AMARELO)
            self.turno = oponente
        else:
            self.turno = oponente


    #DESENHO
    def desenhar_jogo(self):
        TELA.blit(self.tela_de_jogo, (0, 0))
        TELA.blit(pg.transform.scale(self.ultima().img, (400,600)), (LARGURA // 2 - 200, ALTURA // 2 - 300))

        largura, altura, espacamento = 100 , 150, 20
        total = len(self.jogador.mao) * (largura + espacamento) - espacamento
        x0 = LARGURA // 2 - total // 2
        y0 = ALTURA - altura - 30

        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()[0]

        for i, carta in enumerate(self.jogador.mao[:]):
            x = x0 + i * (largura + espacamento)
            rect = pg.Rect(x, y0, largura, altura)
            y = y0 - 30 if rect.collidepoint(mouse) else y0

            TELA.blit(pg.transform.scale(carta.img, (largura, altura)), (x, y))
            if click and rect.collidepoint(mouse) and self.turno == self.jogador and self.carta_valida(carta):
                self.jogador.mao.remove(carta)
                self.bolo.append(carta)
                self.efeito(carta, self.computador)
                self.contador_turno = 0

        # computador
        largura_c, altura_c, espacamento_c = 60, 90, 20
        total_c = len(self.computador.mao) * (largura_c + espacamento_c) - espacamento_c
        x0c = LARGURA // 2 - total_c // 2
        for i in range(len(self.computador.mao)):
            TELA.blit(pg.transform.scale(COSTA,(largura_c, altura_c)),
                      (x0c + i * (largura_c + espacamento_c), 30))

        # textos
        if self.mensagem:
            txt, cor = self.mensagem
            texto_surf = FONTE_GRANDE.render(txt, True, cor)
            texto_rect = texto_surf.get_rect(center = (LARGURA//2, 175))  #centraliza horizontalmente
            TELA.blit(texto_surf, texto_rect)
            self.msg_tempo -= 1
            if self.msg_tempo <= 0:
                self.mensagem = None

        TELA.blit(FONTE.render(f"Turno: {self.turno.nome}", True, AMARELO),(20, 20))
        TELA.blit(FONTE.render(f"Cartas computador: {len(self.computador.mao)}", True, BRANCO), (20, 50))
        TELA.blit(FONTE.render(f"Tempo restante: {max(0,(self.tempo_turno-self.contador_turno)//FPS)}s",True, BRANCO), (20, 80))
        
        def nome_cor(cor):
            return {"r":"vermelha", "g":"verde", "b":"azul", "y":"amarela"}[cor]
        TELA.blit(FONTE.render(f"Cor: {nome_cor(self.ultima().cor)}", True, BRANCO), (20, 110))

        pg.display.flip()

#Loop
jogo = Jogo()

while True:
    RELOGIO.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            

        if event.type == pg.KEYDOWN and event.key == pg.K_o and len(jogo.jogador.mao)==1:
            jogo.jogador.uno = True

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if jogo.estado == TELA_INICIAL and jogo.tela_inicial.clicar_play(event.pos):
                jogo.estado = TELA_JOGO
            if jogo.estado == TELA_INICIAL and jogo.tela_inicial.clicar_config(event.pos):
                jogo.msg("Configurações não implementadas.", AMARELO)
            if jogo.estado == TELA_FINAL and jogo.tela_final.clicar_menu(event.pos):
                jogo = Jogo()
                jogo.estado = TELA_INICIAL 
            if jogo.estado == TELA_FINAL and jogo.tela_final.clicar_reiniciar(event.pos):
                jogo = Jogo()
                jogo.estado = TELA_JOGO

    if jogo.estado == TELA_INICIAL:
        jogo.tela_inicial.desenhar()

    elif jogo.estado == TELA_JOGO:

        if jogo.turno == jogo.jogador:
            jogo.contador_turno += 1

            if not jogo.jogador_tem_jogada():
                jogo.puxar(jogo.jogador)
                jogo.msg("Sem jogada válida. Você puxou 1!", VERMELHO)
                jogo.turno = jogo.computador
                jogo.contador_turno = 0

            elif jogo.contador_turno >= jogo.tempo_turno:
                jogo.puxar(jogo.jogador)
                jogo.msg("Tempo esgotado! Você puxou 1!", VERMELHO)
                jogo.turno = jogo.computador
                jogo.contador_turno = 0

        else:
            jogo.jogar_computador()

        jogo.checar_uno()
        jogo.checar_fim()
        jogo.desenhar_jogo()

    elif jogo.estado == TELA_FINAL:
        jogo.tela_final.desenhar()