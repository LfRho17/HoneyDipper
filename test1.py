from manim import *
from manim_slides import Slide
import numpy as np

class EfficientSineCircle(Slide):
    def construct(self):
        # 1. El motor: un tracker para el ángulo theta (inicia en 0)
        theta = ValueTracker(0)

        # 2. Geometría estática: El círculo a la izquierda y los ejes a la derecha
        circle = Circle(radius=1).shift(LEFT * 4)
        axes = Axes(
            x_range=[0, 4*PI, PI/2], 
            y_range=[-1.5, 1.5, 1], 
            x_length=6, y_length=3
        ).shift(RIGHT * 2)

        # 3. Elementos dinámicos: atados a theta mediante always_redraw
        
        # El punto que orbita el círculo
        dot_circle = always_redraw(lambda: Dot(
            circle.point_at_angle(theta.get_value()), color=YELLOW
        ))

        # El punto que avanza sobre el plano cartesiano
        dot_wave = always_redraw(lambda: Dot(
            axes.c2p(theta.get_value(), np.sin(theta.get_value())), color=YELLOW
        ))

        # La línea horizontal que conecta ambos puntos
        connecting_line = always_redraw(lambda: Line(
            dot_circle.get_center(), dot_wave.get_center(), color=BLUE, stroke_width=2
        ))

        # 4. LA MAGIA: TracedPath dibuja la estela del punto sin bucles manuales
        sine_curve = TracedPath(dot_wave.get_center, stroke_color=RED, stroke_width=3)

        # Añadimos todo a la pantalla
        self.add(circle, axes, dot_circle, dot_wave, connecting_line, sine_curve)
        self.next_slide()

        # 5. Animamos: Hacemos que theta vaya de 0 a 4*PI (dos vueltas completas)
        self.play(theta.animate.set_value(4 * PI), run_time=6, rate_func=linear)
