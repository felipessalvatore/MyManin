from manim import *

class SquareToCircle(Scene):
    def construct(self):
        title = Tex(r"True Statements")
        title1 = Tex(r"$\aleph_\omega > \aleph_0$")
        title2 = Tex(r"Poli > IME")
        title3 = Tex(r"Thiago Lira > Jackson")
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-4 * TAU)
        circle.set_fill(RED, opacity=0.8)
        triangle = Polygon(np.array([0,0,0]),np.array([1,0,0]),np.array([0,-1,1]))
        triangle.set_fill(BLUE, opacity=0.8)
        triangle.flip(LEFT)

        VGroup(title, title1).arrange(DOWN)
        VGroup(title, title2).arrange(DOWN)
        VGroup(title, title3).arrange(DOWN)
        VGroup(title, square).arrange(DOWN)

        self.play(Write(title),
                  Write(title1))
        self.wait()
        self.play(Transform(title1, title2))
        self.wait()
        self.play(Transform(title1, title3))
        self.wait()
        self.play(FadeOut(title1))
        self.wait()
        self.play(Create(square))
        self.wait()
        self.play(Transform(square, circle))
        self.wait()
        self.play(Transform(square,triangle))
        self.wait()
        self.play(FadeOut(square))
        