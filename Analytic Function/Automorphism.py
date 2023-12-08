# cd .vscode\py
# manim -pqk Automorphism.py Automorphism
# -pql : 低质量渲染 -pqh : 高 -pqk : 4k
import numpy as np
from manim import *

class Automorphism(Scene):
    def construct(self):

        def f(z):
            a = complex(0.3, 0)  # (随便取一个表现一下)
            return (a-complex(z[0], z[1]))/(complex(1.0, 0)-a.conjugate()*complex(z[0], z[1]))

        def f1(z: complex):
            a = complex(0.4, 0.3)
            return z+complex(1.0, 0)/(-a.conjugate())

        def f2(z: complex):
            a = complex(0.4, 0.3)
            return complex(1.0, 0)/z

        def f3(z: complex):
            a = complex(0.4, 0.3)
            return -(complex(-1,0)+a*a.conjugate())/(a.conjugate()*a.conjugate())*z

        def f4(z: complex):
            a = complex(0.4, 0.3)
            return z+complex(1.0,0)/a.conjugate()

        # title
        text1 = Tex(
            r'The Automorphism: From unit circle to itself')
        text1.move_to(ORIGIN)
        self.play(Write(text1))
        self.wait()
        self.play(FadeOut(text1))

        # First part: Rotate
        text2 = Tex(
            r'The First Part: Rotate')
        text2.move_to(ORIGIN)
        self.play(Write(text2))
        self.wait()
        self.play(FadeOut(text2))
        text3 = Tex(
            r"We can express it like: \\ $f(z)=z \cdot e^{i\theta}$")
        text3.move_to(LEFT)
        self.play(FadeIn(text3))

        circle = Circle(radius=1, color=BLUE)
        circle.set_fill(opacity=0.5)
        circle.move_to([3.0, 0.0, 0.0])
        self.play(FadeIn(circle))  # 创建单位圆

        line1 = Line([3.0, 0.0, 0.0], [4.0, 0.0, 0.0]).set_stroke(width=0.5)
        line2 = Line([3.0, 0.0, 0.0], [4.0, 0.0, 0.0]).set_stroke(width=0.5)
        line3 = line2.copy()  # 创建标志线段

        center = [3.0, 0.0, 0.0]  # 旋转中心
        theta = ValueTracker(60)  # 初始角

        line2.rotate(theta.get_value()*DEGREES, about_point=center) #旋转

        angle = Angle(line1, line2, radius=0.2, other_angle=False) #角弧
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line2, radius=0.2+2*SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.2)
        ) #角标

        #animate
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
        self.play(FadeOut(text3))

        # Second part: the bijection $\phi(x)$
        # subpart1
        text4 = Tex(
            r'The Second part: the Bijection $\varphi(z)=\dfrac{a-z}{1-\overline{a}z}(|a|<1)$')
        text4.move_to(ORIGIN)
        self.play(Write(text4))
        self.wait()
        self.play(FadeOut(text4))

        text5 = Tex(
            r"For special case $a=0$ : \\ $\varphi(z)=-z$ \\ It's a reflection")
        text5.move_to(LEFT)
        self.play(FadeIn(text5))

        circle1 = Circle(radius=1, color=GREEN)
        circle1.set_fill(opacity=0.5)
        circle1.move_to([3.0, 0.0, 0.0])

        self.play(FadeIn(circle1))
        self.wait()
        self.play(Rotate(circle1, np.pi,
                  axis=RIGHT + DOWN), run_time=3)
        self.wait()

        self.play(FadeOut(circle1))
        self.play(FadeOut(text5))

        # subpart2
        text6 = Tex(
            r"For normal case, we find that: \\ $\varphi(0)=a$ \\ $\varphi(a)=0$ \\ It's like a replacement, but how about other points?")
        text6.move_to(ORIGIN)
        self.play(Write(text6))
        self.wait()
        self.play(FadeOut(text6))

        circle2 = Circle(radius=1.0)
        circle2.set_fill(opacity=0)
        circle2.move_to([-2.0, 0.0, 0.0])

        circle3 = Circle(radius=1.0)
        circle3.set_fill(opacity=0)
        circle3.move_to([2.0, 0.0, 0.0])

        self.play(FadeIn(circle2, circle3))

        point1 = Dot([0.3-2.0, 0.0, 0.0], color=RED, radius=0.08)
        point2 = Dot([2.0, 0.0, 0.0], color=RED, radius=0.08)
        tex1 = DecimalNumber(complex(0.3, 0), color=WHITE,
                             font_size=16).next_to(point1)
        tex2 = DecimalNumber(complex(0, 0), color=WHITE,
                             font_size=16).next_to(point2)

        thetad = ValueTracker(0.0)  # 初始角

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

        self.add(point1, point2, tex1, tex2)
        self.wait()
        self.play(thetad.animate.set_value(360), run_time=5)
        self.wait()

        self.play(FadeOut(point1, point2, tex1, tex2, circle2, circle3))
        self.wait()

        text7 = Tex(
            r"Additionally, we can see that as z moves a circle, \\ $\varphi(z)$ moves a circle, too.\\ This is about the Roucher Theorem. \\")
        text7.move_to(ORIGIN)

        self.play(Write(text7))
        self.wait()
        self.play(FadeOut(text7))

        text8 = Tex(
            r"However, come to the point. \\ To learn more about the bijection $\varphi(z)$. \\ We must study its analytical formula.")
        text8.move_to(ORIGIN)

        self.play(Write(text8))
        self.wait()
        self.play(FadeOut(text8))

        #The equalitation

        text9 = Tex(
            r"$\varphi(z)$"
        )
        text9.move_to(ORIGIN)

        self.play(Write(text9))
        self.wait()

        text9.generate_target()
        text9.target.shift(4 * LEFT)
        self.play(MoveToTarget(text9))
        self.wait()

        equal = Tex(
            r"="
        )
        equal.move_to(ORIGIN + 2 * LEFT)

        text10 = Tex(
            r"$\dfrac{a-z}{1-\overline{a}z}$"
        ).move_to(ORIGIN)

        self.play(Write(equal), Write(text10))
        self.wait()

        text11 = Tex(
            r"$z+\dfrac{1}{-\overline{a}}$"
        )

        self.play(FadeOut(equal), CounterclockwiseTransform(text10, text11))
        self.wait()

        text12 = Tex(
            r"$\dfrac{-\overline{a}z+1}{-\overline{a}}$"
        )
        self.play(CounterclockwiseTransform(text10, text12))
        self.wait()

        text13 = Tex(
            r"$\dfrac{-\overline{a}}{-\overline{a}z+1}$"
        )
        self.play(CounterclockwiseTransform(text10, text13))
        self.wait()

        text14 = Tex(
            r"$\dfrac{-\overline{a}}{-\overline{a}z+1}\cdot\dfrac{-(-1+a\overline{a})}{(-\overline{a})^2}$"
        )
        self.play(CounterclockwiseTransform(text10, text14))
        self.wait()

        text15 = Tex(
            r"$\dfrac{a\overline{a}-1}{(-\overline{a}z+1)\cdot\overline{a}}$"
        )
        self.play(CounterclockwiseTransform(text10, text15))
        self.wait()

        text16 = Tex(
            r"$\dfrac{a\overline{a}-1}{(-\overline{a}z+1)\cdot\overline{a}}+\dfrac{1}{\overline{a}}$"
        )
        self.play(CounterclockwiseTransform(text10, text16))
        self.wait()

        text17 = Tex(
            r"$\dfrac{a\overline{a}-1+1-\overline{a}z}{(-\overline{a}z+1)\cdot\overline{a}}$"
        )
        self.play(CounterclockwiseTransform(text10, text17))
        self.wait()

        text18 = Tex(
            r"$\dfrac{a\overline{a}-\overline{a}z}{(-\overline{a}z+1)\cdot\overline{a}}$"
        )
        self.play(CounterclockwiseTransform(text10, text18))
        self.wait()

        text19 = Tex(
            r"$\dfrac{a-z}{1-\overline{a}z}$"
        )
        self.play(FadeIn(equal), CounterclockwiseTransform(text10, text19))
        self.wait()

        self.play(FadeOut(text9, equal, text10))
        self.wait()

        text20 = Tex(
            r"Therefore, we found that: \\ $\varphi(z)=f_4\circ f_3\circ f_2\circ f_1(z)$ \\Where, $f_1=z+\dfrac{1}{-\overline{a}}$\\$f_2=\dfrac{1}{z}$\\$f_3=z\cdot -\dfrac{-1+a\overline{a}}{(-\overline{a})^2}$\\$f_4=z+\dfrac{1}{\overline{a}}$\\"
        ).move_to(ORIGIN)

        self.play(Write(text20))
        self.wait()
        self.wait()
        self.play(FadeOut(text20))
        self.wait()

        # Animation1

        text21 = Tex(
            r"So for the point $z$"
        ).move_to(ORIGIN)
        self.play(Write(text21))
        self.wait()

        text21.generate_target()
        text21.target.shift(3 * UP)
        self.play(MoveToTarget(text21))
        self.wait()

        circle4 = Circle(radius=1.0)
        circle4.set_fill(opacity=0)
        circle4.move_to([0.0, 0.0, 0.0])

        self.play(Create(circle4))

        z = complex(0.1, 0.5)
        point3 = Dot([0.1, 0.5, 0.0], color=RED, radius=0.08)
        tex3 = Tex(
            r"$z$").next_to(point3)

        self.add(point3, tex3)

        z = f1(z)
        point4 = Dot([z.real, z.imag, 0.0], color=RED, radius=0.08)
        vec1 = Arrow(start=point3, end=point4, color=WHITE)
        tex4 = Tex(
            r"$f_1$").next_to(vec1)
        self.play(FadeIn(point4, vec1, tex4))

        z = f2(z)
        point5 = Dot([z.real, z.imag, 0.0], color=RED, radius=0.08)
        vec2 = Arrow(start=point4, end=point5, color=WHITE)
        tex5 = Tex(
            r"$f_2$").next_to(vec2)
        self.play(FadeIn(point5, vec2, tex5))

        z = f3(z)
        point6 = Dot([z.real, z.imag, 0.0], color=RED, radius=0.08)
        vec3 = Arrow(start=point5, end=point6, color=WHITE)
        tex6 = Tex(
            r"$f_3$").next_to(vec3)
        self.play(FadeIn(point6, vec3, tex6))

        z = f4(z)
        point7 = Dot([z.real, z.imag, 0.0], color=RED, radius=0.08)
        vec4 = Arrow(start=point6, end=point7, color=WHITE)
        tex7 = Tex(
            r"$f_4$").next_to(vec4)
        tex8 = Tex(
            r"$\varphi(z)$").next_to(point7)
        self.play(FadeIn(point7, vec4, tex7, tex8))
        self.wait()

        self.play(FadeOut(text21, point3, point4, point5, point6, point7,
                  vec1, vec2, vec3, vec4, tex3, tex4, tex5, tex6, tex7, tex8, circle4))
        self.wait()

        text22 = Tex(
            r"Therefore, when we apply the bijection to the unit circle, \\ we can see:"
        ).move_to(ORIGIN)

        self.play(Write(text22))
        self.wait()
        self.play(FadeOut(text22))
        self.wait()

        def phi(z: complex) -> complex:
            a = complex(0.4, 0.3)
            return (a-z)/(1-a.conjugate()*z)

        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane))

        text23 = Tex(
            r"$\varphi(z)$"
        ).move_to(LEFT * 3)
        self.play(Write(text23))

        circle5 = Circle(radius=1.0)
        circle5.set_fill(color=PINK, opacity=0.5)
        self.play(Create(circle5))
        self.wait()

        self.play(ApplyComplexFunction(phi, circle5))
        self.wait()

        self.play(FadeOut(text23))
        self.wait()
        text24 = Tex(
            r"$f_4\circ f_3\circ f_2\circ f_1(z)$"
        ).move_to(LEFT * 3)
        self.play(Write(text24))

        self.play(ApplyComplexFunction(f1, circle5))
        self.play(ApplyComplexFunction(f2, circle5))
        self.play(ApplyComplexFunction(f3, circle5))
        self.play(ApplyComplexFunction(f4, circle5))
        self.wait()

        self.play(FadeOut(text24))
        self.wait()

        self.play(FadeOut(circle5, plane))

        text26 = Tex(r"Thanks!")
        self.play(Write(text26))
        self.wait()
        return super().construct()