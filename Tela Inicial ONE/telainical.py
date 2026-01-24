from tracemalloc import start
import pygame as py
running = True

py.init()
screen = py.display.set_mode((0, 0), py.FULLSCREEN)
clock = py.time.Clock()
py.display.set_caption("ONE")
largura, altura = screen.get_size()

Icone = py.image.load("imgs/Icone.png")
py.display.set_icon(Icone)

back_img = (largura, altura)

# -- Imagens --
background = py.image.load("imgs/ONE.png").convert_alpha()
play = py.image.load("imgs/Play.png").convert_alpha()
tela_de_configuracao = py.image.load("imgs/Telaconfiguracao.png").convert_alpha()
configuracao = py.image.load("imgs/Gear.png").convert_alpha()
close_config = py.image.load("imgs/fechartela.png").convert_alpha()
background2 = py.image.load("imgs/background2.png").convert_alpha()


# -- Background --
background = py.transform.scale(background, back_img)

# -- Botão Play --
play_x = (screen.get_width() // 2) - 400
play_y = screen.get_height() // 2 + 50
play = py.transform.scale(play, (360, 180))
hitbox_play = py.Rect(play_x, play_y, 360, 180)
start_game = False

# -- Tela de play --
background2 = py.transform.scale(background2, back_img)

# -- Botão Configurações --
configuracao_x = (screen.get_width() // 2) + 200
configuracao_y = screen.get_height() // 2 + 50
configuracao = py.transform.scale(configuracao, (180, 180))
hitbox_configuracao = py.Rect(configuracao_x, configuracao_y, 180, 180)

# -- Tela de configurações --
tela_de_configuracao = py.transform.scale(tela_de_configuracao, (1200, 800))
mostrar_config = False

# -- Fechar configurações --
close_x = 1300
close_y = 130
close_config = py.transform.scale(close_config, (160, 90))
hitbox_fechar_config = py.Rect(close_x, close_y, 160, 90)
fechar_config = False


while running:
  for event in py.event.get():
    if event.type == py.QUIT:
      running = False

    # -- Botões inicias --
    elif event.type == py.MOUSEBUTTONDOWN:
      mouse_pos = py.mouse.get_pos()

      # -- Botão PLAY
      if hitbox_play.collidepoint(mouse_pos):
        start_game = True

      # -- Botão de configuração
      if hitbox_configuracao.collidepoint(mouse_pos):
        mostrar_config = True
        fechar_config = True

  screen.fill((0, 0, 0))

  centro1_x = screen.get_size()
  centro1_y = screen.get_size()
  centro2_x = (screen.get_width() // 2) - 570
  centro2_y = (screen.get_height() // 2) - 430

  screen.blit(background, (0, 0))
  screen.blit(play, (play_x, play_y))
  screen.blit(configuracao, (configuracao_x, configuracao_y))

  if mostrar_config and fechar_config == True:
    screen.blit(tela_de_configuracao, (centro2_x, centro2_y))
    screen.blit(close_config, (close_x, close_y))
    
  if event.type == py.MOUSEBUTTONDOWN:
    if hitbox_fechar_config.collidepoint(mouse_pos):
        mostrar_config = False
        fechar_config = False

  if start_game == True:
    screen.blit(background2, (0, 0))
        

  py.display.flip()
  clock.tick(60)
