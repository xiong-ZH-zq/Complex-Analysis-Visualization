# manim -qh MobiusTransform.py MobiusTransform

class MobiusTransform(Scene):
    def construct(self):
        # Introduction Scene
        a = complex(0.3,0)    # the constant a
        text = Tex(r"The transform of $f(z)=\dfrac{a-z}{1-\overline{a}z}$ on a unit circle")
        text2 = Tex(r"Every Mobius transform will change circles to circles.").to_corner(UL)
        
        # Mobius Transform Function
        def function(z):
            return (a-z)/(1-a.conjugate()*z)

        self.play(Write(text),run_time=1.5)
        self.play(text.animate.to_corner(UL))

        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane),run_time = 2)
        self.wait()

        circle = Circle(radius=1,color=RED)
        dotpos = [[1,0,0],[0,1,0],[-1,0,0],[0,-1,0]]
        colors =  [BLUE,RED,YELLOW,GREEN]
        dots = VGroup(*[Dot(dot,radius = 0.1,color=colors[i]) for i,dot in enumerate(dotpos)])

        # Use updater to keep the radius of point
        def dotsUpdater(mobj):
            for obj in mobj:
                obj.scale_to_fit_width(0.2)
        dots.add_updater(dotsUpdater, call_updater=True)

        group = VGroup(circle,dots)

        # Animation of Transform
        self.play(Create(group),run_time = 5)
        self.play(ReplacementTransform(text,text2),run_time= 2)
        self.play(ApplyComplexFunction(mobject= group,function=function),run_time = 5)
        self.wait()
        self.play(FadeOut(text),FadeOut(plane),FadeOut(group))
