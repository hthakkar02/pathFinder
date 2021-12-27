import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finder Algorithms")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.total_rows = total_rows
        self.color = WHITE
        self.neighbors = []
        self.width = width

    def get_position(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.width))

    def update_neighbors(self):
        pass

    def __lt__(self, other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for row in range(rows):
        grid.append([])
        for column in range(rows):
            grid[row].append(Node(row, column, gap, rows))
    return grid


def draw_grid(window, rows, width):
    gap = width // rows
    for row in range(rows):
        pygame.draw.line(window, GREY, (0, row * gap), (width, row * gap))
        for column in range(rows):
            pygame.draw.line(window, GREY, (column * gap, 0), (column * gap, width))


def draw(window, grid, rows, width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(window)
    draw_grid(window, rows, width)
    pygame.display.update()


def get_click_pos(mouse_pos, rows, width):
    gap = width // rows
    y, x = mouse_pos
    return y // gap, x // gap


def main(window, width):
    rows = 50
    grid = make_grid(rows, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(window, grid, rows, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:  # Left Mouse Click
                mouse_pos = pygame.mouse.get_pos()
                row, column = get_click_pos(mouse_pos, rows, width)
                node = grid[row][column]

                if not start and node != end and not node.is_barrier():
                    start = node
                    start.make_start()
                elif not end and node != start and not node.is_barrier():
                    end = node
                    end.make_end()
                elif node != start and node != end:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # Right Mouse Click
                mouse_pos = pygame.mouse.get_pos()
                row, column = get_click_pos(mouse_pos, rows, width)
                node = grid[row][column]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

    pygame.quit()


if __name__ == '__main__':
    main(WINDOW, WIDTH)
