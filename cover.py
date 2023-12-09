# draw the cover of Complex Analysis
# manim -p --format=gif cover.py ComplexAnalysisCover
from manim import *
import numpy as np
config.background_color = BLACK

class ComplexAnalysisCover(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()
        title = Tex(r"Complex Analysis Visualization").move_to(UP*2)
        self.play(Create(plane))
        self.play(Write(title),run_time = 2)
        self.wait()

        unit_circle = Circle(radius=1,color=WHITE)
        self.play(Create(unit_circle))
        self.wait()
        
        theta = ValueTracker(0.0)
        vector = Vector([1,0,0],color = WHITE).add_updater(
            lambda vector: vector.become(
                Vector([np.cos(theta.get_value() * DEGREES),np.sin(theta.get_value() * DEGREES),0.0],color = WHITE)
            )
        )
        
        label = MathTex(r"\mathrm{e}^{\mathrm{i}0}")
        label.add_updater(
            lambda label: label.become(
                MathTex(r"\mathrm{e}^{"+f"{round(theta.get_value()/(180),2)}"+r'\mathrm{i}\pi}').next_to(vector,RIGHT)
                )
        )


        self.play(Create(vector),Write(label))
        self.play(theta.animate.set_value(360), run_time=3)
        
        self.wait()
        self.ClearUp()

    def ClearUp(self):
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
