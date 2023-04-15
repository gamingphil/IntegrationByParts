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
                "Philip Mogilski, 18.04.2023", 
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
                "1. Bestimmtes und unbestimmtes Integral",
                font="Roboto",
                font_size=40
            )
            topic2 = Text(
                "2. Die „Produktregel“ des Integrals",
                font="Roboto",
                font_size=40 
            )
            topic3 = Text(
                "3. Phoenix-Integration",
                font="Roboto" ,
                font_size=40
            )
            topic4 = Text(
                "4. DI-Methode",
                font="Roboto",
                font_size=40
            )

            topics = VGroup(topic1, topic2, topic3, topic4).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
            topics.to_corner(LEFT)

            self.play(Write(topicstitle))
            self.play(Write(topic1))
            self.play(Write(topic2))
            self.play(Write(topic3))
            self.play(Write(topic4))
            self.wait(1)
            self.play(Unwrite(VGroup(topicstitle, topics)))
            self.wait(1)


        def integralproductrule():
            ### Product Rule of the Integral ###

            title = Text(
                "Die „Produktregel“ des Integrals",
                font="Roboto Medium", 
                font_size=55
            )

            productrule1 = MathTex(r"f(x) = u(x) \cdot v(x)", font_size = 60)
            productrule2 = MathTex(r"f'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x)", font_size = 60)
            productrule3 = MathTex(r"\int f(x)\; dx = \;?", font_size = 60)

            productrule = VGroup(productrule1, productrule2).set_x(0).arrange(DOWN, buff=1.2, aligned_edge=LEFT).to_corner(LEFT)
            productrule3.move_to(productrule2, aligned_edge=LEFT)


            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))
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


            self.play(Unwrite(VGroup(productrule1, productrule2)))
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

            example_1 = MathTex(r"\int", r"x",r"\cos(x)", r"\, dx", font_size = 40)
            example_2 = MathTex(r"=", r"x \cdot \sin(x)", r"-\int \sin(x) \cdot 1 \, dx", font_size = 40)
            example_3 = MathTex(r"= x \sin(x) + \cos(x)", r"+ c", font_size = 40)

            example = VGroup(example_1, example_2, example_3).set_x(0).arrange(DOWN, buff=0.5, aligned_edge=LEFT).to_corner(DOWN + LEFT).shift(UP*0.1)


            self.play(Create(dividerline))
            self.play(Write(example_1))
            self.play(Write(example_2[0]))

            part1 = MathTex(r"u =", "x")
            part2 = MathTex(r"u' =", r"1")
            part3 = MathTex(r"v =", r"\sin(x)")
            part4 = MathTex(r"v' =", r"\cos(x)")

            parts = VGroup(part1, part2, part3, part4)
            parts.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(DOWN*1.5)

            self.play(Write(VGroup(part1[0], part2[0], part3[0], part4[0])))

            
            ### ----> u and dv choice brackets <------ ###

            ubrace = Brace(example_1[1],sharpness=2,buff=0.2).set_color(RED_C)
            utext = MathTex(r"u", font_size=40).next_to(ubrace, DOWN).set_color(RED_C)

            self.play(DrawBorderThenFill(ubrace), Write(utext))

            vbrace = Brace(example_1[2],sharpness=2,buff=0.1).set_color(GREEN_C)
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
            self.play(Write(part1[1]))
            self.play(Write(part4[1]))
            self.wait(1)
            self.play(Write(part2[1]))
            self.wait(1)
            self.play(Write(part3[1]))

            framebox1 = SurroundingRectangle(derivation4_2[2], buff = .1)
            framebox2group = VGroup(derivation4_2[3], derivation4_2[4])
            framebox2 = SurroundingRectangle(framebox2group, buff = .1)

            self.play(Create(framebox1))
            self.wait(1)
            self.play(Write(example_2[1]))
            self.wait(1)
            self.play(ReplacementTransform(framebox1, framebox2))
            self.wait(1)
            self.play(Write(example_2[2]))

            self.wait(1)
            self.play(Write(example_3[0]))
            self.wait(1)
            self.play(Write(example_3[1]))

            ### wrong choice of u and dv

            wpart1 = MathTex(r"u =", "\cos(x)")
            wpart1[0][0:1].set_color(RED_C)
            wpart2 = MathTex(r"u' =", r"-\sin(x)")
            wpart3 = MathTex(r"v =", r"\frac{1}{2}x^2")
            wpart4 = MathTex(r"v' =", r"x")
            wpart4[0][0:2].set_color(GREEN_C)

            wparts = VGroup(wpart1, wpart2, wpart3, wpart4)
            wparts.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(DOWN*1.5)

            self.wait(4)
            self.play(
                Unwrite(VGroup(example_2, example_3, part1[1], part2[1], part3[1], part4[1])), 
                Uncreate(framebox2), 
                Transform(VGroup(cpart1[0], part2[0], part3[0], cpart4[0]), VGroup(wpart1[0], wpart2[0] ,wpart3[0], wpart4[0]))
                )
            self.wait(1)

            self.play(
                ubrace.animate.set_color(GREEN_C),
                utext.animate.next_to(vbrace, DOWN),
                vbrace.animate.set_color(RED_C),
                vtext.animate.next_to(ubrace, DOWN*0.4),
            )


            self.wait(1)
            self.play(Write(wpart1[1]))
            self.play(Write(wpart4[1]))
            self.wait(1)
            self.play(Write(wpart2[1]))
            self.wait(1)
            self.play(Write(wpart3[1]))
            self.wait(1)

            wrongexample_2 = MathTex(r"= \frac{1}{2}x^2 \cos(x)", r"-", r"\int -\frac{1}{2}x^2 \sin(x) \, dx", font_size = 40)
            wrongexample_2.to_corner(LEFT).shift(DOWN*2.5)

            self.play(Write(wrongexample_2[0]))
            self.wait(1)
            self.play(Write(VGroup(wrongexample_2[1], wrongexample_2[2])))
            self.wait(1)
            self.play(wrongexample_2[2].animate.scale(1.1).set_color(YELLOW_C))
            self.wait(3)


            self.play(
                Unwrite(VGroup(example_1, wrongexample_2, wpart1[1], cpart1[0], wpart2[1], part2[0], wpart3[1], part3[0], wpart4[1], cpart4[0])),
                Unwrite(VGroup(ubrace, utext)),
                Unwrite(VGroup(vbrace, vtext))
            )


            ### how to choose u and dv

            udvchoice1 = Tex("$u$ und $v'$ müssen so gewählt werden,")
            udvchoice1[0][0:1].set_color(RED_C)
            udvchoice1[0][4:6].set_color(GREEN_C)
            udvchoice2 = Tex("dass $u'v$ leicht zu integrieren ist.")

            udvchoice = VGroup(udvchoice1, udvchoice2).arrange(DOWN)
            udvchoice.shift(DOWN*1.5)

            self.wait(1)
            self.play(Write(udvchoice))
            self.wait(5)

            self.play(
                Unwrite(VGroup(title, derivationcolored, udvchoice)),
                Uncreate(dividerline, reverse=False)
                )
            self.wait(1)


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
            definiteText = Tex("bestimmtes Integral")
            definiteTextGroup = VGroup(arrow1, definiteText).set_x(0).arrange(RIGHT,buff=0.1)

            indefinite = MathTex(r"\int f(x) \, dx =", r"F(x)", "+c")
            arrow2 = Arrow(max_tip_length_to_length_ratio=0.1).scale(0.4)
            indefiniteText = Tex("unbestimmtes Integral")
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
            self.play(Unwrite(VGroup(title, slide)))
            self.wait(1)

            
        def examples():
            title = Text(
                "Beispiele",
                font="Roboto Medium", 
                font_size=55
            )

            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))

            ### EXAMPLE 1: x^4 * ln(x)

            ex1_1 = MathTex(r"\int x^4 \ln(x) \, dx")
            ex1_2 = MathTex(r"= \frac{1}{5}x^5 \ln(x)-", r" \int \frac{1}{5}x^5 \cdot \frac{1}{x} \, dx")
            ex1_3 = MathTex(r"= \frac{1}{5}x^2 \ln(x) - \int \frac{1}{5}x^4 \, dx")
            ex1_4 = MathTex(r"= \frac{1}{5}x^2 \ln(x) - \frac{1}{25}x^5 + c")

            ex1 = VGroup(ex1_1, ex1_2, ex1_3, ex1_4).arrange(DOWN).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT).to_corner(LEFT).shift(DOWN*0.3)

            ex1part1 = MathTex(r"u=", r"\ln(x)")
            ex1part2 = MathTex(r"u'=", r"\frac{1}{x}")
            ex1part3 = MathTex(r"v=", r"\frac{1}{5} x^5")
            ex1part4 = MathTex(r"v'=", r"x^4")

            ex1parts = VGroup(ex1part1, ex1part2, ex1part3, ex1part4)
            ex1parts.arrange_in_grid(cols=2, buff=0.5, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(LEFT*0.5)


            self.play(Write(ex1_1))
            self.wait(2)
            self.play(Write(VGroup(ex1part1[0], ex1part2[0], ex1part3[0], ex1part4[0])))
            self.wait(1)
            self.play(Write(ex1part1[1]))
            self.wait(1)
            self.play(Write(ex1part4[1]))
            self.wait(1)
            self.play(Write(ex1part2[1]))
            self.wait(1)
            self.play(Write(ex1part3[1]))
            self.wait(1)
            self.play(Write(ex1_2[0]))
            self.wait(1)
            self.play(Write(ex1_2[1]))
            self.wait(1)
            self.play(Write(ex1_3))
            self.wait(1)
            self.play(Write(ex1_4))
            self.wait(3)

            self.play(Unwrite(VGroup(ex1_1, ex1_2, ex1_3, ex1_4, ex1part1, ex1part2, ex1part3, ex1part4)))


            ### EXAMPLE 2: x^2 * e^x


            ex2_1 = MathTex(r"\int x^2 e^x \, dx")
            ex2_2 = MathTex(r"= x^2 e^x-", r"\int \frac{1}{2}x e^x \, dx")
            ex2_3 = MathTex(r"= x^2 e^x- \left(", r"\frac{1}{2}x e^x", r"-\int \frac{1}{2}e^x \, dx \right)")
            ex2_4 = MathTex(r"= x^2 e^x", r"- \left( \frac{1}{2}x e^x", r"- \frac{1}{2}e^x \right)")
            ex2_5 = MathTex(r"=", r"x^2", r"e^x", r"- \frac{1}{2}x", r"e^x", r"+ \frac{1}{2}", r"e^x", r"+ c")
            ex2_6 = MathTex(r"=", r"e^x", r"\left(", r"x^2", r"- \frac{1}{2}x", r"+ \frac{1}{2}", r"\right)", r"+ c")

            ex2 = VGroup(ex2_1, ex2_2, ex2_3, ex2_4, ex2_5).arrange(DOWN).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT).scale(0.85).to_corner(LEFT).shift(DOWN*0.3)
            ex2_6.scale(0.85).move_to(ex2_5, aligned_edge=LEFT)


            ex2part1 = MathTex(r"u=", r"x^2")
            ex2part2 = MathTex(r"u'=", r"\frac{1}{2}x")
            ex2part3 = MathTex(r"v=", r"e^x")
            ex2part4 = MathTex(r"v'=", r"e^x")

            ex2parts = VGroup(ex2part1, ex2part2, ex2part3, ex2part4)
            ex2parts.arrange_in_grid(cols=2, buff=0.5, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(LEFT*0.5)

            ex2_2part1 = MathTex(r"u=", r"\frac{1}{2}x")
            ex2_2part2 = MathTex(r"u'=", r"\frac{1}{2}")
            ex2_2part3 = MathTex(r"v=", r"e^x")
            ex2_2part4 = MathTex(r"v'=", r"e^x")

            ex2_2parts = VGroup(ex2_2part1, ex2_2part2, ex2_2part3, ex2_2part4)
            ex2_2parts.arrange_in_grid(cols=2, buff=0.5, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(LEFT*0.5)


            self.wait(1)
            self.play(Write(ex2_1))
            self.wait(2)
            self.play(Write(VGroup(ex2part1[0], ex2part2[0], ex2part3[0], ex2part4[0])))
            self.wait(1)
            self.play(Write(ex2part1[1]))
            self.wait(1)
            self.play(Write(ex2part4[1]))
            self.wait(1)
            self.play(Write(ex2part2[1]))
            self.wait(1)
            self.play(Write(ex2part3[1]))
            self.wait(1)
            self.play(Write(ex2_2[0]))
            self.wait(1)
            self.play(Write(ex2_2[1]))
            self.wait(1)


            self.play(
                Unwrite(VGroup(ex2part1[1], ex2part2[1], ex2part3[1], ex2part4[1])), 
                Transform(VGroup(ex2part1[0], ex2part2[0], ex2part3[0], ex2part4[0]), VGroup(ex2_2part1[0], ex2_2part2[0] ,ex2_2part3[0], ex2_2part4[0]))
                )
            
            self.wait(1)
            self.play(Write(ex2_2part1[1]))
            self.wait(1)
            self.play(Write(ex2_2part4[1]))
            self.wait(1)
            self.play(Write(ex2_2part2[1]))
            self.wait(1)
            self.play(Write(ex2_2part3[1]))
            self.wait(1)
            self.play(Write(ex2_3[0]))
            self.wait(1)
            self.play(Write(ex2_3[1]))
            self.wait(1)
            self.play(Write(ex2_3[2]))
            self.wait(1)
            self.play(Write(ex2_4))
            self.wait(1)
            self.play(Write(ex2_5))
            self.wait(1)
            self.play(TransformMatchingTex(ex2_5, ex2_6))
            self.wait(3)


            self.play(Unwrite(VGroup(title, ex2_1, ex2_2, ex2_3, ex2_4, ex2_6, ex2part1[0], ex2_2part1[1], ex2part2[0], ex2_2part2[1], ex2part3[0], ex2_2part3[1], ex2part4[0], ex2_2part4[1])))
            self.wait(1)

            
        def phoenix():
            title = Text(
                "Phoenix-Integration",
                font="Roboto Medium", 
                font_size=55
            )

            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))

            phoenix1 = MathTex(r"\int \sin(x)\cos(x) \, dx =", r"\sin^2(x) -", r"\int \sin(x)\cos(x) \, dx", font_size=35)
            phoenix2 = MathTex(r"2\int \sin(x)\cos(x)\, dx= \sin^2(x)", font_size=35)
            phoenix3 = MathTex(r"\int \sin(x)\cos(x)\, dx &= \frac{\sin^2(x)}{2} + c", font_size=35)

            phoenix = VGroup(phoenix1, phoenix2, phoenix3).arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_corner(LEFT + UP).shift(DOWN)

            phoenix1l = MathTex(r"|\; + \int \sin(x)\cos(x) \, dx", font_size=35)
            phoenix2l = MathTex(r"|\; :2", font_size=35)

            phoenixl = VGroup(phoenix1l, phoenix2l).arrange(DOWN, buff=0.45, aligned_edge=LEFT).to_corner(RIGHT + UP).shift(DOWN)

            part1 = MathTex(r"u =", "\sin(x)")
            part2 = MathTex(r"u' =", r"\cos(x)")
            part3 = MathTex(r"v =", r"\sin(x)")
            part4 = MathTex(r"v' =", r"\cos(x)")

            parts = VGroup(part1, part2, part3, part4)
            parts.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(DOWN).shift(UP*0.7)

            
            self.wait(1)
            self.play(Write(phoenix1[0]))
            self.play(Write(VGroup(part1[0], part2[0], part3[0], part4[0])))
            self.wait(1)
            self.play(Write(part1[1]))
            self.wait(1)
            self.play(Write(part4[1]))
            self.wait(1)
            self.play(Write(part2[1]))
            self.wait(1)
            self.play(Write(part3[1]))
            self.wait(1)
            self.play(Write(phoenix1[1]))
            self.wait(1)
            self.play(Write(phoenix1[2]))
            self.wait(1)
            self.play(Write(phoenix1l))
            self.wait(1)
            self.play(Write(phoenix2))
            self.wait(1)
            self.play(Write(phoenix2l))
            self.wait(1)
            self.play(Write(phoenix3))

        


        titlepage()
        topics()
        indefiniteIntegral()
        integralproductrule()
        examples()
        phoenix()