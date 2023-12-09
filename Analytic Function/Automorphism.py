# manim -pqh Automorphism.py Automorphism
import numpy as np
from manim import *

class Automorphism(Scene):
    def construct(self):
        def f(z):
            a = complex(0.3, 0)  # any a is OK
            return (a-complex(z[0], z[1]))/(complex(1.0, 0)-a.conjugate()*complex(z[0], z[1]))
        a = complex(0.4, 0.3)
        def f1(z: complex):
            return z+complex(1.0, 0)/(-a.conjugate())
        def f2(z: complex):
            return complex(1.0, 0)/z
        def f3(z: complex):
            return -(complex(-1,0)+a*a.conjugate())/(a.conjugate()*a.conjugate())*z
        def f4(z: complex):
            return z+complex(1.0,0)/a.conjugate()
        
        functions = [f,f1,f2,f3,f4]

        # title
        title = Tex(
            r'The Automorphism: From unit circle to itself')
        self.ShowAndThenFade(title,1)

        # First part: Rotate
        first_part_intro = Tex(
            r'The First Part: Rotate')
        self.ShowAndThenFade(first_part_intro,1)

        first_part_formula = Tex(
            r"We can express it like: \\ $f(z)=z \cdot \mathrm{e}^{\mathrm{i}\theta}$")
        first_part_formula.move_to(LEFT)
        self.play(FadeIn(first_part_formula))

        circle = Circle(radius=1, color=BLUE)
        circle.set_fill(opacity=0.5)
        circle.move_to([3.0, 0.0, 0.0])
        self.play(DrawBorderThenFill(circle))  # unit circle

        # the line that form the angle
        line1 = Line([3.0, 0.0, 0.0], [4.0, 0.0, 0.0]).set_stroke(width=0.5)
        line2 = Line([3.0, 0.0, 0.0], [4.0, 0.0, 0.0]).set_stroke(width=0.5)
        line3 = line2.copy()  

        center = [3.0, 0.0, 0.0]  # rotating center
        theta = ValueTracker(60)  # initial angle

        line2.rotate(theta.get_value()*DEGREES, about_point=center)

        angle = Angle(line1, line2, radius=0.2, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line2, radius=0.2+2*SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.2)
        )

        self.wait()
        self.add(line1, line2, angle, tex)
        self.wait()

        line2.add_updater(
            lambda x: x.become(line3.copy()).rotate(
                theta.get_value() * DEGREES, about_point=center
            )
        )
        angle.add_updater(
            lambda x: x.become(
                Angle(line1, line2, radius=0.2, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line2, radius=0.2+2*SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.2)
            )
        )

        self.play(tex.animate.set_color(RED))
        self.play(theta.animate.increment_value(300), run_time=5)
        self.wait()

        self.play(FadeOut(line1, line2, angle, tex, circle))
        self.play(FadeOut(first_part_formula))



        # Second part: the bijection $\phi(x)$
        # subpart1
        second_part_intro = Tex(
            r'The Second part: the Bijection $\varphi(z)=\dfrac{a-z}{1-\overline{a}z}(|a|<1)$')
        self.ShowAndThenFade(second_part_intro)

        reflection_intro = Tex(
            r"For special case $a=0$ : \\ $\varphi(z)=-z$ \\ It's a reflection")
        reflection_intro.move_to(LEFT)
        self.play(FadeIn(reflection_intro))

        circle1 = Circle(radius=1, color=GREEN)
        circle1.set_fill(opacity=0.5)
        circle1.move_to([3.0, 0.0, 0.0])

        self.play(FadeIn(circle1))
        self.wait()
        self.play(Rotate(circle1, np.pi,
                  axis=RIGHT + DOWN), run_time=3)
        self.wait()

        self.play(FadeOut(circle1))
        self.play(FadeOut(reflection_intro))

        # subpart2
        subpart2_intro = Tex(
            r"For normal case, we find that: \\ $\varphi(0)=a$ \\ $\varphi(a)=0$ \\ It's like a replacement, but how about other points?")
        self.ShowAndThenFade(subpart2_intro,1)

        circle2 = Circle(radius=1.0)
        circle2.set_fill(opacity=0)
        circle2.move_to([-2.0, 0.0, 0.0])

        circle3 = Circle(radius=1.0)
        circle3.set_fill(opacity=0)
        circle3.move_to([2.0, 0.0, 0.0])

        subpart2_title = Tex(r"The one-to-one relation between two points").to_edge(UP)
        self.play(Write(subpart2_title))

        self.play(FadeIn(circle2, circle3))

        point1 = Dot([0.3-2.0, 0.0, 0.0], color=RED, radius=0.08)
        point2 = Dot([2.0, 0.0, 0.0], color=RED, radius=0.08)
        tex1 = DecimalNumber(complex(0.3, 0), color=WHITE,
                             font_size=16).next_to(point1)
        tex2 = DecimalNumber(complex(0, 0), color=WHITE,
                             font_size=16).next_to(point2)

        thetad = ValueTracker(0.0)  # the valuetracker of initial angle

        point1.add_updater(
            lambda x: x.move_to(
                [-2.0 + 0.3 * np.cos(thetad.get_value() * DEGREES), 0.3 * np.sin(thetad.get_value() * DEGREES), 0.0])
        )
        point2.add_updater(
            lambda x: x.move_to(
                [f([0.3 * np.cos(thetad.get_value() * DEGREES), 0.3 * np.sin(thetad.get_value() * DEGREES), 0.0]).real+2.0, f([0.3 * np.cos(thetad.get_value() * DEGREES), 0.3 * np.sin(thetad.get_value() * DEGREES), 0.0]).imag, 0.0])
        )
        tex1.add_updater(
            lambda x: x.become(DecimalNumber(
                complex(point1.get_x() + 2, point1.get_y()), color=WHITE,
                font_size=16).next_to(point1))
        )
        tex2.add_updater(
            lambda x: x.become(DecimalNumber(
                complex(point2.get_x() - 2, point2.get_y()), color=WHITE,
                font_size=16).next_to(point2))
        )

        self.play(Create(point1),Create(point2), Create(tex1), Create(tex2))
        self.wait()
        self.play(thetad.animate.set_value(360), run_time=5)
        self.wait()

        self.ClearUp()
        self.wait()

        summary_of_subpart2 = Tex(
            r"Additionally, we can see that as $z$ moves a circle, \\ $\varphi(z)$ moves a circle, too.\\ This is about the Rouche Theorem. \\")
        summary_of_subpart2.move_to(ORIGIN)

        self.play(Write(summary_of_subpart2))
        self.wait(2.5)
        self.play(FadeOut(summary_of_subpart2))

        text8 = Tex(
            r"However, come to the point. \\ To learn more about the bijection $\varphi(z)$. \\ We must study its analytical formula.")
        text8.move_to(ORIGIN)

        self.play(Write(text8))
        self.wait(2)
        self.play(FadeOut(text8))

        #The transformation of formula

        phi_z = Tex(
            r"$\varphi(z)=$"
        )
        phi_z.move_to(ORIGIN)

        self.play(Write(phi_z))
        self.wait()

        phi_z.generate_target()
        phi_z.target.shift(4 * LEFT)
        self.play(MoveToTarget(phi_z))
        self.wait()

        changing_part = Tex(
            r"$\dfrac{a-z}{1-\overline{a}z}$",
            r"$z+\dfrac{1}{-\overline{a}}$",
            r"$\dfrac{-\overline{a}z+1}{-\overline{a}}$",
            r"$\dfrac{-\overline{a}}{-\overline{a}z+1}$",
            r"$\dfrac{-\overline{a}}{-\overline{a}z+1}\times\dfrac{-(-1+a\overline{a})}{(-\overline{a})^2}$",
            r"$\dfrac{a\overline{a}-1}{(-\overline{a}z+1)\cdot\overline{a}}$",
            r"$\dfrac{a\overline{a}-1}{(-\overline{a}z+1)\cdot\overline{a}}+\dfrac{1}{\overline{a}}$",
            r"$\dfrac{a\overline{a}-1+1-\overline{a}z}{(-\overline{a}z+1)\cdot\overline{a}}$",
            r"$\dfrac{a\overline{a}-\overline{a}z}{(-\overline{a}z+1)\cdot\overline{a}}$",
            r"$\dfrac{a-z}{1-\overline{a}z}$",
        )
        
        for i in range(0,10):
            part = changing_part[i].next_to(phi_z,RIGHT)
            self.play(Write(part),run_time = 0.5)
            self.wait()
            self.play(FadeOut(part))
        
        self.wait()
        self.ClearUp()

        # The end of calculation
        calculation_end = Tex(
            r"Therefore, we found that: \\ $\varphi(z)=f_4\circ f_3\circ f_2\circ f_1(z)$ \\Where, $f_1=z+\dfrac{1}{-\overline{a}}$\\$f_2=\dfrac{1}{z}$\\$f_3=z\cdot -\dfrac{-1+a\overline{a}}{(-\overline{a})^2}$\\$f_4=z+\dfrac{1}{\overline{a}}$\\"
        ).move_to(ORIGIN)

        self.ShowAndThenFade(calculation_end,2)
        # Animation1
        for_the_point_z = Tex(
            r"So for the point $z$"
        ).move_to(ORIGIN)
        self.play(Write(for_the_point_z))
        self.wait()

        for_the_point_z.generate_target()
        for_the_point_z.target.shift(3 * UP)
        self.play(MoveToTarget(for_the_point_z))
        self.wait()

        circle4 = Circle(radius=1.0)
        circle4.set_fill(opacity=0)
        circle4.move_to([0.0, 0.0, 0.0])

        self.play(Create(circle4))

        z = complex(0.1, 0.5)
        point = Dot([0.1, 0.5, 0.0], color=RED, radius=0.08)
        tex3 = Tex(
            r"$z$").next_to(point)

        self.add(point, tex3)

        for i in range(1,5):
            z = functions[i](z)
            prev_point = point
            point = Dot([z.real, z.imag, 0.0], color=RED, radius=0.08)
            vec = Arrow(start=prev_point, end=point, color=WHITE)
            tex = Tex(f"$f_{i}$").next_to(vec)
            
            self.play(FadeIn(tex,point,vec))
            self.wait()
            if i==4:
                point_tex = MathTex(r"\varphi(z)").next_to(point,RIGHT)
                self.play(FadeIn(point_tex))
            self.play(FadeOut(tex,vec))
        
        self.wait()
        # Clear all the things
        self.ClearUp()
        self.wait()

        transform_animation_intro = Tex(
            r"Therefore, when we apply the bijection to the unit circle, \\ we can see:"
        )
        self.ShowAndThenFade(transform_animation_intro)

        def phi(z: complex) -> complex:
            a = complex(0.4, 0.3)
            return (a-z)/(1-a.conjugate()*z)

        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane))

        transform_title = Tex(
            r"The transformation:",
            r"$\varphi(z)$"
        ).to_corner(UL)
        self.play(Write(transform_title))

        circle5 = Circle(radius=1.0)
        circle5.set_fill(color=PINK, opacity=0.5)
        self.play(Create(circle5))
        self.wait()

        self.play(ApplyComplexFunction(phi, circle5))
        self.wait()

        self.play(FadeOut(transform_title[1]))
        formula = Tex(
            r"$f_4\circ f_3\circ f_2\circ f_1(z)$"
        ).next_to(transform_title[0],RIGHT)
        self.play(Write(formula))

        # Apply the function one by one
        for i in range(1,5):
            self.play(ApplyComplexFunction(functions[i], circle5))
        self.wait()

        self.ClearUp()
        self.wait()

        end_up = Tex(r"Thanks!")
        self.ShowAndThenFade(end_up)
        return super().construct()
    
    def ShowAndThenFade(self,text:VMobject,time:int=1)-> None:
        self.play(Write(text))
        self.wait(time)
        self.play(FadeOut(text))
    
    def ClearUp(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
