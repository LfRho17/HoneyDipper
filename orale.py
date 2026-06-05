from manim import *
from manim_slides import Slide

latex_aditional = TexTemplate()
latex_aditional.add_to_preamble(r"\usepackage{esint}")
Tex.set_default(tex_template = latex_aditional)
MathTex.set_default(tex_template = latex_aditional)

class title_page(Slide):
    def construct(self):

        ###### Authors #####
        name_1 = Text("Luis F. Rosales")
        name_2 = Text("Daniela Chaviedo")

        about = Text("An Electromagnetic Theory project by two physics dummies").scale(0.3).move_to(ORIGIN)
        ##### -------- #####


        logo = ImageMobject('honey.png').scale(0.4)
        title = Text("Project HoneyDipper", color = '#F29C1F').scale(1.5)
        
        t_and_logo = Group(logo, title)
        t_and_logo.arrange(RIGHT, buff = 0.5)
        t_and_logo.to_edge(UP, buff = 0.5)

        authors = Group(name_1, name_2)
        authors.arrange(DOWN, aligned_edge = RIGHT, buff = 0.5).to_corner(DOWN + RIGHT, buff = 0.5).scale(0.6)
        self.play(FadeIn(authors))
        self.play(FadeIn(about))
        ##################### MAXWELL EQUATIONS #####################
        gaussLaw = MathTex(r"\vec{\nabla} \cdot \vec{E} = \frac{\rho}{\varepsilon_0}")
        gaussLaw_Magnetic = MathTex(r"\vec{\nabla} \cdot \vec{B} = 0")
        faradayLaw = MathTex(r"\vec{\nabla} \times \vec{E} = - \frac{\partial \vec{B}}{\partial t}")
        ampereLaw_MLaw = MathTex(r"\vec{\nabla} \times \vec{B} = \mu_0 \left(\vec{J} +\varepsilon_0 \frac{\partial \vec{E}}{\partial t} \right)")

        maxWelleq = VGroup(gaussLaw, gaussLaw_Magnetic, faradayLaw, ampereLaw_MLaw).scale(1)
        # maxWelleq.arrange(DOWN, aligned_edge = LEFT, buff = 0.5).to_corner(UP + LEFT, buff = 0.5)

        maxWelleq.arrange(DOWN, buff = 0.5) #.to_edge(DOWN, buff = 0.5)
        maxWelleq.move_to(ORIGIN)
        title_eq = Tex(r"Maxwell's Equations").to_edge(UP, buff = 0.5)

        tGauss = Tex(r"Gauss' Law").scale(1.2)
        #############################################################

        self.play(FadeIn(logo)) 
        self.play(Write(title))

        self.next_slide()

        self.play(FadeOut(authors))
        self.play(FadeOut(about))
        self.play(FadeOut(logo), ReplacementTransform(title, title_eq))
        self.play(Write(maxWelleq, run_time = 4))


        self.next_slide()

        self.play(
            FadeOut(ampereLaw_MLaw), 
            FadeOut(gaussLaw_Magnetic), 
            FadeOut(faradayLaw)
        )
        
        tGauss.move_to(title_eq)

        self.play(
            gaussLaw.animate.move_to(ORIGIN), 
            ReplacementTransform(title_eq, tGauss) 
        )
