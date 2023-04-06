from typing_extensions import runtime
from manim import *

class Partial(Scene):
    def construct(self):
        question = Text("How can we find the definite integral of").shift(UP * 2)
        # question.arrange(UP)
        text = Text("Integration by parts").shift(UP*3)

        eq = MathTex(r"\int x e^x \; dx").next_to(question, DOWN)
        eq2 = MathTex(r"\int u\;dv = uv-\int v\; du").scale(1.5)

        self.play(Write(question))
        self.play(Write(eq))
        self.wait(2)
        self.play(Unwrite(question), Unwrite(eq))
        self.wait(1)
        self.play(Write(text))
        self.play(Write(eq2, run_time=2))
        self.wait(2)
        