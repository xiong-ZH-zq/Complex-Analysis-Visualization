# manim -pqh AComplexNumber.py ComplexNumberExample
from manim import *
class ComplexNumberExample(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()
        self.add(plane)

        d1 = Vector(plane.n2p(4 + 3j), color=YELLOW)
        d1b_x = Brace(d1)    # 实部/The real part
        d1b_x_text = d1b_x.get_tex(r"\mathrm{Re}(z)")
        self.add(d1,d1b_x,d1b_x_text)

        d1b_y = Brace(d1,direction=RIGHT)    # 虚部/The imaginary part
        d1b_y_text = d1b_y.get_tex(r"\mathrm{Im}(z)")
        self.add(d1b_y,d1b_y_text)

        d1b_m = Brace(d1,direction=d1.copy().rotate(PI/2).get_unit_vector())    # 复数的模/The module of z
        d1b_m_text = d1b_m.get_tex(r"|z|")

        self.add(d1b_m,d1b_m_text)
