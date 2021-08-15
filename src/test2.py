import numpy as np
from manim import *
import random


DEFAULT_ANIMATION_RUN_TIME = 3

def random_small_angle():
    return random.uniform(-np.pi/40,np.pi/40)

class GrowFromCenterGeneral(Transform):
    def __init__(self, mobject, **kwargs):
        target = mobject.copy()
        mobject.scale_in_place(0)
        Transform.__init__(self, mobject, target, **kwargs)

def apple_pile():
    bottom_row = [Square(i).rotate(random_small_angle()) for i in range(3)]
    top_row = [Square(3).rotate(-np.pi/20),Square(4).rotate(np.pi/20)]
    Group(*bottom_row).arrange_submobjects(buff=0.1)
    Group(*top_row).arrange_submobjects(buff=0.1)
    Group(*top_row).next_to(Group(*bottom_row),direction=UP,buff=0)
    return Group(*(bottom_row + top_row))


class MyDrawing(Scene):
    def construct(self):
        apples = apple_pile().center()
        Group(apples).center()
        self.play(Succession(*map(GrowFromCenterGeneral, apples.submobjects), rate_func=None, run_time = 1.5*DEFAULT_ANIMATION_RUN_TIME))