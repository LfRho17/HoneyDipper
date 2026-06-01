from manim import *
from manim_slides import Slide
import numpy as np

class EfficientSineCircle(Slide):
    def construct(self):
        theta = ValueTracker(0)

        circle = Circle(radius=1).shift(LEFT * 4)
        axes = Axes(
            x_range=[0, 4*PI, PI/2], 
            y_range=[-1.5, 1.5, 1], 
            x_length=6, y_length=3
        ).shift(RIGHT * 2)

        
        dot_circle = always_redraw(lambda: Dot(
            circle.point_at_angle(theta.get_value()), color=YELLOW
        ))

        dot_wave = always_redraw(lambda: Dot(
            axes.c2p(theta.get_value(), np.sin(theta.get_value())), color=YELLOW
        ))

        connecting_line = always_redraw(lambda: Line(
            dot_circle.get_center(), dot_wave.get_center(), color=BLUE, stroke_width=2
        ))

        sine_curve = TracedPath(dot_wave.get_center, stroke_color=RED, stroke_width=3)

        self.add(circle, axes, dot_circle, dot_wave, connecting_line, sine_curve)
        self.next_slide()

        self.play(theta.animate.set_value(4 * PI), run_time=6, rate_func=linear)
