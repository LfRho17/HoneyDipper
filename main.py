from manim import *
from manim_slides import Slide

latex_aditional = TexTemplate()
latex_aditional.add_to_preamble(r"\usepackage{esint}")
Tex.set_default(tex_template = latex_aditional)
MathTex.set_default(tex_template = latex_aditional)

class title_page(Slide):
    def construct(self):
        logo = ImageMobject('honey.png').scale(0.4)
        title = Text("Project HoneyDipper", color = '#F29C1F').scale(1.5)
        
        t_and_logo = Group(logo, title)
        t_and_logo.arrange(RIGHT, buff = 0.5)
        t_and_logo.to_edge(UP, buff = 0.5)

        ##################### MAXWELL EQUATIONS #####################
        gaussLaw = MathTex(r"\vec{\nabla} \cdot \vec{E} = \frac{\rho}{\varepsilon_0}")
        gaussLaw_Magnetic = MathTex(r"\vec{\nabla} \cdot \vec{B} = 0")
        faradayLaw = MathTex(r"\vec{\nabla} \times \vec{E} = - \frac{\partial \vec{B}}{\partial t}")
        ampereLaw_MLaw = MathTex(r"\vec{\nabla} \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}")

        maxWelleq = VGroup(gaussLaw, gaussLaw_Magnetic, faradayLaw, ampereLaw_MLaw).scale(0.5)
        maxWelleq.arrange(DOWN, aligned_edge = LEFT, buff = 0.5).to_corner(UP + LEFT, buff = 0.5)

        title_eq = Tex(r"Maxwell's Equations").to_edge(UP, buff = 0.5)
        #############################################################

        self.play(FadeIn(logo)) 
        self.play(Write(title))

        self.next_slide()

        self.play(FadeOut(logo), Transform(title, title_eq))
        self.play(Write(maxWelleq, run_time = 4))
