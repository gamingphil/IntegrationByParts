from manim import *
from manim_slides import Slide
from manim_editor import PresentationSectionType



class PartielleIntegration(Scene):
    def construct(self):
        def pause():
            self.wait(0.1)
            self.next_section(type=PresentationSectionType.NORMAL)


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
            pause()
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
            pause()
            self.play(Write(topic1))
            pause()
            self.play(Write(topic2))
            pause()
            self.play(Write(topic3))
            pause()
            self.play(Write(topic4))
            pause()
            self.play(Unwrite(VGroup(topicstitle, topics)))
            pause()


        def integralproductrule():
            ### Product Rule of the Integral ###

            title = Text(
                "Die „Produktregel“ des Integrals",
                font="Roboto Medium", 
                font_size=55
            )

            productrule1 = MathTex(r"f(x) = u(x) \cdot v(x)", font_size = 60)
            productrule2 = MathTex(r"f'(x) = u'(x) \cdot v(x) + u(x) \cdot v'(x)", font_size = 60)
            productrule3 = MathTex(r"\int f(x)\, dx = \;?", font_size = 60)

            productrule = VGroup(productrule1, productrule2).set_x(0).arrange(DOWN, buff=1.2, aligned_edge=LEFT).to_corner(LEFT)
            productrule3.move_to(productrule2, aligned_edge=LEFT)


            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))
            pause()
            self.play(Write(productrule1))
            pause()
            self.play(Write(productrule2))
            pause()
            self.play(Transform(productrule2, productrule3))
            pause()


            derivation1 = MathTex("(uv)'", "=", "u'v + uv'")
            derivation1copy = MathTex("(uv)'", "=", "u'v + uv'")
            derivation2 = MathTex("\int", "(uv)'", "\,dx", "=", "\int", "u'v + uv'", "\,dx")
            derivation2copy = MathTex("\int (", "uv", ")' \,dx", "=", "\int u'v + uv' \,dx")
            derivation3 = MathTex("uv", "=", "\int u'v + uv' \,dx")
            derivation3copy = MathTex("uv", "=", "\int", "u'v", "+", "uv'", "\,dx")
            derivation4 = MathTex("uv", "=", "\int", "u'v", "\,dx", "+", "\int", "uv'", "\,dx")
            derivation4copy = MathTex("uv", "=", "\int u'v \,dx", "+", "\int uv' \,dx")
            derivation4_2 = MathTex("\int uv' \,dx", "=", "uv", "-", "\int u'v \,dx")

            derivation = VGroup(derivation1, derivation2, derivation3, derivation4).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT).to_corner(LEFT).shift(DOWN*0.2)

            derivation1copy.move_to(derivation1, aligned_edge=LEFT)
            derivation2copy.move_to(derivation2, aligned_edge=LEFT)
            derivation3copy.move_to(derivation3, aligned_edge=LEFT)
            derivation4copy.move_to(derivation4, aligned_edge=LEFT)
            derivation4_2.move_to(derivation4, aligned_edge=LEFT)


            self.play(Unwrite(VGroup(productrule1, productrule2)))
            self.play(Write(derivation1))
            self.add(derivation1copy)
            pause()
            self.play(TransformMatchingTex(derivation1, derivation2))
            self.add(derivation2copy)
            pause()
            self.play(Transform(derivation2copy,derivation3))
            self.add(derivation3copy)
            pause()
            self.play(TransformMatchingTex(derivation3copy, derivation4))
            self.add(derivation4copy)
            self.remove(derivation4)
            pause()
            self.play(TransformMatchingTex(derivation4copy, derivation4_2))
            self.wait(0.3)
            self.play(Circumscribe(derivation4copy))
            self.remove(derivation4copy)
            self.add(derivation4_2)
            pause()
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

            pause()
            self.play(Create(dividerline))
            self.play(Write(example_1))
            self.play(Write(example_2[0]))

            part1 = MathTex(r"u =", "x")
            part2 = MathTex(r"u' =", r"1")
            part3 = MathTex(r"v =", r"\sin(x)")
            part4 = MathTex(r"v' =", r"\cos(x)")

            parts = VGroup(part1, part2, part3, part4)
            parts.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(DOWN*1.5)

            pause()
            self.play(Write(VGroup(part1[0], part2[0], part3[0], part4[0])))

            
            ### ----> u and dv choice brackets <------ ###

            ubrace = Brace(example_1[1],sharpness=2,buff=0.2).set_color(RED_C)
            utext = MathTex(r"u", font_size=40).next_to(ubrace, DOWN).set_color(RED_C)

            pause()
            self.play(DrawBorderThenFill(ubrace), Write(utext))

            vbrace = Brace(example_1[2],sharpness=2,buff=0.1).set_color(GREEN_C)
            vtext = MathTex(r"v'", font_size=40).next_to(vbrace, DOWN*0.4).set_color(GREEN_C)

            pause()
            self.play(DrawBorderThenFill(vbrace), Write(vtext))


            derivationcolored = MathTex("\int uv' \,dx = uv - \int u'v \,dx")
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

            pause()
            self.play(Write(part1[1]))
            pause()
            self.play(Write(part4[1]))
            pause()
            self.play(Write(part2[1]))
            pause()
            self.play(Write(part3[1]))

            framebox1 = SurroundingRectangle(derivation4_2[2], buff = .1)
            framebox2group = VGroup(derivation4_2[3], derivation4_2[4])
            framebox2 = SurroundingRectangle(framebox2group, buff = .1)

            pause()
            self.play(Create(framebox1))
            pause()
            self.play(Write(example_2[1]))
            pause()
            self.play(ReplacementTransform(framebox1, framebox2))
            pause()
            self.play(Write(example_2[2]))

            pause()
            self.play(Write(example_3[0]))
            pause()
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

            pause()
            self.play(
                Unwrite(VGroup(example_2, example_3, part1[1], part2[1], part3[1], part4[1])), 
                Uncreate(framebox2), 
                Transform(VGroup(cpart1[0], part2[0], part3[0], cpart4[0]), VGroup(wpart1[0], wpart2[0] ,wpart3[0], wpart4[0]))
                )
            pause()

            self.play(
                ubrace.animate.set_color(GREEN_C),
                utext.animate.next_to(vbrace, DOWN),
                vbrace.animate.set_color(RED_C),
                vtext.animate.next_to(ubrace, DOWN*0.4),
            )


            pause()
            self.play(Write(wpart1[1]))
            pause()
            self.play(Write(wpart4[1]))
            pause()
            self.play(Write(wpart2[1]))
            pause()
            self.play(Write(wpart3[1]))
            pause()

            wrongexample_2 = MathTex(r"= \frac{1}{2}x^2 \cos(x)", r"-", r"\int -\frac{1}{2}x^2 \sin(x) \, dx", font_size = 40)
            wrongexample_2.to_corner(LEFT).shift(DOWN*2.5)

            self.play(Write(wrongexample_2[0]))
            pause()
            self.play(Write(VGroup(wrongexample_2[1], wrongexample_2[2])))
            pause()
            self.play(wrongexample_2[2].animate.scale(1.1).set_color(YELLOW_C))
            pause()


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

            pause()
            self.play(Write(udvchoice))
            pause()

            self.play(
                Unwrite(VGroup(title, derivationcolored, udvchoice)),
                Uncreate(dividerline, reverse=False)
                )
            pause()


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

            pause()
            self.play(Write(definite[0]))
            pause()
            self.play(Write(definite[1]))
            pause()
            self.play(Write(definite[2]))
            pause()
            self.play(Write(definiteTextGroup))
            pause()
            self.play(Write(indefinite[0]))
            pause()
            self.play(Write(indefinite[1]))
            pause()
            self.play(Write(indefinite[2]))
            pause()
            self.play(Write(indefiniteTextGroup))
            pause()
            self.play(Unwrite(VGroup(title, slide)))
            pause()

            
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
            ex1_3 = MathTex(r"= \frac{1}{5}x^5 \ln(x) - \int \frac{1}{5}x^4 \, dx")
            ex1_4 = MathTex(r"= \frac{1}{5}x^5 \ln(x) - \frac{1}{25}x^5 + c")

            ex1 = VGroup(ex1_1, ex1_2, ex1_3, ex1_4).arrange(DOWN).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT).to_corner(LEFT).shift(DOWN*0.3)

            ex1part1 = MathTex(r"u=", r"\ln(x)")
            ex1part2 = MathTex(r"u'=", r"\frac{1}{x}")
            ex1part3 = MathTex(r"v=", r"\frac{1}{5} x^5")
            ex1part4 = MathTex(r"v'=", r"x^4")

            ex1parts = VGroup(ex1part1, ex1part2, ex1part3, ex1part4)
            ex1parts.arrange_in_grid(cols=2, buff=0.5, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(LEFT*0.5)

            pause()
            self.play(Write(ex1_1))
            pause()
            self.play(Write(VGroup(ex1part1[0], ex1part2[0], ex1part3[0], ex1part4[0])))
            pause()
            self.play(Write(ex1part1[1]))
            pause()
            self.play(Write(ex1part4[1]))
            pause()
            self.play(Write(ex1part2[1]))
            pause()
            self.play(Write(ex1part3[1]))
            pause()
            self.play(Write(ex1_2[0]))
            pause()
            self.play(Write(ex1_2[1]))
            pause()
            self.play(Write(ex1_3))
            pause()
            self.play(Write(ex1_4))
            pause()

            self.play(Unwrite(VGroup(ex1_1, ex1_2, ex1_3, ex1_4, ex1part1, ex1part2, ex1part3, ex1part4)))


            ### EXAMPLE 2: x^2 * e^x


            ex2_1 = MathTex(r"\int x^2 e^x \, dx")
            ex2_2 = MathTex(r"= x^2 e^x-", r"\int 2x e^x \, dx")
            ex2_3 = MathTex(r"= x^2 e^x- \left(", r"2x e^x", r"-\int 2e^x \, dx \right)")
            ex2_4 = MathTex(r"= x^2 e^x", r"- \left( 2x e^x", r"- 2 e^x \right)")
            ex2_5 = MathTex(r"=", r"x^2", r"e^x", r"- 2x", r"e^x", r"+ 2", r"e^x", r"+ c")
            ex2_6 = MathTex(r"=", r"e^x", r"\left(", r"x^2", r"- 2x", r"+ 2", r"\right)", r"+ c")

            ex2 = VGroup(ex2_1, ex2_2, ex2_3, ex2_4, ex2_5).arrange(DOWN).set_x(0).arrange(DOWN, buff=0.4, aligned_edge=LEFT).scale(0.85).to_corner(LEFT).shift(DOWN*0.3)
            ex2_6.scale(0.85).move_to(ex2_5, aligned_edge=LEFT)


            ex2part1 = MathTex(r"u=", r"x^2")
            ex2part2 = MathTex(r"u'=", r"2x")
            ex2part3 = MathTex(r"v=", r"e^x")
            ex2part4 = MathTex(r"v'=", r"e^x")

            ex2parts = VGroup(ex2part1, ex2part2, ex2part3, ex2part4)
            ex2parts.arrange_in_grid(cols=2, buff=0.5, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(LEFT*0.5)

            ex2_2part1 = MathTex(r"u=", r"2x")
            ex2_2part2 = MathTex(r"u'=", r"2")
            ex2_2part3 = MathTex(r"v=", r"e^x")
            ex2_2part4 = MathTex(r"v'=", r"e^x")

            ex2_2parts = VGroup(ex2_2part1, ex2_2part2, ex2_2part3, ex2_2part4)
            ex2_2parts.arrange_in_grid(cols=2, buff=0.5, col_alignments="ll",col_widths=None).to_corner(RIGHT).shift(LEFT*0.5)


            pause()
            self.play(Write(ex2_1))
            pause()
            self.play(Write(VGroup(ex2part1[0], ex2part2[0], ex2part3[0], ex2part4[0])))
            pause()
            self.play(Write(ex2part1[1]))
            pause()
            self.play(Write(ex2part4[1]))
            pause()
            self.play(Write(ex2part2[1]))
            pause()
            self.play(Write(ex2part3[1]))
            pause()
            self.play(Write(ex2_2[0]))
            pause()
            self.play(Write(ex2_2[1]))
            pause()


            self.play(
                Unwrite(VGroup(ex2part1[1], ex2part2[1], ex2part3[1], ex2part4[1])), 
                Transform(VGroup(ex2part1[0], ex2part2[0], ex2part3[0], ex2part4[0]), VGroup(ex2_2part1[0], ex2_2part2[0] ,ex2_2part3[0], ex2_2part4[0]))
                )
            
            pause()
            self.play(Write(ex2_2part1[1]))
            pause()
            self.play(Write(ex2_2part4[1]))
            pause()
            self.play(Write(ex2_2part2[1]))
            pause()
            self.play(Write(ex2_2part3[1]))
            pause()
            self.play(Write(ex2_3[0]))
            pause()
            self.play(Write(ex2_3[1]))
            pause()
            self.play(Write(ex2_3[2]))
            pause()
            self.play(Write(ex2_4))
            pause()
            self.play(Write(ex2_5))
            pause()
            self.play(TransformMatchingTex(ex2_5, ex2_6))
            pause()


            self.play(Unwrite(VGroup(title, ex2_1, ex2_2, ex2_3, ex2_4, ex2_6, ex2part1[0], ex2_2part1[1], ex2part2[0], ex2_2part2[1], ex2part3[0], ex2_2part3[1], ex2part4[0], ex2_2part4[1])))
            pause()

            
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

            
            pause()
            self.play(Write(phoenix1[0]))
            pause()
            self.play(Write(VGroup(part1[0], part2[0], part3[0], part4[0])))
            pause()
            self.play(Write(part1[1]))
            pause()
            self.play(Write(part4[1]))
            pause()
            self.play(Write(part2[1]))
            pause()
            self.play(Write(part3[1]))
            pause()
            self.play(Write(phoenix1[1]))
            pause()
            self.play(Write(phoenix1[2]))
            pause()
            self.play(Write(phoenix1l))
            pause()
            self.play(Write(phoenix2))
            pause()
            self.play(Write(phoenix2l))
            pause()
            self.play(Write(phoenix3))
            pause()
            self.play(Unwrite(VGroup(phoenix1, phoenix1l, phoenix2, phoenix2l, phoenix3, part1, part2, part3, part4)))



            ### EXAMPLE: e^x sin(x)

            ex1 = MathTex(r"\int e^x \sin(x) \, dx =",  r"e^x \sin(x) -", r"\int e^x \cos(x) \, dx", font_size=35)
            ex2 = MathTex(r"\int e^x \sin(x) \, dx = e^x \sin(x) -\left(", r"e^x \cos(x) -", r"\int -e^x\sin(x) \, dx\right)", font_size=35)
            ex3_1 = MathTex(r"\int e^x \sin(x) \, dx &= e^x \sin(x) - e^x \cos(x)", r"+", r"\int", r"-", r"e^x\sin(x) \, dx", font_size=35)
            ex3_2 = MathTex(r"\int e^x \sin(x) \, dx &= e^x \sin(x) - e^x \cos(x)", r"-", r"\int", r"e^x\sin(x) \, dx", font_size=35)
            ex4_1 = MathTex(r"2\int e^x \sin(x) \, dx &=", r"e^x", r"\sin(x) -", r"e^x", r"\cos(x)", font_size=35)
            ex4_2 = MathTex(r"2\int e^x \sin(x) \, dx &=", r"e^x", r"\left(", r"\sin(x) -", r"\cos(x)", r"\right)", font_size=35)
            ex5 = MathTex(r"\int e^x \sin(x) \, dx &= \frac{1}{2} e^x\left(\sin(x) - \cos(x)\right) + c", font_size=35)

            ex = VGroup(ex1, ex2, ex3_1, ex4_1, ex5)
            ex.arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_corner(LEFT + UP).shift(DOWN)

            ex3_2.move_to(ex3_1, aligned_edge=LEFT)
            ex4_2.move_to(ex4_1, aligned_edge=LEFT)
            
            ex3l = MathTex(r"|\; + \int e^x \sin(x) \, dx", font_size=35)
            ex4l = MathTex(r"|\; :2", font_size=35)

            exl = VGroup(ex3l, ex4l).arrange(DOWN, buff=0.5, aligned_edge=LEFT).to_corner(RIGHT + UP).shift(DOWN*3.25)

            expart1 = MathTex(r"u =", "\sin(x)")
            expart2 = MathTex(r"u' =", r"\cos(x)")
            expart3 = MathTex(r"v =", r"e^x")
            expart4 = MathTex(r"v' =", r"e^x")

            exparts = VGroup(expart1, expart2, expart3, expart4)
            exparts.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(DOWN).shift(UP*0.7)

            expart2_1 = MathTex(r"u =", "\cos(x)")
            expart2_2 = MathTex(r"u' =", r"-\sin(x)")
            expart2_3 = MathTex(r"v =", r"e^x")
            expart2_4 = MathTex(r"v' =", r"e^x")

            exparts2 = VGroup(expart2_1, expart2_2, expart2_3, expart2_4)
            exparts2.arrange_in_grid(cols=2, buff=0.3, col_alignments="ll",col_widths=None).to_corner(DOWN).shift(UP*0.7)

            pause()
            self.play(Write(ex1[0]))
            pause()
            self.play(Write(VGroup(expart1[0], expart2[0], expart3[0], expart4[0])))
            pause()
            self.play(Write(expart1[1]))
            pause()
            self.play(Write(expart4[1]))
            pause()
            self.play(Write(expart2[1]))
            pause()
            self.play(Write(expart3[1]))
            pause()
            self.play(Write(ex1[1]))
            pause()
            self.play(Write(ex1[2]))
            pause()
            self.play(
                Unwrite(VGroup(expart1[1], expart2[1], expart3[1], expart4[1])), 
                Transform(VGroup(expart1[0], expart2[0], expart3[0], expart4[0]), VGroup(expart2_1[0], expart2_2[0] ,expart2_3[0], expart2_4[0]))
                )
            pause()
            self.play(Write(expart2_1[1]))
            pause()
            self.play(Write(expart2_4[1]))
            pause()
            self.play(Write(expart2_2[1]))
            pause()
            self.play(Write(expart2_3[1]))
            pause()
            self.play(Write(ex2[0]))
            pause()
            self.play(Write(ex2[1]))
            pause()
            self.play(Write(ex2[2]))
            pause()
            self.play(Unwrite(VGroup(expart1[0] ,expart2_1[1], expart2[0], expart2_2[1], expart3[0], expart2_3[1], expart4[0], expart2_4[1]), reverse=False))
            pause()
            self.play(Write(ex3_1))
            pause()
            self.play(TransformMatchingTex(ex3_1, ex3_2))
            pause()
            self.play(Write(ex3l))
            pause()
            self.play(Write(ex4_1))
            pause()
            self.play(TransformMatchingTex(ex4_1, ex4_2))
            pause()
            self.play(Write(ex4l))
            pause()
            self.play(Write(ex5))
            pause()
            self.play(Unwrite(VGroup(title, ex1, ex2, ex3_2, ex3l, ex4_2, ex4l, ex5)))
            pause()


        def dimethod():
            title = Text(
                "DI-Methode",
                font="Roboto Medium", 
                font_size=55
            )

            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))

            ### 1st stop: x^2 sin(3x)

            ex1 = MathTex(r"\int x^2 \sin(3x) \, dx")
            ex2 = MathTex(r"=", r"-\frac{1}{3}x^2\cos(3x)", r"+ \frac{2}{9}x \sin(3x)")
            ex3 = MathTex(r"+ \frac{2}{27}\cos(3x)", r"+c")

            ex = VGroup(ex1, ex2, ex3)
            ex.arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_corner(LEFT + UP).shift(DOWN)
            ex3.shift(RIGHT*0.5)

            emptycorner = MathTex(r"")
            sign1 = MathTex(r"+")
            sign2 = MathTex(r"-")
            sign3 = MathTex(r"+")
            sign4 = MathTex(r"-")

            Dhead = MathTex(r"D")
            Ihead = MathTex(r"I")

            D_1 = MathTex(r"x^2")
            D_2 = MathTex(r"2x")
            D_3 = MathTex(r"2")
            D_4 = MathTex(r"0")

            I_1 = MathTex(r"\sin(3x)")
            I_2 = MathTex(r"-\frac{1}{3}\cos(3x)")
            I_3 = MathTex(r"-\frac{1}{9}\sin(3x)")
            I_4 = MathTex(r"\frac{1}{27}\cos(3x)")

            DItable = VGroup(emptycorner, Dhead, Ihead, sign1, D_1, I_1, sign2, D_2, I_2, sign3, D_3, I_3, sign4, D_4, I_4)
            DItable.arrange_in_grid(cols=3, buff=0.6, col_alignments="ccc",col_widths=None).scale(0.9).to_corner(RIGHT).shift(LEFT*0.4)

            arrow1 = Arrow(start= D_1.get_center(), end=I_2.get_center(), buff=0.7).shift(LEFT*0.4)
            arrow2 = Arrow(start= D_2.get_center(), end=I_3.get_center(), buff=0.75).shift(LEFT*0.4)
            arrow3 = Arrow(start= D_3.get_center(), end=I_4.get_center(), buff=0.75).shift(LEFT*0.5)
            
            pause()
            self.play(Write(VGroup(ex1, ex2[0])))
            pause()
            self.play(Write(VGroup(Dhead, Ihead)))
            pause()
            self.play(Write(VGroup(sign1, sign2, sign3, sign4)))
            pause()
            self.play(Write(D_1))
            pause()
            self.play(Write(I_1))
            pause()
            self.play(Write(I_2))
            pause()
            self.play(Write(I_3))
            pause()
            self.play(Write(I_4))
            pause()
            self.play(Write(D_2))
            pause()
            self.play(Write(D_3))
            pause()
            self.play(Write(D_4))
            pause()
            self.play(
                Write(arrow1),
                sign1.animate.scale(1.1).set_color(YELLOW_C),
                D_1.animate.scale(1.1).set_color(YELLOW_C),
                I_2.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(ex2[1]))
            pause()
            self.play(
                Unwrite(arrow1),
                sign1.animate.scale(0.9).set_color(WHITE),
                D_1.animate.scale(0.9).set_color(WHITE),
                I_2.animate.scale(0.9).set_color(WHITE)
            )
            self.play(
                Write(arrow2),
                sign2.animate.scale(1.1).set_color(YELLOW_C),
                D_2.animate.scale(1.1).set_color(YELLOW_C),
                I_3.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(ex2[2]))
            pause()
            self.play(
                Unwrite(arrow2),
                sign2.animate.scale(0.9).set_color(WHITE),
                D_2.animate.scale(0.9).set_color(WHITE),
                I_3.animate.scale(0.9).set_color(WHITE)
            )
            self.play(
                Write(arrow3),
                sign3.animate.scale(1.1).set_color(YELLOW_C),
                D_3.animate.scale(1.1).set_color(YELLOW_C),
                I_4.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(ex3[0]))
            pause()
            self.play(
                Unwrite(arrow3),
                sign3.animate.scale(0.9).set_color(WHITE),
                D_3.animate.scale(0.9).set_color(WHITE),
                I_4.animate.scale(0.9).set_color(WHITE)
            )
            self.play(Write(ex3[1]))
            pause()
            self.play(Unwrite(VGroup(ex, DItable)))

            ### 2nd stop: ln(x)

            ex21_1 = MathTex(r"\int \ln(x)", r"\, dx")
            ex21_2 = MathTex(r"\int \ln(x)", r"\cdot 1", r"\, dx")
            ex22_1 = MathTex(r"=", r"x\ln(x)", r"- \int", r"\frac{1}{x} \cdot x", r"\,dx")
            ex22_2 = MathTex(r"=", r"x\ln(x)", r"- \int", r"1", r"\,dx")
            ex23 = MathTex(r"=x\ln(x) - x + c")

            exn2 = VGroup(ex21_1, ex22_1, ex23)
            exn2.arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_corner(LEFT + UP).shift(DOWN)
            ex21_2.move_to(ex21_1, aligned_edge=LEFT)
            ex22_2.move_to(ex22_1, aligned_edge=LEFT)

            emptycorner2 = MathTex(r"")
            sign21 = MathTex(r"+")
            sign22 = MathTex(r"-")

            D2head = MathTex(r"D")
            I2head = MathTex(r"I")

            D2_1 = MathTex(r"\ln(x)")
            D2_2 = MathTex(r"\frac{1}{x}")

            I2_1 = MathTex(r"1")
            I2_2 = MathTex(r"x")


            DItable2 = VGroup(emptycorner2, D2head, I2head, sign21, D2_1, I2_1, sign22, D2_2, I2_2)
            DItable2.arrange_in_grid(cols=3, buff=0.6, col_alignments="ccc",col_widths=None).scale(0.9).to_corner(RIGHT).shift(LEFT*1.5)

            arrow21 = Arrow(start= D2_1.get_center(), end=I2_2.get_center(), buff=0.5).shift(DOWN*0.1 + RIGHT*0.1)
            
            framebox1 = SurroundingRectangle(VGroup(sign22, D2_2, I2_2), buff = .2)

            pause()
            self.play(Write(VGroup(ex21_1, ex22_1[0])))
            self.play(Write(VGroup(D2head, I2head, sign21, sign22)))
            pause()
            self.play(TransformMatchingTex(ex21_1, ex21_2))
            pause()
            self.play(Write(D2_1))
            pause()
            self.play(Write(I2_1))
            pause()
            self.play(Write(I2_2))
            pause()
            self.play(Write(D2_2))
            pause()
            self.play(Create(framebox1))
            pause()
            self.play(Uncreate(framebox1))
            self.play(
                Write(arrow21),
                sign21.animate.scale(1.1).set_color(YELLOW_C),
                D2_1.animate.scale(1.1).set_color(YELLOW_C),
                I2_2.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(ex22_1[1]))
            pause()
            self.play(
                Unwrite(arrow21),
                sign21.animate.scale(0.9).set_color(WHITE),
                D2_1.animate.scale(0.9).set_color(WHITE),
                I2_2.animate.scale(0.9).set_color(WHITE)
            )
            self.play(
                sign22.animate.scale(1.1).set_color(YELLOW_C),
                D2_2.animate.scale(1.1).set_color(YELLOW_C),
                I2_2.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(VGroup(ex22_1[2], ex22_1[3], ex22_1[4])))
            pause()
            self.play(TransformMatchingTex(ex22_1, ex22_2))
            pause()
            self.play(
                sign22.animate.scale(0.9).set_color(WHITE),
                D2_2.animate.scale(0.9).set_color(WHITE),
                I2_2.animate.scale(0.9).set_color(WHITE)
            )
            self.play(Write(ex23))
            pause()
            self.play(Unwrite(VGroup(ex21_2, ex22_2, ex23, DItable2)))

            ### 3rd stop: e^-x cos(x)

            ex31 = MathTex(r"\int e^{-x} \cos(x) \, dx =", r"e^{-x}\sin(x)", r"- e^{-x}\cos(x)", r"- \int e^{-x} \cos(x) \,dx", font_size = 35)
            ex32_1 = MathTex(r"2\int e^{-x} \cos(x)\, dx =", r"e^{-x}", r"\sin(x) -", r"e^{-x}", r"\cos(x)", font_size = 35)
            ex32_2 = MathTex(r"2\int e^{-x} \cos(x)\, dx =", r"e^{-x}", r"\left(", r"\sin(x) -", r"\cos(x)",r"\right)", font_size = 35)
            ex33 = MathTex(r"\int e^{-x} \cos(x) \, dx = \frac{1}{2} e^{-x}\left(\sin(x) - \cos(x)\right)", font_size = 35)

            exn3 = VGroup(ex31, ex32_1, ex33)
            exn3.arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_corner(LEFT + UP).shift(DOWN)
            ex32_2.move_to(ex32_1, aligned_edge=LEFT)

            ex31l = MathTex(r"|\; + \int e^{-x} \cos(x) \, dx", font_size = 35)
            ex32l = MathTex(r"|\; :2", font_size = 35)

            ex3l = VGroup(ex31l, ex32l).arrange(DOWN, buff=0.45, aligned_edge=LEFT).to_corner(RIGHT + UP).shift(DOWN)


            emptycorner3 = MathTex(r"")
            sign31 = MathTex(r"+")
            sign32 = MathTex(r"-")
            sign33 = MathTex(r"+")

            D3head = MathTex(r"D")
            I3head = MathTex(r"I")

            D3_1 = MathTex(r"e^{-x}")
            D3_2 = MathTex(r"-e^{-x}")
            D3_3 = MathTex(r"e^{-x}")

            I3_1 = MathTex(r"\cos(x)")
            I3_2 = MathTex(r"\sin(x)")
            I3_3 = MathTex(r"-\cos(x)")

            DItable3 = VGroup(emptycorner3, D3head, I3head, sign31, D3_1, I3_1, sign32, D3_2, I3_2, sign33, D3_3, I3_3)
            DItable3.arrange_in_grid(cols=3, buff=0.6, col_alignments="ccc",col_widths=None).scale(0.9).to_corner(RIGHT + DOWN).shift(LEFT*0.4 + UP*0.5)

            arrow31 = Arrow(start= D3_1.get_center(), end=I3_2.get_center(), buff=0.7).shift(LEFT*0.1)
            arrow32 = Arrow(start= D3_2.get_center(), end=I3_3.get_center(), buff=0.75).shift(LEFT*0.1)

            framebox2 = SurroundingRectangle(VGroup(sign33, D3_3, I3_3), buff = .2)

            pause()
            self.play(Write(ex31[0]))
            self.play(Write(VGroup(D3head, I3head, sign31, sign32, sign33)))
            pause()
            self.play(Write(D3_1))
            pause()
            self.play(Write(I3_1))
            pause()
            self.play(Write(I3_2))
            pause()
            self.play(Write(I3_3))
            pause()
            self.play(Write(D3_2))
            pause()
            self.play(Write(D3_3))
            pause()
            self.play(Create(framebox2))
            pause()
            self.play(Uncreate(framebox2))
            self.play(
                Write(arrow31),
                sign31.animate.scale(1.1).set_color(YELLOW_C),
                D3_1.animate.scale(1.1).set_color(YELLOW_C),
                I3_2.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(ex31[1]))
            pause()
            self.play(
                Unwrite(arrow31),
                sign31.animate.scale(0.9).set_color(WHITE),
                D3_1.animate.scale(0.9).set_color(WHITE),
                I3_2.animate.scale(0.9).set_color(WHITE)
            )
            self.play(
                Write(arrow32),
                sign32.animate.scale(1.1).set_color(YELLOW_C),
                D3_2.animate.scale(1.1).set_color(YELLOW_C),
                I3_3.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(ex31[2]))
            pause()
            self.play(
                Unwrite(arrow32),
                sign32.animate.scale(0.9).set_color(WHITE),
                D3_2.animate.scale(0.9).set_color(WHITE),
                I3_3.animate.scale(0.9).set_color(WHITE)
            )
            self.play(
                sign33.animate.scale(1.1).set_color(YELLOW_C),
                D3_3.animate.scale(1.1).set_color(YELLOW_C),
                I3_3.animate.scale(1.1).set_color(YELLOW_C)
            )
            pause()
            self.play(Write(ex31[3]))
            pause()
            self.play(
                sign33.animate.scale(0.9).set_color(WHITE),
                D3_3.animate.scale(0.9).set_color(WHITE),
                I3_3.animate.scale(0.9).set_color(WHITE)
            )
            self.play(Write(ex31l))
            pause()
            self.play(Write(ex32_1))
            pause()
            self.play(TransformMatchingTex(ex32_1, ex32_2))
            pause()
            self.play(Write(ex32l))
            pause()
            self.play(Write(ex33))
            pause()
            self.play(Unwrite(VGroup(ex31, ex31l, ex32_2, ex32l, ex33, DItable3)))
            
            ### why does it work?

            formula = MathTex(r"\int uv' \,dx = uv -", r"\int u'v \,dx")
            formula.to_corner(UP).shift(DOWN)

            dividerline = Line(LEFT*6, RIGHT*6).shift(UP*0.9)

            dividerline.set_stroke(color=GREY, width=1)

            emptycornerw = MathTex(r"")
            signw1 = MathTex(r"+")
            signw2 = MathTex(r"-")
            signw3 = MathTex(r"+")

            Dwhead = MathTex(r"D")
            Iwhead = MathTex(r"I")

            Dw_1 = MathTex(r"u")
            Dw_2 = MathTex(r"u'")
            Dw_3 = MathTex(r"u''")

            Iw_1 = MathTex(r"v'")
            Iw_2 = MathTex(r"v")
            Iw_3 = MathTex(r"V")

            DItablew = VGroup(emptycornerw, Dwhead, Iwhead, signw1, Dw_1, Iw_1, signw2, Dw_2, Iw_2, signw3, Dw_3, Iw_3)
            DItablew.arrange_in_grid(cols=3, buff=0.6, col_alignments="ccc",col_widths=[0.5, 1, 1],).scale(0.9).to_corner( DOWN).shift(UP*0.7 + LEFT*0.5)
            Iw_1.shift(UP*0.08)
            Dw_2.shift(UP*0.08)

            arroww1 = Arrow(start= Dw_1.get_center(), end=Iw_2.get_center(), buff=0.55)#.shift(LEFT*0.1)

            pause()

            self.play(Write(formula))
            self.play(Create(dividerline))
            self.play(Write(VGroup(Dwhead, Iwhead, signw1, signw2, signw3)))
            pause()
            self.play(Write(VGroup(Dw_1, Iw_1)))
            self.play(
                Dw_1.animate.set_color(RED_C),
                Iw_1.animate.set_color(RED_C),
                formula[0][1:4].animate.set_color(RED_C)
            )
            pause()
            self.play(Write(VGroup(Dw_2, Iw_2)))
            pause()
            self.play(Write(arroww1))
            pause()
            self.play(
                arroww1.animate.set_color(GREEN_C),
                formula[0][7:9].animate.set_color(GREEN_C)
            )
            pause()
            self.play(
                Dw_2.animate.set_color(YELLOW_E),
                Iw_2.animate.set_color(YELLOW_E),
                formula[1][1:4].animate.set_color(YELLOW_E)
            )

            formula2 = MathTex(r"\int u'v \,dx")
            formula2[0][1:4].set_color(YELLOW_E)
            formula2.move_to(formula, aligned_edge=LEFT)

            pause()
            self.play(FadeOut(formula[0]))
            self.play(TransformMatchingShapes(formula[1], formula2))
            pause()

            formula3 = MathTex(r"\int uv' \,dx", r"= uv - \int u'v \,dx")
            formula3.to_corner(UP).shift(DOWN)
            formula3[0][1:4].set_color(RED_C)
            formula3[1][1:3].set_color(GREEN_C)
            formula3[1][5:8].set_color(YELLOW_E)

            self.play(TransformMatchingShapes(formula2, formula3[0]))
            pause()
            self.play(VGroup(Dw_1, Iw_1, Dw_2, Iw_2, arroww1).animate.shift(DOWN*0.94))
            pause()
            self.play(Write(formula3[1]))
            pause()
            self.play(Unwrite(VGroup(title, formula3, Dwhead, Iwhead, signw1, signw2, signw3, Dw_1, Iw_1, Dw_2, Iw_2, arroww1)), Uncreate(dividerline))
            pause()

            
        def ibpbounds():
            title = Text(
                "Was bei einem bestimmten Integral?",
                font="Roboto Medium", 
                font_size=55
            )

            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))

            originalformula = MathTex(r"\int uv' \,dx = uv - \int u'v \,dx", font_size= 50)

            formula = MathTex(r"\int_a^b uv' \, dx =", r"\left[uv\right]_a^b - \int_a^b u'v \, dx", font_size= 50)

            formulae = VGroup(originalformula, formula).arrange(DOWN, buff=1)

            question = MathTex(r"\int_a^b uv' \, dx =", r"\; ?", font_size= 50)
            question.move_to(formula, aligned_edge=LEFT)
            pause()
            self.play(Write(originalformula))
            pause()
            self.play(Write(question))
            pause()
            self.play(Unwrite(question[1]))
            self.play(Write(formula[1]))
            pause()
            self.play(Unwrite(VGroup(title, originalformula, question[0], formula[1])))
            pause()

        def end():
            thanks = Text(
                "Danke für eure Aufmerksamkeit!",
                font="Roboto Medium", 
                font_size=55
            )

            title = Text(
                "Quellen",
                font="Roboto Medium", 
                font_size=55
            )

            self.play(Write(thanks))
            pause()
            self.play(Unwrite(thanks))
            self.play(Write(title))
            self.play(title.animate.scale(0.7).to_corner(UP + LEFT))
            source1 = Tex("https://de.wikipedia.org/wiki/Partielle\_Integration", font_size=30)
            source2 = Tex("https://docs.editor.manim.community/", font_size=30)
            source3 = Tex("https://docs.manim.community/", font_size=30)
            source4 = Tex("https://en.wikipedia.org/wiki/Integration\_by\_parts", font_size=30)
            source5 = Tex("https://www.mathe-online.at/mathint/lexikon/i.html", font_size=30)
            source6 = Tex("https://youtu.be/2I-\_SV8cwsw", font_size=30)
            source7 = Tex("https://youtu.be/7t4xB6XZvJo", font_size=30)
            source8 = Tex("https://youtu.be/fikL-JSRB4U", font_size=30)
            source9 = Tex("https://youtu.be/I\_1haFAXr\_Y", font_size=30)

            sources = VGroup(source1, source2, source3, source4, source5, source6, source7, source8, source9).arrange(DOWN,buff=0.3, aligned_edge= LEFT).to_corner(LEFT)
            self.play(Write(sources))
            self.wait(0.1)

            


        titlepage()
        topics()
        indefiniteIntegral()
        integralproductrule()
        examples()
        phoenix()
        dimethod()
        ibpbounds()
        end()