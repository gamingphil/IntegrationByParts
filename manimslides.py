from manim import *
from manim_slides import Slide
import manimpango

class PartInt(Slide):
    def construct(self):
        
        self.camera.background_color = "#181b2b"

        ### TITLE PAGE ###
        title1 = Text(
            "Partielle Integration",  
            font="Roboto Black", 
            font_size=55
        )
        title2 = Text(
            "Philip Mogilski, 23.02.2023", 
            font="Roboto Light", 
            font_size=30
        )        

        title1.shift(UP*0.3)
        title2.shift(DOWN*0.5)

        self.play(Write(title1))
        self.play(Write(title2))
        # self.pause()
        self.pause()
        self.play(Unwrite(title1), Unwrite(title2))

        ### TOPICS ###

        topicstitle = Text(
            "Themen",
            font="Roboto Medium", 
            font_size=55
        )

        topicstitle.scale(0.7).to_corner(UP + LEFT)

        topic1 = Text(
            "1. Die „Produktregel“ des Integrals",
            font="Roboto",
            font_size=45 
        )
        topic2 = Text(
            "2. Phoenix-Integration",
            font="Roboto" ,
            font_size=45
        )
        topic3 = Text(
            "3. DI-Methode",
            font="Roboto",
            font_size=45
        )

        topics = VGroup(topic1, topic2, topic3).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        topics.to_corner(LEFT)

        self.play(Write(topicstitle))
        self.play(Write(topic1))
        self.play(Write(topic2))
        self.play(Write(topic3))
        self.pause()
        self.play(Unwrite(topics))
        self.play(Unwrite(topicstitle))
        self.pause()

        ### Product Rule of the Integral ###

        slide3title = Text(
            "Die „Produktregel“ des Integrals",
            font="Roboto Medium", 
            font_size=55
        )

        productrule1 = MathTex(r"f(x) = u(x) \cdot v(x)", font_size = 60)
        productrule2 = MathTex(r"f'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x)", font_size = 60)
        productrule3 = MathTex(r"\int f(x)\; dx = \;?", font_size = 60)

        slide3 = VGroup(productrule1, productrule2).set_x(0).arrange(DOWN, buff=1.2, aligned_edge=LEFT).to_corner(LEFT)
        productrule3.move_to(productrule2, aligned_edge=LEFT)


        self.play(Write(slide3title))
        self.play(slide3title.animate.scale(0.7).to_corner(UP + LEFT))
        self.play(Write(productrule1))
        self.play(Write(productrule2))
        self.pause()
        self.play(Transform(productrule2, productrule3))
        self.pause()


        derivation1 = MathTex("(uv)'", "=", "u'v + uv'")
        derivation1copy = MathTex("(uv)'", "=", "u'v + uv'")
        derivation2 = MathTex("\int", "(uv)'", "\;dx", "=", "\int", "u'v + uv'", "\;dx")
        derivation2copy = MathTex("\int (", "uv", ")' \;dx", "=", "\int u'v + uv' \;dx")
        derivation3 = MathTex("uv", "=", "\int u'v + uv' \;dx")
        derivation3copy = MathTex("uv", "=", "\int", "u'v", "+", "uv'", "\;dx")
        derivation4 = MathTex("uv", "=", "\int", "u'v", "\;dx", "+", "\int", "uv'", "\;dx")
        derivation4copy = MathTex("uv", "=", "\int u'v \;dx", "+", "\int uv' \;dx")
        derivation4_2 = MathTex("\int uv' \;dx", "=", "uv", "-", "\int u'v \;dx")

        derivation = VGroup(derivation1, derivation2, derivation3, derivation4).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT).to_corner(LEFT).shift(DOWN*0.2)

        derivation1copy.move_to(derivation1, aligned_edge=LEFT)
        derivation2copy.move_to(derivation2, aligned_edge=LEFT)
        derivation3copy.move_to(derivation3, aligned_edge=LEFT)
        derivation4copy.move_to(derivation4, aligned_edge=LEFT)
        derivation4_2.move_to(derivation4, aligned_edge=LEFT)


        self.play(Unwrite(productrule1), Unwrite(productrule2))
        self.play(Write(derivation1))
        self.add(derivation1copy)
        self.pause()
        self.play(TransformMatchingTex(derivation1, derivation2))
        self.add(derivation2copy)
        self.pause()
        self.play(Transform(derivation2copy,derivation3))
        self.add(derivation3copy)
        self.pause()
        self.play(TransformMatchingTex(derivation3copy, derivation4))
        self.add(derivation4copy)
        self.remove(derivation4)
        self.pause()
        self.play(TransformMatchingTex(derivation4copy, derivation4_2))
        self.pause()
        self.play(Circumscribe(derivation4copy))
        self.remove(derivation4copy)
        self.add(derivation4_2)
        self.pause()
        self.play(
            FadeOut(derivation1copy), 
            FadeOut(derivation2copy),
            FadeOut(derivation1),
            FadeOut(derivation2),
            FadeOut(derivation3copy),
        )
        self.play(derivation4_2.animate.move_to(ORIGIN).shift(UP*1.5).scale(1.2))
        self.wait()