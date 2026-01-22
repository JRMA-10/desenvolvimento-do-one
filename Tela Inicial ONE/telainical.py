import pygame as py
running = True

py.init()
screen = py.display.set_mode((640, 480))
clock = py.time.Clock()
py.display.set_caption("ONE")

# -- Imagens --
background = py.image.load("imgs/ONE.png").convert_alpha()
play = py.image.load("imgs/Play.png").convert_alpha()
tela_de_configuracao = py.image.load("imgs/Telaconfiguracao.png").convert_alpha()
configuracao = py.image.load("imgs/Gear.png").convert_alpha()


# -- Background --
background = py.transform.scale(background, (640, 480))

# -- Botão Play --
play_x = 200
play_y = 260
play = py.transform.scale(play, (120, 60))
hitbox_play = py.Rect(play_x, play_y, 120, 60)

# -- Botão Configurações --
configuracao_x = 380
configuracao_y = 260
configuracao = py.transform.scale(configuracao, (60, 60))
hitbox_configuracao = py.Rect(configuracao_x, configuracao_y, 60, 60)

# -- Tela de configurações --
tela_de_configuracao = py.transform.scale(tela_de_configuracao, (400, 350))
mostrar_config = False

while running:
  for event in py.event.get():
    if event.type == py.QUIT:
      running = False
    elif event.type == py.MOUSEBUTTONDOWN:
      mouse_pos = py.mouse.get_pos()
      if hitbox_play.collidepoint(mouse_pos):
        print("Adicionar proxima tela")
      if hitbox_configuracao.collidepoint(mouse_pos):
        print("Botão de configurações foi clicado")
        mostrar_config = True

  screen.fill((0, 0, 0))

  centro1 = background.get_rect(center=(640//2, 480//2))
  centro2 = tela_de_configuracao.get_rect(center=(640//2, 480//2))

  screen.blit(background, centro1)
  screen.blit(play, (play_x, play_y))
  screen.blit(configuracao, (configuracao_x, configuracao_y))

  if mostrar_config == True:
    screen.blit(tela_de_configuracao, centro2)


  py.display.flip()
  clock.tick(60)
