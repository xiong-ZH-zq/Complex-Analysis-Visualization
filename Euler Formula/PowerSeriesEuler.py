# manim -pqh PowerSeriesEuler.py PowerSeriesEuler
from manim import *
from math import factorial
class PowerSeriesEuler(Scene):
    def construct(self):
        # Introduction
        title = Tex(r"Euler Formula in Power Series' View ($\theta = \frac{\pi}{ 2 }$)")
        self.play(Create(title),run_time = 2)
        self.play(FadeOut(title))


        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane))

        THETA = PI/2
        real_value_vector = Vector([np.exp(THETA),0],color = RED)     # e^\theta real vector
        label = MathTex(r"\mathrm{e}^{\theta}").next_to(real_value_vector, DR, 0.1)
        self.play(Create(real_value_vector),Create(label))

        # Euler exp_formula Text
        exp_formula = MathTex(r"\mathrm{e}^{\mathrm{i}\theta}=",
            "1",
            r"+\mathrm{i}\theta",
            r"+\frac{(\mathrm{i}\theta)^2}{2!}",
            r"+\frac{(\mathrm{i}\theta)^3}{3!}",
            r"+\frac{(\mathrm{i}\theta)^4}{4!}",
            r"+\cdots"
        )
        exp_formula.to_corner(UL)
        
        cos_formula = MathTex(r"\cos{\theta}=",
        r"1",
        r"-\frac{\theta^2}{2!}",
        r"+\frac{\theta^4}{4!}",
        r"-\cdots"
        )
        cos_formula.to_corner(DL)

        sin_formula = MathTex(r"\sin{\theta}=",
        r"\theta",
        r"-\frac{\theta^3}{3!}",
        r"+\cdots"
        )
        sin_formula.to_corner(DR)

        # the vector approaching e^\theta
        real_vector = Vector([1,0],color = BLUE)
        real_value = [1,0]

        # e^{i\theta}
        destination = Dot([np.cos(THETA),np.sin(THETA),0],color = WHITE,radius = 0.01)
        dot_label = MathTex(r"\mathrm{e}^{\mathrm{i}\theta}").next_to(destination,DR,0.1)

        # Directions for spiral vectors
        directions = [np.array([1,0,0]),np.array([0,1,0]),np.array([-1,0,0]),np.array([0,-1,0])]
        origin = np.array([1,0,0])

        self.play(
            Create(real_vector),
            Create(destination),
            Write(exp_formula[0:2]),
            Write(cos_formula[0:2]),
            Write(sin_formula[0]),
            Create(dot_label),
            )

        
        for i in range(1,len(exp_formula)-1):

            # Write Power Series Partly
            if(i%2 == 1):
                index = int((i-1)/2)
                self.play(
                    Transform(sin_formula[index:index+1],sin_formula[index:index+2]),
                    Transform(exp_formula[i:i+1],exp_formula[i:i+2]),
                    run_time = 1.5)
            else:
                index = int(i/2)
                self.play(
                    Transform(cos_formula[index:index+1],cos_formula[index:index+2]),
                    Transform(exp_formula[i:i+1],exp_formula[i:i+2]),
                    run_time = 1.5)

            if(i == len(exp_formula)-2):
                self.play(Transform(cos_formula[index+1:index+2],cos_formula[index+1:index+3]),run_time=1.5)

            # change real value vector 
            increase = THETA**(i)/(factorial(i))
            real_value[0] += increase
            tmp_vector = Vector(real_value,color = BLUE)
            self.play(ReplacementTransform(real_vector,tmp_vector))
            real_vector = tmp_vector

            # spiral movement
            direction = directions[i%4]
            tmp_vector2 = Arrow(start = origin,end= origin+increase*direction, color = WHITE,buff = increase,stroke_width=8)
            self.play(Create(tmp_vector2))
            origin = origin+increase*direction
        
        self.wait()
