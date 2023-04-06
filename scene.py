from manim import *
from manim_slides import Slide

class deineMudda(Slide):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            tips=False,
            axis_config={"color": BLUE},
        )

        graph = axes.plot(lambda x: (1/3)*x**3+0.5*x**2+x-1, color=GREEN)
        graph_label = axes.get_graph_label(graph, label=MathTex(r"\frac{1}{3}x^3+\frac{1}{2}x^2+x-1"))

        graph2 = axes.plot(lambda x: x**2+x+1, color=RED)
        graph_label2 = axes.get_graph_label(graph2, label='x^{2}+x+1')

        graph3 = axes.plot(lambda x: 2*x + 1, color=YELLOW_D)
        graph_label3 = axes.get_graph_label(graph3, label='2x+1')

        self.play(Create(axes), Create(graph), Write(graph_label))
        self.pause()
        self.play(Transform(graph, graph2), Transform(graph_label, graph_label2))
        self.pause()
        self.play(Transform(graph, graph3), Transform(graph_label, graph_label3))
        self.pause()
        self.play(Unwrite(graph_label), Uncreate(graph), Uncreate(axes))
        self.wait()

class deineFormel(Scene):
    def construct(self):
        equation = MathTex(r"x_{1,2}= \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        equation2 = MathTex(r"i\hbar\frac{\partial\psi}{\partial t} = \left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\right]\psi")
        equation3 = MathTex(r"\frac{d}{dx}\int_a^x f(t) dt = f(x)")

        self.play(Write(equation))
        self.wait(2)
        self.play(Unwrite(equation))
        self.play(Write(equation2))
        self.wait(2)
        self.play(Unwrite(equation2))
        self.play(Write(equation3))
        self.wait(2)
        self.play(Unwrite(equation3))