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

    font = pygame.font.SysFont('Corbel', 100)
    title1 = font.render("Path Finding", True, text_color)
    title2 = font.render("Algorithms", True, text_color)

    font = pygame.font.SysFont('Corbel', 60)
    # Buttons
    a_star_button = font.render("A Star Algorithm", True, text_color)
    dijkstras = font.render("Dijkstras Algorithm", True, text_color)
    buttons = [a_star_button, dijkstras]

    button_info = dict()
    for num in range(len(buttons)):
        button_info[num] = {"button": buttons[num], "button_width": 450,
                            "button_height": ((buttons[num].get_height() // 10) + 2) * 10}
    # "button_width": ((buttons[num].get_width() // 10) + 5) * 10
    run = True
    choice = None
    while run:
        mouse = pygame.mouse.get_pos()
        curr_x = 25
        curr_y = 400
        # Sets up the x and y position for each button
        for key in button_info:
            button_info[key]["button_x"] = curr_x
            button_info[key]["button_y"] = curr_y
            curr_y = curr_y + 25 + button_info[key]["button_height"]
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                run = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # Checks the button click
                for key in button_info:
                    if button_info[key]["button_x"] <= mouse[0] <= button_info[key]["button_x"] + \
                            button_info[key]["button_width"] \
                            and button_info[key]["button_y"] <= mouse[1] <= button_info[key]["button_y"] + \
                            button_info[key]["button_height"]:
                        run = False
                        choice = key
        screen.fill(light_blue)
        screen.blit(title1, ((WIDTH-title1.get_width())/2, 100))
        screen.blit(title2, ((WIDTH-title2.get_width())/2, 200))
        # Changes the color of the button if mouse is hovering over it
        for key in button_info:
            if button_info[key]["button_x"] <= mouse[0] <= button_info[key]["button_x"] + \
                    button_info[key]["button_width"] \
                    and button_info[key]["button_y"] <= mouse[1] <= button_info[key]["button_y"] + \
                    button_info[key]["button_height"]:
                pygame.draw.rect(screen, button_light, [button_info[key]["button_x"], button_info[key]["button_y"],
                                                        button_info[key]["button_width"],
                                                        button_info[key]["button_height"]])
            else:
                pygame.draw.rect(screen, button_dark, [button_info[key]["button_x"], button_info[key]["button_y"],
                                                       button_info[key]["button_width"],
                                                       button_info[key]["button_height"]])
            screen.blit(button_info[key]["button"], (button_info[key]["button_x"] + (button_info[key]["button_width"] -
                                                                                     buttons[key].get_width()) / 2,
                                                     button_info[key]["button_y"] + 8))
        # updates the frames of the game
        pygame.display.update()
    if choice == 0:
        a_star.main(screen, WIDTH)
    elif choice == 1:
        print("D")
    pygame.quit()


if __name__ == '__main__':
    main(WIDTH)
