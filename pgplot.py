import pygame as pg


class Pgp(object):
    def __init__(self, width, height):
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()

    def update(self):
        pass


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 400))
    Pgp(600, 400)

    while True:
        for event in pg.event.get():
            if event == pg.QUIT:
                pg.quit()
                quit()
        pg.display.update()
