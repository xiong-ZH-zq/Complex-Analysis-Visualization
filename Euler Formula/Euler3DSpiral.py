# manim -qh Euler3DSpiral.py EulerThreeDSpiral
from manim import *
from typing import Tuple
class EulerThreeDSpiral(ThreeDScene):
    def construct(self):
        # Introduction
        title = Tex(r"Euler Formula in 3D Views")
        self.introduction(title)
        
        # 3D Axes
        axes = ThreeDAxes(
            x_range=(-0.1, 4.25),
            y_range=(-1.5, 1.5),
            z_range=(-1.5, 1.5),
            y_length=5, z_length=5,
            axis_config={"color": WHITE}
        ).add_coordinates()
        
        # Camera initial angle
        camera_orig_phi, camera_orig_theta = 75*DEGREES, -30*DEGREES

        curve, curve_extension, formula = self.show_curve(
            axes=axes, camera_orig_phi=camera_orig_phi, camera_orig_theta=camera_orig_theta)
        self.wait()

        self.show_sin(curve=curve, formula=formula,
                      camera_orig_phi=camera_orig_phi, camera_orig_theta=camera_orig_theta)
        self.wait()

        self.show_cos(curve=curve, formula=formula,
                      camera_orig_phi=camera_orig_phi, camera_orig_theta=camera_orig_theta)
        self.wait()

        self.play(FadeOut(axes, curve, curve_extension, formula, shift=IN))
        self.wait()
    
    def introduction(self,title) -> None:
        """Show Introduction Scene
        :param title: The Tex class to be shown
        """
        title.move_to(ORIGIN)
        self.play(Create(title),run_time = 1)
        self.wait()
        self.play(FadeOut(title),run_time = 1)


    def show_curve(self, axes, camera_orig_phi, camera_orig_theta) -> Tuple[Mobject, Mobject, Mobject]:
        """Draw the 3D Curve
        :param axes: ThreeDAxes
        :param camera_orig_phi: origin phi
        :param camera_orig_theta: origin theta
        """
        curve, curve_extension = [
            ParametricFunction(
                lambda t: axes.coords_to_point(
                    t, np.exp(complex(0, PI*t)).real, np.exp(complex(0, PI*t)).imag),
                t_range=t_range,
                color=WHITE
            ) for t_range in [(0, 2, 0.1), (2, 4, 0.1)]]

        # 公式生成
        formula = MathTex(
            r"z = \mathrm{e}^{\mathrm{i} t \pi}, \quad t\in [0, 2]", color=WHITE)
        formula.rotate(axis=OUT, angle=90 *
                       DEGREES).rotate(axis=UP, angle=90*DEGREES)
        formula.next_to(curve, UP + OUT)

        # 设定摄像机的位置
        self.set_camera_orientation(
            phi=90*DEGREES, theta=0, focal_distance=10000)
        self.play(Create(axes),Create(curve, run_time=2), Write(formula))
        self.wait()
        
        # 重新设定相机位置
        self.move_camera(phi=camera_orig_phi, theta=camera_orig_theta)
        self.wait()

        # 更改范围并延长曲线
        four = MathTex("4", color=WHITE).rotate(
            axis=OUT, angle=90*DEGREES).rotate(axis=UP, angle=90*DEGREES)
        four.move_to(formula[0][12])
        self.play(Create(curve_extension, run_time=2),
                  formula[0][12].animate(run_time=1.5).become(four))

        return curve, curve_extension, formula

    def show_sin(self, curve, formula, camera_orig_phi, camera_orig_theta):
        """Show the Side of Sine Curve
        :param curve: the 3D curve
        :param formula: the formula to be shown
        """

        self.move_camera(phi=90*DEGREES, theta=-90 *
                         DEGREES, focal_distance=10000)
        self.remove(formula)
        self.wait()
        sine_text = MathTex(
            r"\sin(t \pi) = \mathrm{Im}(z)", color=WHITE)
        sine_text.rotate(axis=RIGHT, angle=90 *
                         DEGREES).next_to(curve, 6*RIGHT + OUT)
        self.play(Write(sine_text), run_time=1)
        self.wait(4)

        # 整体展示
        self.add(formula)
        self.move_camera(phi=camera_orig_phi, theta=camera_orig_theta)
        self.play(FadeOut(sine_text, run_time=2))

    def show_cos(self, curve, formula, camera_orig_phi, camera_orig_theta):
        """Show the Side of Cosine Curve
        the params are the same as show_sin()
        """
        self.move_camera(phi=0, theta=-90*DEGREES, focal_distance=10000)
        self.remove(formula)
        self.wait()
        cosine_text = MathTex(r"\cos(t \pi) = \mathrm{Re}(z)",
                              color=WHITE).next_to(curve, 6*RIGHT + UP)
        self.play(Write(cosine_text), run_time=1)
        self.wait(4)

        # Overview
        self.add(formula)
        self.move_camera(phi=camera_orig_phi, theta=camera_orig_theta)
        self.play(FadeOut(cosine_text, run_time=2))
