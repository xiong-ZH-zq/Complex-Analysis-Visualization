# manim -pqh PowerSeriesEuler.py PowerSeriesEuler
from manim import *
from math import factorial
class PowerSeriesEuler(Scene):
    def construct(self):

        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane))

        THETA = PI/3
        real_value_vector = Vector([np.exp(THETA),0],color = RED)     # e^\theta real vector
        label = MathTex(r"\mathrm{e}^{\theta}").next_to(real_value_vector, DR, 0.1)
        self.play(Create(real_value_vector),Create(label))

        # Euler Formula Text
        formula = MathTex(r"\mathrm{e}^{\mathrm{i}\theta}=",
            "1",
            r"+\mathrm{i}\theta",
            r"+\frac{(\mathrm{i}\theta)^2}{2!}",
            r"+\frac{(\mathrm{i}\theta)^3}{3!}",
            r"+\frac{(\mathrm{i}\theta)^4}{4!}",
            r"+\cdots"
        )
        formula.to_corner(UL)

        # the vector approaching e^\theta
        real_vector = Vector([1,0],color = BLUE)
        real_value = [1,0]

        # e^{i\theta}
        destination = Dot([np.cos(THETA),np.sin(THETA),0],color = WHITE,radius = 0.01)
        dot_label = MathTex(r"\mathrm{e}^{\mathrm{i}\theta}").next_to(destination,DOWN,0.1)

        # Directions for spiral vectors
        directions = [np.array([1,0,0]),np.array([0,1,0]),np.array([-1,0,0]),np.array([0,-1,0])]
        origin = np.array([1,0,0])

        self.play(
            Create(real_vector),
            Create(destination),
            Write(formula[0:2]),
            Create(dot_label),
            )

        
        for i in range(1,len(formula)-1):
            # write power series partly
            self.play(Transform(formula[i:i+1],formula[i:i+2]),run_time = 1.5)

            # change real value vector 
            increase = THETA**(i)/(factorial(i))
            real_value[0] += increase
            tmp_vector = Vector(real_value,color = BLUE)
            self.play(ReplacementTransform(real_vector,tmp_vector))
            real_vector = tmp_vector

            # spiral movement
            direction = directions[i%4]
            tmp_vector2 = Arrow(start = origin,end= origin+increase*direction, color = WHITE,buff = increase,stroke_width=1.5)
            self.play(Create(tmp_vector2))
            origin = origin+increase*direction
        
        self.wait()