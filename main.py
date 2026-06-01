from manim import *
from manim_slides import Slide

config.tex_template.add_to_preamble(r"\usepackage{esint}")

class title_page(Slide):
    def construct(self):
        logo = ImageMobject('honey.png').scale(0.4)
        
        title = Text("Project HoneyDipper", color = '#F29C1F').scale(1.5)
       # title.set_color_by_gradient(RED, YELLOW, GREEN, BLUE)

        header = Group(logo, title).arrange(RIGHT, buff=0.5)

        header.to_edge(UP, buff=0.5)

        self.play(FadeIn(logo)) # El logo aparece primero
       # self.next_slide() # Pausa para tu presentación
        
        self.play(Write(title)) 
