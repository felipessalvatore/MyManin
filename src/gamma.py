# #!/usr/bin/env python
# # python3 -m manim gamma.py CreateGraph -p


from manim import *
import numpy as np


WAIT_TIME = 0.3



def get_exp(i):
    return lambda x: (x**(i-1))*np.exp(-x)


def get_exp_label(i):
    return 'x^{' + str(i) + "-1} e^{-x}"



class CreateGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 15],
            y_range=[0, 20],
            axis_config={"color": BLUE},
        )

        first_g = 4
        last_g = 6
        num_iter = 10
        range_graps = np.linspace(first_g, last_g, num=num_iter)
        graphs = [axes.get_graph(get_exp(i), color=WHITE) for i in range_graps]
        desc = [MathTex(get_exp_label(np.round(i,2))) for i in range_graps]

        title = Tex(r"Gamma Function")
        self.play(Write(title))
        self.wait()
        desc[0].to_corner(UP + LEFT)
        self.play(
            Transform(title, desc[0]))
        self.wait()
        self.play(Create(axes))
        self.wait()
        self.play(Create(graphs[0]))
        self.wait(WAIT_TIME)
        desc[1].to_corner(UP + LEFT)
        self.play(FadeOut(title),
                  Transform(desc[0], desc[1]),
                  Transform(graphs[0], graphs[0+1]))
        self.wait(WAIT_TIME)

        for i in range(len(graphs)+3):
            try:
                desc[i+1].to_corner(UP + LEFT)
                desc[i+2].to_corner(UP + LEFT)
                comands = [FadeOut(desc[i]),
                           Transform(desc[i+1], desc[i+2]),
                           FadeOut(graphs[i]),
                           Transform(graphs[i+1], graphs[i+2])]
                self.play(*comands)
                self.wait(WAIT_TIME)
            except IndexError:
                pass