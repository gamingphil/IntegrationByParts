from manim import *
from manim_slides import Slide
import manimpango

class PartielleIntegration(Scene):
    def construct(self):
        
        self.camera.background_color = "#181b2b"
        def titlepage():
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
            self.wait(1)
            self.play(Unwrite(title1), Unwrite(title2))

        def topics():
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
            self.wait(1)
            self.play(Unwrite(topics))
            self.play(Unwrite(topicstitle))
            self.wait(1)


        def integralproductrule():
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
            self.wait(1)
            self.play(Transform(productrule2, productrule3))
            self.wait(1)


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
            self.wait(1)
            self.play(TransformMatchingTex(derivation1, derivation2))
            self.add(derivation2copy)
            self.wait(1)
            self.play(Transform(derivation2copy,derivation3))
            self.add(derivation3copy)
            self.wait(1)
            self.play(TransformMatchingTex(derivation3copy, derivation4))
            self.add(derivation4copy)
            self.remove(derivation4)
            self.wait(1)
            self.play(TransformMatchingTex(derivation4copy, derivation4_2))
            self.wait(0.3)
            self.play(Circumscribe(derivation4copy))
            self.remove(derivation4copy)
            self.add(derivation4_2)
            self.wait(1)
            self.play(
                FadeOut(derivation1copy), 
                FadeOut(derivation2copy),
                FadeOut(derivation1),
                FadeOut(derivation2),
                FadeOut(derivation3copy),
            )
            self.play(derivation4_2.animate.move_to(ORIGIN).shift(UP*1.5).scale(1.2))

            ### EXAMPLE ###

            dividerline = Line(LEFT*6, RIGHT*6).shift(UP*0.25)

            dividerline.set_stroke(color=GREY, width=1)

            example1_1 = MathTex(r"\int", r"x",r"\cos(x)", r"\, dx", font_size = 40)
            example1_2 = MathTex(r"=", r"x \cdot \sin(x)", r"-\int \sin(x) \cdot 1 \, dx", font_size = 40)
            example1_3 = MathTex(r"= x \sin(x) + \cos(x) + c", font_size = 40)

            example1 = VGroup(example1_1, example1_2, example1_3).set_x(0).arrange(DOWN, buff=0.5, aligned_edge=LEFT).to_corner(DOWN + LEFT).shift(UP*0.1)


            self.play(Create(dividerline))
            self.play(Write(example1_1))
            self.play(Write(example1_2[0]))

            part1 = MathTex(r"u =", "x")
            part2 = MathTex(r"u' =", r"1")
            part3 = MathTex(r"v =", r"\sin(x)")
            part4 = MathTex(r"v' =", r"\cos(x)")

            parts = VGroup(part1, part2, part3, part4)
            parts.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(DOWN*1.5)

            self.play(
                Write(part1[0]),
                Write(part2[0]),
                Write(part3[0]),
                Write(part4[0]),
            )

            ### ----> u and dv choice brackets <------ ###

            ubrace = Brace(example1_1[1],sharpness=2,buff=0.2).set_color(RED_C)
            utext = MathTex(r"u", font_size=40).next_to(ubrace, DOWN).set_color(RED_C)

            self.play(DrawBorderThenFill(ubrace), Write(utext))

            vbrace = Brace(example1_1[2],sharpness=2,buff=0.1).set_color(GREEN_C)
            vtext = MathTex(r"v'", font_size=40).next_to(vbrace, DOWN*0.4).set_color(GREEN_C)

            self.play(DrawBorderThenFill(vbrace), Write(vtext))


            derivationcolored = MathTex("\int uv' \;dx = uv - \int u'v \;dx")
            derivationcolored.move_to(ORIGIN).shift(UP*1.5).scale(1.2)
            derivationcolored[0][1:2].set_color(RED_C)
            derivationcolored[0][2:4].set_color(GREEN_C)
            derivationcolored[0][7:8].set_color(RED_C)
            

            cpart1 = MathTex(r"u =", "x")
            cpart1[0][0:1].set_color(RED_C)
            cpart2 = MathTex(r"u' =", r"1")
            cpart3 = MathTex(r"v =", r"\sin(x)")
            cpart4 = MathTex(r"v' =", r"\cos(x)")
            cpart4[0][0:2].set_color(GREEN_C)
            
            cparts = VGroup(cpart1, cpart2, cpart3, cpart4)
            cparts.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(DOWN*1.5)
            
            self.play(
                FadeTransform(derivation4_2, derivationcolored),
                FadeTransform(part1[0], cpart1[0]),
                FadeTransform(part4[0], cpart4[0])
            )

            self.wait(1)
            self.play(
                Write(part1[1]),
                Write(part4[1]),
            )
            self.wait(1)
            self.play(Write(part2[1]))
            self.wait(1)
            self.play(Write(part3[1]))

            framebox1 = SurroundingRectangle(derivation4_2[2], buff = .1)
            framebox2group = VGroup(derivation4_2[3], derivation4_2[4])
            framebox2 = SurroundingRectangle(framebox2group, buff = .1)

            self.play(Create(framebox1))
            self.wait(1)
            self.play(Write(example1_2[1]))
            self.wait(1)
            self.play(ReplacementTransform(framebox1, framebox2))
            self.wait(1)
            self.play(Write(example1_2[2]))

            self.wait(1)
            self.play(Write(example1_3))


        def indefiniteIntegral():
            title = Text(
                "Bestimmtes und unbestimmtes Integral",
                font="Roboto Medium", 
                font_size=55
            )

            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))

            definite = MathTex(r"\int_a^b f(x) \, dx =", r"\left[F(x)\right]_a^b=", r"F(b) - F(a)")
            arrow1 = Arrow(max_tip_length_to_length_ratio=0.1).scale(0.4)
            definiteText = Text("bestimmtes Integral", font="Roboto", font_size=32)
            definiteTextGroup = VGroup(arrow1, definiteText).set_x(0).arrange(RIGHT,buff=0.1)
            



            indefinite = MathTex(r"\int f(x) \, dx =", r"F(x)", "+c")
            arrow2 = Arrow(max_tip_length_to_length_ratio=0.1).scale(0.4)
            indefiniteText = Text("unbestimmtes Integral", font="Roboto", font_size=32)
            indefiniteTextGroup = VGroup(arrow2, indefiniteText).set_x(0).arrange(RIGHT,buff=0.1)

            
            slide = VGroup(definite, definiteTextGroup, indefinite, indefiniteTextGroup).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT).to_corner(LEFT)

            indefinite.shift(DOWN*0.5)
            indefiniteTextGroup.shift(DOWN*0.5)

            self.play(Write(definite[0]))
            self.wait(1)
            self.play(Write(definite[1]))
            self.wait(1)
            self.play(Write(definite[2]))
            self.wait(1)
            self.play(Write(definiteTextGroup))
            self.wait(1)
            self.play(Write(indefinite[0]))
            self.wait(1)
            self.play(Write(indefinite[1]))
            self.wait(1)
            self.play(Write(indefinite[2]))
            self.wait(1)
            self.play(Write(indefiniteTextGroup))
            self.wait(5)
            self.play(Unwrite(slide))
            self.play(Unwrite(title))
            self.wait(1)

        # titlepage()
        # topics()
        # integralproductrule()
        indefiniteIntegral()