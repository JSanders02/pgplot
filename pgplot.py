import pygame as pg


class Pgp(object):
    def __init__(self, surface, width, height, topleft=None, topright=None,
                 bottomleft=None, bottomright=None, centre=None):
        self.__screen = surface
        self.__width = width
        self.__height = height

        self.__rect = pg.Rect(0, 0, self.__width, self.__height)

        if topleft is not None:
            self.__rect.topleft = (int(topleft[0]), int(topleft[1]))

        elif topright is not None:
            self.__rect.topright = (int(topright[0]), int(topright[1]))

        elif bottomleft is not None:
            self.__rect.bottomleft = (int(bottomleft[0]), int(bottomleft[1]))

        elif bottomright is not None:
            self.__rect.bottomright = (int(bottomright[0]), int(bottomright[1]))

        elif centre is not None:
            self.__rect.center = (int(centre[0]), int(centre[1]))

    def update(self):
        pg.draw.rect(self.__screen, (222, 222, 222), self.__rect)


if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((1920, 1080))
    pgp = Pgp(screen, 600, 400, bottomleft=(960, 540))

    while True:
        for event in pg.event.get():
            if event == pg.QUIT:
                pg.quit()
                quit()
        screen.fill((255, 255, 255))
        pgp.update()
        pg.display.update()
