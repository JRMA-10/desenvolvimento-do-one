import pygame as py

py.init()
screen = py.display.set_mode((640, 480))
clock = py.time.Clock()
running = True

mouse_x, mouse_y = 0, 0
font = py.font.Font(None, 100)
posição_x, posição_y = 50, 200
rect = py.Rect(posição_x, posição_y, 30, 30) # rect é a variavel representando a caixa de colisão (hitbox); py.Rect torna a variavel para funcionar como um Rect.
texto_surface = font.render("...", True, (0, 0, 0))

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEMOTION:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            print(f"Mouse está em {mouse_x}, {mouse_y}")
        elif event.type == py.MOUSEBUTTONDOWN:
            mouse_pos = py.mouse.get_pos()
            if rect.collidepoint(mouse_pos):
                texto_surface = font.render("Clicou na hitbox!", True, (0, 0, 0))

    # O texto mudará quando o mouse clicar no figure; "rect.collide..." é a principal ferramenta usada para indicar colisões


    screen.fill((255, 255, 255))

    figura = py.Surface((30, 30))
    figura.fill((0, 0, 0))
    screen.blit(figura, (posição_x, posição_y))

    screen.blit(texto_surface, (15, 40))

    py.display.flip()
    clock.tick(60)

    print(f"Mouse está em {mouse_x}, {mouse_y}")

py.quit()

