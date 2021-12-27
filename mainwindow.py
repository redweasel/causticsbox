import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

import raytracer as rt


class Menu:
    def render(self, screen: pg.Surface, width: int, height: int):
        raise NotImplementedError()

    def keydown(self, e):
        raise NotImplementedError()

    def keyup(self, e):
        raise NotImplementedError()

    def mousemove(self, mx, my):
        raise NotImplementedError()

    def help(self):
        raise NotImplementedError()


def draw_rays(ray_pos, ray_dir, ray_props):
    hack = 0.0
    vendor = glGetString(GL_VENDOR)
    if vendor == b"Intel":
        hack = 0.2

    # TODO very inefficient! better to use new shader pipeline.
    glLineWidth(2)
    glBegin(GL_LINES)
    for i in range(len(ray_props)):
        # HACK: compensate for light loss depending on the angle that is caused by rasterisation
        # this is only necessary on some devices, and not on others... weird! Is rasterisation with MSAA different?
        # For the record:
        # my NVIDIA GTX 1070 works without this hack
        # my Intel UHD Graphics 620 needs this hack
        # - redweasel
        fac = abs((ray_dir[i][0]**2 - ray_dir[i][1]**2) / (ray_dir[i][0]**2 + ray_dir[i][1]**2)) * hack + 1.0

        glColor(ray_props[i] / fac)  # hope the precision is enough
        glVertex2fv(ray_pos[i])
        glVertex2fv(ray_pos[i] + ray_dir[i] * 2000.0)
    glEnd()


class MainWindow(Menu):
    def __init__(self):
        super(MainWindow).__init__()

    def render(self, screen: pg.Surface, width: int, height: int):
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_DONT_CARE)
        mx, my = pg.mouse.get_pos()
        ray_pos, ray_dir, ray_props = rt.create_point_light_rays(mx, my, (0.2, 0.2, 0.2))
        draw_rays(ray_pos, ray_dir, ray_props)

    def keydown(self, e):
        pass

    def keyup(self, e):
        pass

    def mousemove(self, mx, my):
        pass

    def help(self):
        return ["Move Mouse to shine light"]
