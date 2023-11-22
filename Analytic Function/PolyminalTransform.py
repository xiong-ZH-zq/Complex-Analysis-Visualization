# manim -pqh PolyminalTransform.py PolyminalTransform
from manim import *
def function(z):
    return z**2+z
class PolyminalTransform(Scene):
    def construct(self):
        text = Tex(r"The transform of $f(z)=z^2+z$ on a unit circle")
        self.play(Write(text),run_time=1.5)
        self.play(text.animate.to_corner(UL))

        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane),run_time = 1.5)
        self.wait()

        circle = Circle(radius=1,color=RED)
        dotpos = [[1,0,0],[0,1,0],[-1,0,0],[0,-1,0]]
        dots = VGroup(*[Dot(dot,radius = 0.1) for dot in dotpos])

        # Use updater to keep the radius of point
        def dotsUpdater(mobj):
            for obj in mobj:
                obj.scale_to_fit_width(0.2)
        dots.add_updater(dotsUpdater, call_updater=True)

        group = VGroup(circle,dots)

        self.play(Create(group),run_time = 2)
        self.play(ApplyComplexFunction(mobject= group,function=function))
        self.wait()
        self.play(FadeOut(text),FadeOut(plane),FadeOut(group))
