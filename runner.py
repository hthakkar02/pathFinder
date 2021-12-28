import pygame

pygame.init()

width = 800
screen = pygame.display.set_mode((width, width))

# white color
text_color = (255, 255, 255)

# light shade of the button
button_light = (170, 170, 170)

# dark shade of the button
button_dark = (100, 100, 100)

font = pygame.font.SysFont('Corbel', 35)
text = font.render("A Star Algorithm", True, text_color)
button1_w = ((text.get_width()//10) + 5)*10
button1_h = ((text.get_height()//10) + 2)*10

run = True

while run:
    mouse = pygame.mouse.get_pos()
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            run = False

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width / 2 + button1_w and width / 2 <= mouse[1] <= width / 2 + button1_h:
                run = False
    # if mouse is hovered on a button it
    # changes to lighter shade
    screen.fill((137, 207, 240))
    if width / 2 <= mouse[0] <= width / 2 + button1_w and width / 2 <= mouse[1] <= width / 2 + button1_h:
        pygame.draw.rect(screen, button_light, [width / 2, width / 2, button1_w, button1_h])

    else:
        pygame.draw.rect(screen, button_dark, [width / 2, width / 2, button1_w, button1_h])

    # superimposing the text onto our button
    screen.blit(text, (width / 2 + 25, width / 2 + 8))

    # updates the frames of the game
    pygame.display.update()
pygame.quit()

