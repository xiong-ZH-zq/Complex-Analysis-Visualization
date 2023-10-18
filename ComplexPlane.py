# manim -pqh ComplexPlane.py ComplexPlaneExample
from manim import *
class ComplexPlaneExample(Scene):
    def construct(self):
        # plane表示复平面，add_coordinates表示加坐标
        plane = ComplexPlane().add_coordinates()
        self.add(plane)

        # 建立Dot对象表示点
        d1 = Vector(plane.n2p(2 + 1j), color=YELLOW)    #设立颜色和坐标,n2p表示number_to_point
        d2 = Dot(plane.n2p(-1 - 1j), color=YELLOW)

        # 建立label，用LaTeX公式标注点
        label1 = MathTex(r"2+\mathrm{i}").next_to(d1, UR, 0.1)
        label2 = MathTex(r"\sqrt{2}\mathrm{e}^{\frac{5\pi}{4}}").next_to(d2, DL, 0.1)

        # 在平面上加点与标签
        self.add(
            d1,
            label1,
            d2,
            label2,
        )
