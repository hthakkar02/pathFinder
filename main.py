import pygame
import a_star

WIDTH = 800

def main(WIDTH):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Path Finder Algorithms")

    light_blue = (137, 207, 240)
    text_color = (255, 255, 255)
    button_light = (170, 170, 170)
    button_dark = (100, 100, 100)

    font = pygame.font.SysFont('Corbel', 35)
    text = font.render("A Star Algorithm", True, text_color)
    button1_w = ((text.get_width() // 10) + 5) * 10
    button1_h = ((text.get_height() // 10) + 2) * 10

    run = True
    choice = None
    while run:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:
                run = False

            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH / 2 <= mouse[0] <= WIDTH / 2 + button1_w and WIDTH / 2 <= mouse[1] <= WIDTH / 2 + button1_h:
                    run = False
                    choice = "a_star"

        # if mouse is hovered on a button it
        # changes to lighter shade
        screen.fill(light_blue)
        if WIDTH / 2 <= mouse[0] <= WIDTH / 2 + button1_w and WIDTH / 2 <= mouse[1] <= WIDTH / 2 + button1_h:
            pygame.draw.rect(screen, button_light, [WIDTH / 2, WIDTH / 2, button1_w, button1_h])

        else:
            pygame.draw.rect(screen, button_dark, [WIDTH / 2, WIDTH / 2, button1_w, button1_h])

        # superimposing the text onto our button
        screen.blit(text, (WIDTH / 2 + 25, WIDTH / 2 + 8))

        # updates the frames of the game
        pygame.display.update()
    if choice == "a_star":
        a_star.main(screen, WIDTH)
    pygame.quit()


if __name__ == '__main__':
    main(WIDTH)
