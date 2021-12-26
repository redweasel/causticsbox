import pygame as pg
from time import time
from OpenGL.GL import *
from OpenGL.GLU import *
import mainwindow


class Context:
    def __init__(self):
        # start game
        pg.init()
        print("pygame driver:", pg.display.get_driver())

        # create window
        self.screen = None
        self.width = 800
        self.height = 600
        self.init_screen(800, 600)

        pg.key.set_repeat(500, 10)

        # customize window
        pg.display.set_caption("CausticsBox2D")
        #icon = pg.image.load_extended('./../res/causticsbox.png')
        #pg.display.set_icon(icon)

        # prepare text rendering
        pg.font.init()
        self.smallfont = pg.font.SysFont('Latin Modern Roman', 20)
        self.bigfont = pg.font.SysFont('Latin Modern Roman', 80)
        self.menu = None

    def set_menu(self, menu):
        self.menu = menu

    def draw_text(self, x, y, text, color=(255, 255, 255)):
        text_surface = self.smallfont.render(text, True, color, (0, 0, 0, 0)).convert_alpha()
        text_data = pg.image.tostring(text_surface, "RGBA", True)
        glWindowPos2d(x, self.height - y - text_surface.get_height())
        glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)

    def init_screen(self, w, h):
        self.width = w
        self.height = h
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLEBUFFERS, 1)
        pg.display.gl_set_attribute(pg.GL_MULTISAMPLESAMPLES, 8)
        self.screen = pg.display.set_mode((w, h), pg.RESIZABLE | pg.DOUBLEBUF | pg.OPENGL, vsync=1)  # type: pg.Surface # TODO is this needed on resize?
        glViewport(0, 0, w, h)
        # print("New Size:", (w, h), self.screen.get_size())

    def event(self, e):
        if e.type == pg.VIDEORESIZE:
            # reinit the screen buffer if the window is resized
            self.init_screen(e.w, e.h)
        elif e.type == pg.KEYDOWN:
            # if a key is pressed
            if self.menu:
                self.menu.keydown(e)
        # Wenn eine Taste losgelassen wird
        elif e.type == pg.KEYUP:
            # if a key is pressed
            if self.menu:
                self.menu.keyup(e)
        mx, my = pg.mouse.get_pos()
        if self.menu:
            self.menu.mousemove(mx, my)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        width, height = self.width, self.height

        glLoadIdentity()
        glOrtho(0.0, width, height, 0.0, 0.0, 1.0)

        glEnable(GL_BLEND)
        glBlendFunc(GL_ONE, GL_ONE)  # Additive Blending
        if self.menu:
            self.menu.render(self.screen, width, height)

        if pg.key.get_pressed()[pg.K_TAB]:
            if self.menu:
                help_list = self.menu.help()
                for i in range(len(help_list)):
                    self.draw_text(width - 250, height - 5 - 25 * (len(help_list) - i), help_list[i], (100, 100, 100))
        else:
            self.draw_text(width - 120, height - 30, 'Tab for Help', (100, 100, 100))

    def quit(self):
        pg.quit()


ctx = Context()
ctx.set_menu(mainwindow.MainWindow())

# Main Loop (this is where the program runs)
while True:
    # Eingaben einlesen
    for e in pg.event.get():
        # Für das Schließereignis das Spiel kontrolliert beenden
        if e.type == pg.QUIT:
            ctx.quit()
            exit()
        ctx.event(e)

    ctx.render()

    # Gezeichnete Inhalte in das Fenster übertragen
    pg.display.flip()
    pg.event.wait()
